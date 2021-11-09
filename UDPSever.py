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


print("\n[*] Starting Chat with server code...%s:%d" % (serverIP,serverPort))
print("The chat is ready.\n\n")

#os.system("tput setaf 2")
name = input("Enter Your name:")
if(name == "QUIT"):
    os._exit(1)
print("Type *QUIT* to exit the program. \n\n")



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
        print("\t\t\t\t" +  inMess[0].decode())
        
#creating threads 
T1 = threading.Thread(target=send)
T2 = threading.Thread(target=receive)
#starting threads 
T1.start()
T2.start()

