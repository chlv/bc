#    --coding:utf-8 --

import os,re

# create original device info by devcon.exe
def get_original_device():
	os.system("devcon hwids * > sysinfo.txt")

        


# get device location and name from sysinfo.txt	
def get_location(filename):
	f = open(filename,"rb+")
	device = open("device.txt","a")
#	zz = re.compile(r'^[\S+].*$')
	count = len(f.readlines())
	f.seek(0)
	for line in range(0,count):
#		re = re.compile(r'^[\S+].*$')
		location = re.findall(r'^[\S+].*$',str(f.readline()),re.I)
		if len(location) != 0:
			location = str(location).strip()
			location = str(location).replace("\\\\","\\")
			device.write(location)
#			device.write(str(f.tell()))
			device.write("\n")
			f.seek(1,1)
#			device.write(str(f.tell()))
			device.write(str(f.readline()))	
	device.close()
	f.close()


	

get_original_device()
get_location("sysinfo.txt")
os.system("move /y device.txt %temp% ")
os.system("move /y sysinfo.txt %temp% ")

if os.path.exists("c:\\Drvpack64"):
	os.system("xcopy /y C:\Drvpack64\Autobot\utils\config.txt %temp% ")
	
if os.path.exists("c:\\Drvpack"):
	os.system("xcopy /y C:\Drvpack\Autobot\utils\config.txt %temp% ")