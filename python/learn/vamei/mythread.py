#	-- coding:utf-8 --

import threading
import time
import socket



HOST = "127.0.0.1"
PORT = 80

def connport():
	s = socket.socket()
	try:
		s.connect((HOST,PORT))
		print s.recv(1024)
	except:
		print("Connect Failed!")


class MyThread(threading.Thread):
	def __init__(self,id):
		threading.Thread.__init__(self)
		self.id = id

	def run(self):
		print("Time:%s Now Start a new thread...%s" % (time.ctime(),threading.current_thread))
#		connport()
		time.sleep(10)
		print("Time:%s Thread Name:%s" % (time.ctime(),threading.current_thread))

thread = []

for i in range(100000):
	thread.append(MyThread(i))

print thread

for t in thread:
#	t.setDaemon(1)
	t.start()

t.join()

print("Over %s" % time.ctime())