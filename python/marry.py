#  -- coding:utf-8 --

import time


YEAR1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
YEAR2 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def runnian(year):
	if year % 400 == 0:
#		print("%d��������"%year)
		return 29
	elif year % 4 == 0 and year % 100 != 0:
#		print("%d��������"%year)
		return 29
	else:
		return 28


def get_time():
	str = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	print ("Now time %s" % str)
	list = str.split("-")
	return list

def count_days(now_time):
	count = 0 
	temp = 0
	days = 0
	marry_time = [2015,10,18]
	int_marry_time = int("".join(str(e) for e in marry_time))
	int_now_time = int("".join(str(e) for e in now_time))
#	print int_marry_time
#	print int_now_time
	if int_now_time - int_marry_time < 0:
		print("Not married")
	elif int_now_time <= 20151231 :
		if int(now_time[1]) == 10:
			days = int(now_time[2]) - int(marry_time[2]) + 1
#			print("10")
		elif int(now_time[1]) == 11:
			days = 31 - int(marry_time[2]) + 1 + int(now_time[2])
#			print("11")
		else:
			days = 31 - int(marry_time[2]) + 1 + int(now_time[2]) + 30
#			print("12")
	else:
		for y in range(2016,int(now_time[0])):
#			print ("year %s"% y)
			if runnian(y) == 29:
				count += 1
#				print count
			else:
				count += 0
#				print count
		days = (len(range(2016,int(now_time[0]))) - count) * 365 + count * 366 + 75
#		print len(range(2016,int(now_time[0])))
#		print days
		if runnian(int(now_time[0])) == 28:
#			print("ping")
#			month_list = YEAR1.keys()
			day_list = YEAR1.values()
			for month in range(0,int(now_time[1])-1):
				temp += day_list[month]
#				 print temp
			days = days + int(temp) + int(now_time[2])
		else:
#			print("run")
#			month_list = YEAR2.keys()
			day_list = YEAR2.values()
#			print day_list
			for month in range(0,int(now_time[1])-1):
#				 print month
				temp += day_list[month]
#				 print temp
			days = days + int(temp) + int(now_time[2])
	return days
		
		
	
	
	

print("We married 2015-10-18")
#print(get_time())
#time = get_time()
day = count_days(get_time())
if day == 0:
	print ("We are not married yet")
else:
	print("We have married %s days" % day)
		
#input = raw_input("������һ�����:")
#result = runnian(int(input))
#print(result)