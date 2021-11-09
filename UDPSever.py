import socket
import threading
import os



serverIP ='127.0.0.1'
serverPort = 12000
#no listen 
#ideally gonna need two threads 
#make sure to 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("[*] Starting server...%s:%d" % (serverIP,serverPort) + "\n")
print("The server is ready. ")

def send():
    while True:
        outMess = input("Me: ")
        if (outMess == "quit" | outMess == "Quit" | outMess == "QUIT"):
            os._exit(1)

        serverSocket.send(str(outMess).encode())
        print("\n")

def receive():
    while True: 
        inMess = serverSocket.recvfrom(2048)
        print("Them: " + inMess[0].decode())
        

        print("\n")

#creating threads 
T1 = threading.Thread(target=send)
T2 = threading.Thread(target=receive)

#starting threads 
T1.start()
T2.start()


'''while True:
    #no accept
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    print ("[*] Client Socket Address: %s Send string to the client: %s" % (clientAddress, modifiedMessage)) 
'''