#Server side:
Import Socket, Threading

 1. Main function
- Inside the main function, you have to
(1) Create an UDP socket
(2) Bind with your IP and port
(3) Create a thread array 
threads = []
(4) Create the first thread, which could receive message 

from client 
t1 = threading.Threads(target=receive)
(5) Append this thread to the thread array 
threads.append(t1)
(6) Create the second thread, which could send message to the client 
t2 = threading.Threads(target=send)
(7) Append it to the thread array 
threads.append(t2)
(8) Protect the parent thread by setting Daemon to true for each thread
(9) Start each thread
for t in threads: 
t.setDaemon(True) 
t.start()
(10) After that, join each thread so that the parent thread will wait for each child 
threads finished.
for t in threads: 
t.join()
(11) Close the serversocket.