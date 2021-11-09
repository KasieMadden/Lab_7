import socket 
import threading
import os 
import sys

cleintIP  = "127.0.0.1"
clientPort = 1234
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind((cleintIP, clientPort))

print("\n[*] Starting Chat with client code...%s:%d" % (cleintIP,clientPort))
print("The chat is ready.\n\n")

#os.system("tput setaf 2")
name = input("Enter Your name: ")
if(name == "QUIT"):
    os._exit(1)

print("Type *QUIT* to exit the program. \n\n")


def send():
    while True:
        
        outMess = input()
        if (outMess == "QUIT"):
            os._exit(1)

        sendMess = "{}>> {}".format(name,outMess)
        clientSocket.sendto(sendMess.encode(),("127.0.0.1",4321) ) #server IP and port


def receive():
    while True: 
        inMess = clientSocket.recvfrom(2048)
        print("\t\t\t\t" + inMess[0].decode()) 

#creating threads 
T1 = threading.Thread(target=send)
T2 = threading.Thread(target=receive)
#starting threads 
T1.start()
T2.start()
