import socket
import threading
import os
import sys
#no listen 
#ideally gonna need two threads 
#make sure to 


serverIP ="127.0.0.1"
serverPort = 4321
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))


print("Hello and welcome to a simple UDP chat box\n"  )

name = input("Enter Your name: ")
print("Waiting........")



sname = "{}".format(name)
serverSocket.sendto(sname.encode(),("127.0.0.1",1234))


inName = serverSocket.recvfrom(2048)
print("\nStarting Chat with: "  + inName[0].decode()) 


if(name == "QUIT"):
    os._exit(1)
print("\tType *QUIT* to exit the program. \n\n")

print("===================================================\n")



def send():
    while True:
        
        outMess =  input() 
    
        if (outMess == "QUIT"):
            os._exit(1)
        
        sendMess = "{}>> {}".format(name,outMess)
        serverSocket.sendto(sendMess.encode(),("127.0.0.1",1234) ) #client IP and port

def receive():
    while True: 
        inMess = serverSocket.recvfrom(2048)     
        print("\t\t\t" +  inMess[0].decode())

        
#creating threads 
T1 = threading.Thread(target=send)
T2 = threading.Thread(target=receive)
#starting threads 
T1.start()
T2.start()

