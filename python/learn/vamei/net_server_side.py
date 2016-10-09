#    --coding:utf-8 --



import socket
HOST = ""
PORT = 8001

reply = "Yes"

s = socket.socket()
s.bind((HOST,PORT))
s.listen(10)
while 1:
    con,addr = s.accept()
    request = con.recv(1024)

    print("request is:",request)
    print ("connected by",addr)

    con.sendall(reply)
con.close()

