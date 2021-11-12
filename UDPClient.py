import socket 
import threading
import os 
import sys

cleintIP  = "127.0.0.1"
clientPort = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind((cleintIP, clientPort))

print("Hello and welcome to a simple UDP chat box\n"  )

name = input("Enter Your name: ")
if(name == "QUIT"):
    os._exit(1)
print("Waiting........")


#Sending name to the other person
sname = "{}".format(name)
clientSocket.sendto(sname.encode(),("127.0.0.1",4321))

#Reciving name fomr 
inName = clientSocket.recvfrom(2048)
print("\nStarting Chat with: "  + inName[0].decode()) 


print("\tType *QUIT* to exit the program at any time.\n")
print("===================================================\n")

def send():
    while True:
        outMess =  input()
        if (outMess == "QUIT"):
            os._exit(1)

        sendMess = "{}>> {}".format(name,outMess)
        clientSocket.sendto(sendMess.encode(),("127.0.0.1",4321) ) #server IP and port


def receive():
    while True: 
        inMess = clientSocket.recvfrom(2048)
        print("\t\t\t" + inMess[0].decode()) 

#creating threads 
T1 = threading.Thread(target=send)
T2 = threading.Thread(target=receive)
#starting threads 
T1.start()
T2.start()
