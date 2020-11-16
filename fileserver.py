from concurrent import futures
import logging
from cryptography.fernet import Fernet
import grpc
import os, sys
import random

import pb.filesw_pb2 as filepb
import pb.filesw_pb2_grpc as filepb_grpc
import pb.central_pb2 as centralpb
import pb.central_pb2_grpc as central_grpc

class FileServer(filepb_grpc.FileServerServicer):
    def __init__(self, port, directory, key):
        self.clientCount = 0
        self.sessionCount = 0
        self.folderCount = 0
        self.fileCount = 0
        self.port = port
        self.currentClient = ""
        self.directory = directory
        self.sessionKeys = {}
        self.kdcKey = key
        self.session = ("", "")

    def ShareKey(self, request, context):
        Ticket = request.file2.encode()
        fernet = Fernet(self.kdcKey)

        plaintext = fernet.decrypt(Ticket).decode().split()
        shared_key, pid = plaintext
        self.clientCount += 1

        if self.session != ("", ""):
            print("Session over!\n")
            self.session = ("", "")


        print("\n{} )Received a session key from client pid {} with a nonce.".format(self.clientCount, pid))

        shared_key = shared_key.encode()
        self.sessionKeys[pid] = shared_key

        self.session = (pid, shared_key.decode())
        self.sessionCount = 0

        fernet = Fernet(shared_key)
        plaintext = str(int(fernet.decrypt(request.file1.encode()).decode()) - 1)
        ciphertext = fernet.encrypt(plaintext.encode()).decode()

        print("   Sent a nonce to the client for authentication.\n   Connection has been established!\n")

        return filepb.Response(name = ciphertext)

    def LS(self, request, context):   
        fernet = Fernet(self.session[1].encode())
        self.sessionCount += 1
        List = os.listdir(self.directory)
        print("   {}) LS request from Client with PID {}.".format(self.sessionCount, self.session[0]))
        # Pb = filepb.Files()
        plaintext = ""
        for l in List:
            plaintext += l + " "
            # f = Pb.file.add()
            # f.n = l
        if len(plaintext) > 0:
            plaintext = plaintext[:-1]
        ciphertext = fernet.encrypt(plaintext.encode()).decode()
        return filepb.Response(name = ciphertext)
    
    def CP(self, request, context):   
        fernet = Fernet(self.session[1].encode())
        file1, file2 = fernet.decrypt(request.name.encode()).decode().split(" ")
        self.sessionCount += 1
        print("   {}) CP request from Client with PID {}.".format(self.sessionCount, self.session[0]))
        with open(os.path.join(self.directory, file1), 'r') as f:
            content = f.read()
        with open(os.path.join(self.directory, file2), 'a') as f:
            f.write("\n" + content)
        with open(os.path.join(self.directory, file2), 'r') as f:
            content = f.read()

        content = fernet.encrypt((content).encode()).decode()
        return filepb.Response(name = content)
    
    def CAT(self, request, context):   
        fernet = Fernet(self.session[1].encode())
        self.sessionCount += 1
        print("   {}) CAT request from Client with PID {}.".format(self.sessionCount, self.session[0]))
        plaintext = fernet.decrypt(request.name.encode()).decode()
        with open(os.path.join(self.directory, plaintext), 'r') as f:
            content = f.read()

        ciphertext = fernet.encrypt((content).encode()).decode()
        return filepb.Response(name = ciphertext)
    
    def PWD(self, request, context):   
        fernet = Fernet(self.session[1].encode())
        self.sessionCount += 1

        print("   {}) PWD request from Client with PID {}.".format(self.sessionCount, self.session[0]))
        ciphertext = fernet.encrypt((self.directory).encode()).decode()
        return filepb.Response(name = ciphertext)
    
    def NEW(self, request, context):
        self.sessionCount += 1
        fernet = Fernet(self.session[1].encode())
        plaintext = fernet.decrypt(request.name.encode()).decode()

        fer = Fernet(self.kdcKey)
        ciphertext = fer.encrypt((plaintext + " " + self.session[0]).encode()).decode()
        msg = "FS" + self.port + " " + ciphertext
        
        channel = grpc.insecure_channel('localhost:50051')
        stub = central_grpc.CentralStub(channel)
        stub.NewFile(centralpb.Request(name = msg))

        content = "File has been created by client with PID " + self.session[0]
        with open(os.path.join(self.directory, plaintext), 'w') as f:
            f.write(content)
        print("   {}) NEW request from Client with PID {}.".format(self.sessionCount, self.session[0]))
        ciphertext = fernet.encrypt((content).encode()).decode()
        return filepb.Response(name = ciphertext)
    

def serve(port, directory, Key):

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    filepb_grpc.add_FileServerServicer_to_server(FileServer(port, directory, Key.encode()), server)

    insecure_port = '[::]:' + port
    server.add_insecure_port(insecure_port)
    print("File Server is now active: ")

    try :
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down the server.")

    return 

def makedirectory(port, directory):
    if os.path.exists(directory) == False:
        os.mkdir(directory)

    print(directory)
    for i in range(0, 3):
        name = os.path.join(directory, str(i) + ".txt")
        with open(name, 'w') as f:
            f.write("This is the first line in the text file - {}".format(name))
    print("Directory updated !!")

def generate_nonce(length=8):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])

def sendToCentral(id, nonce = "", Key = ""):
    channel = grpc.insecure_channel('localhost:50051')
    stub = central_grpc.CentralStub(channel)

    response = stub.Registration(centralpb.Request(name = id))
    fernet = Fernet(Key.encode())
    plaintext = fernet.decrypt(response.name.encode()).decode()
    if int(plaintext) + 1 == int(nonce):
        print("Registration complete successfully.")

def Register(port, shared_key):
    """ 
    namePORT - nonce - Shared key
    nonce - 1 : encrypted by shared key
    """
    with open('secret.key', 'rb') as f:
        public_key = f.read()
    nonce = generate_nonce()
    plaintext = "FS" + port + " " + str(nonce) + " " + shared_key
    fernet = Fernet(public_key)
    ciphertext = fernet.encrypt(plaintext.encode()).decode()

    sendToCentral(ciphertext, nonce, shared_key)


if __name__ == '__main__':
    logging.basicConfig()
    port = sys.argv[1]
    
    directory = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(directory, "FS" + port)

    if sys.argv[2] == '1':
        makedirectory(port, directory)

    print("Server started at port ", port, ".\nSent a Registration request to Central Server.")

    key = Fernet.generate_key().decode()
    Register(port, key)
    serve(port, directory, key)
