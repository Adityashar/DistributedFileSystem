# Copyright 2015 gRPC authors.
from __future__ import print_function
import logging
from cryptography.fernet import Fernet
import grpc
import sys, os
import random

import pb.central_pb2 as centralpb
import pb.central_pb2_grpc as central_grpc
import pb.filesw_pb2 as filepb
import pb.filesw_pb2_grpc as filepb_grpc

def generate_nonce(length=8):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


def selectServer(serversLen):
    print("Index of selected FS: ", end='  ')
    index = int(input()) - 1

    while index + 1 > serversLen:
        print("Enter a valid number !!!", end = "   ")
        index = int(input()) - 1
    
    return index

def centralServer(id, Key = "", nonce = ""):
    channel = grpc.insecure_channel('localhost:50051')
    stub = central_grpc.CentralStub(channel)
    servers = []

    """ choose service from stub and then proto message from pb
        serialized message with respect to the proto    """

    if nonce == "":
        response = stub.GiveFS(centralpb.Request(name = str(id))).name.encode()
        fernet = Fernet(Key.encode())
        plaintext = fernet.decrypt(response).decode()
        servers = plaintext.split(" ")
        print("The Number of File Servers active are {}.\nSelect the File Server to establish communication:\n".format(len(servers)))
        for i, s in enumerate(servers):
            print(i + 1, ") " + s)

    else:
        # print(id.decode(), type(id))
        response = stub.Registration(centralpb.Request(name = id.decode()))
        fernet = Fernet(Key.encode())
        plaintext = fernet.decrypt(response.name.encode()).decode()
        if int(plaintext) + 1 == int(nonce):
            print("Registration complete successfully.")

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
        response = stub.CAT(filepb.Request(name = filenme))
        print("The contents of the given file are: ")
        print(response.name)

    elif task == 'cp':
        print("Enter the two file names: ")
        f1 = input()
        f2 = input()
        print("\nThe Contents of file {} are copied into the file {}.".format(f1, f2))
        response = stub.CP(filepb.CPReq(file1 = f1, file2 = f2))
        print("The Request has been processed. The new content of {} is :\n{}".format(f2, response.name))

    elif task == 'pwd':
        response = stub.PWD(filepb.Request(name = "")).name
        print("The directory is as follows: ", response)

    elif task == 'new':
        print("Added")
        response = ""

    else:
        response = "The service requested does not exist !"

    return response

"""
client sends rpc to centre with the latter's public key
rpc includes a key generated at the client itself
at the centre, the key: pid(client) is appended to a list
pid - nonce - key(decoded-nonbinary)
"""

def registration(id, key):
    with open("secret.key", 'rb') as f:
        public_key = f.read()
    
    nonce = generate_nonce()
    f = Fernet(public_key)
    plaintext = str(id) + " " + nonce + " " + key 
    ciphertext = f.encrypt(plaintext.encode())

    print("Registration request sent to central server by client!")
    centralServer(ciphertext, key, nonce)

def getSharedKey(cur_serv, kdcKey, pid):
    nonce = generate_nonce()
    msg = str(pid) + " " + cur_serv + " " + nonce

    channel = grpc.insecure_channel('localhost:50051')
    stub = central_grpc.CentralStub(channel)
    response = stub.

if __name__ == '__main__':
    logging.basicConfig()
    print('The Client is functioning now.')
    id = os.getpid()

    client_kdc = Fernet.generate_key().decode()
    # print(str(client_kdc), client_kdc.decode().encode(), type(generate_nonce()))
    registration(id, client_kdc)
    
    servers = centralServer(id, client_kdc)
    serverNum = len(servers)
    cur_serv = selectServer(serverNum)     
    shared_key = getSharedKey(servers[cur_serv], client_kdc, id)
    
    # print("\nThe File Server selected is {}. Please select the RPC service for the same !\n".format(servers[cur_serv][1]))
    # print("1. ls - list files in given FS\n2. cp - copy content of one file to another\n3. cat - Display contents of given file\n4. pwd - show current directory\n5. new - add a new file")
    # print()

    # Task = ['ls', 'cp', 'cat', 'pwd']
    # cur_task = (input()).lower()
    # stop = 0

    # while stop != 1:

    #     doTask(cur_task, servers[cur_serv], id)

    #     print("Select another service. (N for none)  :")
    #     cur_task = (input()).lower()

    #     if cur_task == "n":
    #         print("Do you want to change the File Server?(y / N)", end = "  ")
    #         cont = (input()).lower()
    #         if cont == 'n':
    #             stop = 1
    #         else:
    #             cur_serv = selectServer(serverNum)
    #             print("Enter the type of Service: ", end = "   ")
    #             cur_task = (input()).lower()



"""

registration : 
FS with central
client with central

serverlist:
client with central

needham schroedhar:

1. use the needham service of centralserver
2. message contains : pid, nonce, FS
3. response is encrypted by client[pid]Key contains : Ticket, nonce, key, 
4. send a request to fs with ticket, pid - separate strings
5. nonce - 1 encrypted by shared key

authentication required each time FS is selected
use the shared key for rpc

establish a shared key for both


"""
