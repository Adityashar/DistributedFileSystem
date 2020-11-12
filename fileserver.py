from concurrent import futures
import logging

import grpc
import os, sys

import pb.filesw_pb2 as filepb
import pb.filesw_pb2_grpc as filepb_grpc


class FileServer(filepb_grpc.FileServerServicer):
    def __init__(self, port, directory):
        self.clientCount = 0
        self.folderCount = 0
        self.fileCount = 0
        self.port = port
        self.currentClient = ""
        self.directory = directory

    def LS(self, request, context):   
        self.clientCount += 1
        List = os.listdir(self.directory)
        Pb = filepb.Files()
        for l in List:
            f = Pb.file.add()
            f.n = l
        return Pb
    
    def CP(self, request, context):
        self.clientCount += 1
        
        return filepb.Response(name = "Done")
    
    def CAT(self, request, context):
        self.clientCount += 1
        with open(os.path.join(self.directory, request.name), 'r') as f:
            content = f.read()
        return filepb.Response(name = content)
    
    def PWD(self, request, context):
        self.clientCount += 1
        return filepb.Response(name = self.directory)
    
    def NEW(self, request, context):
        self.clientCount += 1
        
        return filepb.Response(name = "Added File/Folder")
    

def serve(port, directory):

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    filepb_grpc.add_FileServerServicer_to_server(FileServer(port, directory), server)

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
    for i in range(0, 3):
        name = str(i)
        with open(directory + name, 'w') as f:
            f.write("This is the first line in the text file - {}".format(name))
    print("Directory updated !!")
    return 

if __name__ == '__main__':
    logging.basicConfig()
    port = sys.argv[1]
    
    directory = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(directory, "FS" + port)

    if sys.argv[2] == '1':
        makedirectory(port, directory)

    print("Server started at port ", port)
    serve(port, directory)
