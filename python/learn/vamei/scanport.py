# -- coding:utf-8 --

import socket





for port in range(1,1025):
	try:
		s = socket.socket()
		host = ("10.237.80.75",port)
		s.connect(host)
		print host
		s.close()
	except:
		pass
#		print (host[0] + ":" + str(host[1]) + " is not accessable")
		
		
