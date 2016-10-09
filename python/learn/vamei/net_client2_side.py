#   --coding:utf-8  --


import  socket
HOST = "127.0.0.1"
PORT = 8001

request = "Can you hear me? this is another client"

s = socket.socket()
s.connect((HOST,PORT))

s.sendall(request)

reply = s.recv(1024)
print("reply is:",reply)

s.close()
