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
    
def doTask(task, serverName, id, shared_key):
    port = serverName[2:]
    channel = 'localhost:' + port
    channel = grpc.insecure_channel(channel)
    stub = filepb_grpc.FileServerStub(channel)
    id = str(id)
    fernet = Fernet(shared_key)

    if task == 'ls':
        response = stub.LS(filepb.Request(name = ""))
        plaintext = fernet.decrypt(response.name.encode()).decode().split(" ")
        print("\nThe Files present in {} are as follows: ".format(serverName))
        for i, s in enumerate(plaintext):
            print(i + 1, ") " + s)
    
    elif task == 'cat':
        print("Enter the filename: ", end = " ")
        filenme = input()
        ciphertext = fernet.encrypt((filenme).encode()).decode()
        response = stub.CAT(filepb.Request(name = ciphertext))
        plaintext = fernet.decrypt(response.name.encode()).decode()

        if plaintext == 'N':
            print("File not exists !")
        else:
            print("\nThe contents of the given file are: \n")
            print(plaintext)

    elif task == 'cp':
        print("Enter the two file names: ")
        f1 = input("First File : ")
        f2 = input("Second File : ")
        print("\nThe Contents of file {} are copied into the file {}.".format(f1, f2))

        ciphertext = fernet.encrypt((f1 + " " + f2).encode()).decode()
        response = stub.CP(filepb.Request(name = ciphertext))
        plaintext = fernet.decrypt(response.name.encode()).decode()
        if plaintext == 'N':
            print("File not exists !")
        else:
            print("\nThe Request has been processed. The new content of {} is :\n\n{}".format(f2, plaintext))

    elif task == 'pwd':
        response = stub.PWD(filepb.Request(name = ""))
        plaintext = fernet.decrypt(response.name.encode()).decode()
        print("\nThe directory is as follows: ", plaintext)

    elif task == 'new':
        filename = input("Please Enter the File name: ")
        ciphertext = fernet.encrypt((filename).encode()).decode()
        response = stub.NEW(filepb.Request(name = ciphertext))
        plaintext = fernet.decrypt(response.name.encode()).decode()
        print("\nThe Contents of the new file are: \n\n", plaintext)        

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
    """
    pid, server, nonce
    nonce, fs, shared_key, ticket
    (ticket) = decoded ciphertext encrypted by kdcFS key - (session_key + pid)
    make a rpc req to FS with two messages - (nonce)sharedkey.decode() and ticketcipher 
    Response encrypted by session_key - nonce-1 
    """
    nonce = generate_nonce()
    msg = str(pid) + " " + cur_serv + " " + nonce

    channel = grpc.insecure_channel('localhost:50051')
    stub = central_grpc.CentralStub(channel)
    response = stub.GenKey(centralpb.Request(name = msg)).name.encode()

    print("\nSent a request to the KDC for a ticket to establish session between the client with pid {} and File Server {}.".format(pid, cur_serv))

    fernet = Fernet(kdcKey.encode())
    plaintext = fernet.decrypt(response).decode()
    _, _, shared_key, ticketCipher = plaintext.split(" ")

    shared_key = shared_key.encode()
    fernet = Fernet(shared_key)
    plaintext = nonce
    ciphertext = fernet.encrypt(plaintext.encode()).decode()

    print("Session Key and Ticket received.\nSent RPC request to FS with an encrypted nonce and Ticket")

    port = cur_serv[2:]
    channel = 'localhost:' + port
    channel = grpc.insecure_channel(channel)
    stub = filepb_grpc.FileServerStub(channel)
    response = stub.ShareKey(filepb.CPReq(file1 = ciphertext, file2 = ticketCipher)).name.encode()

    plaintext = fernet.decrypt(response).decode()

    if int(plaintext) + 1 == int(nonce):
        print("Session has been established between client with pid {} and file server {}.\n".format(pid, cur_serv))
        return shared_key
    else:
        print("Connection failed to establish.")
        exit()

def checkCenter(key, pid):
    fernet = Fernet(key.encode())
    channel = grpc.insecure_channel('localhost:50051')
    stub = central_grpc.CentralStub(channel)

    response = stub.GetUpdate(centralpb.Request(name = pid))
    plaintext = fernet.decrypt(response.name.encode()).decode()
    if len(plaintext) == 0:
        return 
    
    print("\nThe following files have been added : FileName[FileServer]\n")
    plaintext = plaintext.split()
    for i,p in enumerate(plaintext):
        print ("  ", i+1, ") ", p)
    return    


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
    shared_key = getSharedKey(servers[cur_serv], client_kdc, id)    # Bytes type
    
    print("\nThe File Server selected is {}. Please select the RPC service for the same !\n".format(servers[cur_serv]))
    print("1. ls - list files in given FS\n2. cp - copy content of one file to another\n3. cat - Display contents of given file\n4. pwd - show current directory\n5. new - add a new file")
    print()

    Task = ['ls', 'cp', 'cat', 'pwd', 'new']
    cur_task = (input()).lower()
    stop = 0

    while stop != 1:

        if cur_task in Task:
            doTask(cur_task, servers[cur_serv], id, shared_key)
        else:
            print("Wrong input.")

        checkCenter(client_kdc, str(id))
        print("\nSelect another service. (N for none)  :  ", end = "")
        cur_task = (input()).lower()

        if cur_task == "n":
            print("\nDo you want to change the File Server?(y / N)", end = "  ")
            cont = (input()).lower()
            if cont == 'n':
                stop = 1
            else:
                print("Session over with {}.\n".format(cur_serv))
                cur_serv = selectServer(serverNum)
                shared_key = getSharedKey(servers[cur_serv], client_kdc, id)
                print("\nEnter the type of Service :", end = "  ")
                cur_task = (input("LS / CAT / CP / PWD ::  ")).lower()



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
