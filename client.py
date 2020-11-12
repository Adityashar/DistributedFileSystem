# Copyright 2015 gRPC authors.
from __future__ import print_function
import logging

import grpc
import sys, os

import pb.central_pb2 as centralpb
import pb.central_pb2_grpc as central_grpc
import pb.filesw_pb2 as filepb
import pb.filesw_pb2_grpc as filepb_grpc


def selectServer(serversLen):
    print("Index of selected FS: ", end='  ')
    index = int(input()) - 1

    while index + 1 > serversLen:
        print("Enter a valid number !!!", end = "   ")
        index = int(input()) - 1
    
    return index

def getServers(id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = central_grpc.CentralStub(channel)
    servers = []

    """ choose service from stub and then proto message from pb
        serialized message with respect to the proto    """

    response = stub.GiveFS(centralpb.Request(name = str(id)))
    print("The Number of File Servers active are {}.\nSelect the File Server to establish communication:\n".format(response.num))
    for i, s in enumerate(response.serv):
        print(i + 1, ") " + s.id)
        servers.append((s.port, s.id))

    return servers
    
def doTask(task, server, id):
    port, serverName = server
    channel = 'localhost:' + port
    channel = grpc.insecure_channel(channel)
    stub = filepb_grpc.FileServerStub(channel)
    id = str(id)

    if task == 'ls':
        response = stub.LS(filepb.Request(name = id))
        print("The Files present in {} are as follows: ".format(serverName))
        for i, s in enumerate(response.file):
            print(i + 1, ") " + s.n)
    
    elif task == 'cat':
        print("Enter the filename: ", end = " ")
        filenme = input()
        response = stub.CAT(filepb.Request(name = "1.txt"))
        print("The contents of the given file are: ")
        print(response.name)

    elif task == 'cp':
        print("Enter the two file names: ")
        file1 = input()
        file2 = input()
        response = stub.CP(filepb.CPReq(file1 = "1.txt", file2 = "2.txt"))
        print("The Request has been processed.")


    elif task == 'pwd':
        response = stub.PWD(filepb.Request(name = "")).name
        print("The directory is as follows: ", response)

    elif task == 'new':
        print("Added")
        response = ""

    else:
        response = "The service requested does not exist !"

    return response

if __name__ == '__main__':
    logging.basicConfig()
    print('The Client is functioning now.')
    id = os.getpid()
    
    servers = getServers(id)
    serverNum = len(servers)
    cur_serv = selectServer(serverNum) 
    
    print("\nThe File Server selected is {}. Please select the RPC service for the same !\n".format(servers[cur_serv][1]))
    print("1. ls - list files in given FS\n2. cp - copy content of one file to another\n3. cat - Display contents of given file\n4. pwd - show current directory\n5. new - add a new file")

    Task = ['ls', 'cp', 'cat', 'pwd']
    cur_task = (input()).lower()
    stop = 0

    while stop != 1:

        doTask(cur_task, servers[cur_serv], id)

        print("Select another service. (N for none)  :")
        cur_task = (input()).lower()

        if cur_task == "n":
            print("Do you want to change the File Server?(y / N)", end = "  ")
            cont = (input()).lower()
            if cont == 'n':
                stop = 1
            else:
                cur_serv = selectServer(serverNum)
                print("Enter the type of Service: ", end = "   ")
                cur_task = (input()).lower()