#   --coding:utf-8 --

"""scan 80 port and get server IP"""

import socket

s = socket.socket()

ip = [10,237,0,0]
port = 80

while ip != [10,237,80,76]:
	for i in range(80,81):
		ip[2] = i
		for j in range(74,77):
			ip[3] = j
			ip_con = str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3])
			print ip_con
			try:
				s.connect((ip_con,port))
				print s.recv(1024)
			except:
				pass
			print ip


s.close()