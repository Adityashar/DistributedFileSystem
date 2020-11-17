from concurrent import futures
import logging
from cryptography.fernet import Fernet
import grpc

import pb.central_pb2 as centralpb
import pb.central_pb2_grpc as central_grpc


class Central(central_grpc.CentralServicer):

    def __init__(self, key):
        self.public_key = key
        self.client_keys = {}
        self.fs_keys = {}
        self.client_notification = {}

    def Decrypt(self, content):
        fernet = Fernet(self.public_key)
        plaintext = fernet.decrypt(content).decode()
        return plaintext.split(" ")

    def Encrypt(self, content, PD, pid = ""):
        if pid != "":
            # print(self.client_keys, self.fs_keys)
            if PD == 1:    
                fernet = Fernet(self.client_keys[pid])
            else:
                fernet = Fernet(self.fs_keys[pid])
        else:
            fernet = Fernet(self.public_key)
        ciphertext = fernet.encrypt(content.encode())
        return ciphertext

    def GiveFS(self, request, context):
        pid = request.name
        print("Received a request for FS list by client with PID {}.".format(pid))
        fs = centralpb.Response2()
        # print(self.fs_keys.keys(), type(self.fs_keys.keys()))
        plaintext = " ".join(list(self.fs_keys.keys()))
        ciphertext = self.Encrypt(plaintext, 1, pid).decode()
        fs.name = ciphertext

        return fs
        # fs.num = 3
        # port_i = 4000
        # init = "FS"
        # for i in range(0, fs.num):
        #     server = fs.serv.add()
        #     server.port = str(port_i + i)
        #     server.id = init + str(i + 1)

        # return fs

    def Registration(self, request, context):
        """
        Request - pid : nonce : key - encrypted message
        Decrypt, then make list, make a response : nonce -1 
        Encrypt response and send it
        """
        items = self.Decrypt(request.name.encode())
        
        # print(items)
        if "FS" in items[0]:
            self.fs_keys[items[0]] = items[2].encode()
            r = str(int(items[1])-1)
            print("Received a request for Registration by FS with Port {}.\nSent a Response to the FS: `{}`\n".format(items[0][2:], r))
            res = self.Encrypt(r, 0, items[0])
        else:
            self.client_keys[items[0]] = items[2].encode()
            self.client_notification[items[0]] = []
            r = str(int(items[1])-1)
            print("Received a request for Registration by client with PID {}.\nSent a response to the client: `{}`\n".format(items[0], r))
            res = self.Encrypt(r, 1, items[0])
        

        return centralpb.Response2(name = res.decode())
        # PROTO MESSAGE
        # serialized response with respect to the proto
    
    def GenKey(self, request, context):
        """
        pid, nonce, FS
        response encrypted by kdc_key : nonce, FS, shared_key, ticket((shared_key + pid) encrypted by FS_KDC)
        """
        items = request.name.split()
        pid, fs, nonce = items

        kdc_client_key = self.client_keys[pid]
        kdc_fs_key = self.fs_keys[fs]
        shared_key = Fernet.generate_key().decode()         
        
        ticket = shared_key + " " + pid
        ticketCipher = self.Encrypt(ticket, 0, fs).decode() 

        plaintext = nonce + " " + fs + " " + shared_key + " " + ticketCipher
        ciphertext = self.Encrypt(plaintext, 1, pid).decode()

        print("\nReceived a Session Establishment Request from client with pid {} for FileServer {}.\nSent a Ticket and generated a Session-Key for the same.\n".format(pid, fs))

        return centralpb.Response2(name = ciphertext)
    
    def NewFile(self, request, context):
        fileserver, filename = request.name.split()
        fernet = Fernet(self.fs_keys[fileserver])
        filename, pid = fernet.decrypt(filename.encode()).decode().split()

        print("New File {} has been created in FileServer {} by client with pid {}.".format(filename, fileserver, pid))

        for k in self.client_notification.keys():
            if pid != k:
                self.client_notification[k].append((filename, fileserver))

        return centralpb.Response2(name = "")

    def GetUpdate(self, request, context):
        pid = request.name
        fernet = Fernet(self.client_keys[pid])
        plaintext = ""
        for u in self.client_notification[pid] : 
            plaintext += "{}[{}] ".format(u[0], u[1])
        
        if len(plaintext) > 0:
            plaintext = plaintext[:-1]
            print("Sent a Notification to {} about new files created.".format(request.name))
            self.client_notification[pid] = []
        ciphertext = fernet.encrypt(plaintext.encode()).decode()

        return centralpb.Response2(name = ciphertext)

def serve():

    key = Fernet.generate_key()
    with open("secret.key", 'wb') as f:
        f.write(key)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    central_grpc.add_CentralServicer_to_server(Central(key), server)

    server.add_insecure_port('[::]:50051')
    try :
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down the server.")


if __name__ == '__main__':

    logging.basicConfig()
    serve()
