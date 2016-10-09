#      --coding:utf-8 --


import socket

print("create socket....")
s = socket.socket()

print("look up port number...")
port = socket.getservbyname("http","tcp")

print("connet to the server...")
s.connect(("valfs.amd.com",port))

print port
print("Done")

print("connect from",s.getsockname())
print("connect to ",s.getpeername())