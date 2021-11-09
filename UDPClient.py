import socket 
import threading
import os 

target_host  = '127.0.0.1'
target_port = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send():
    while True:
        outMess = input("Me: ")
        if (outMess == "quit" | outMess == "Quit" | outMess == "QUIT"):
            os._exit(1)

        clientSocket.send(str(outMess).encode())
        print("\n")

def receive():
    while True: 
        inMess = clientSocket.recvfrom(2048)
        print("Them: " + inMess[0].decode())
        

        print("\n")

#creating threads 
T1 = threading.Thread(target=send)
T2 = threading.Thread(target=receive)

#starting threads 
T1.start()
T2.start()







'''clientSocket.sendto(message.encode(),(target_host, target_port))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
'''