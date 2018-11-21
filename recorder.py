import time

morning = {'hour': 10, 'minutes': 10, 'day': 6}
evening = {'hour': 17, 'minutes': 10, 'day': 6}
recLength = 70 # in minutes

def itIsTime(serviceTime):
	currTime = time.gmtime()
	if (currTime.tm_wday == morning['day'] and 
		currTime.tm_hour == serviceTime['hour'] and
		currTime.tm_min >= serviceTime['minutes']):
		return True
	else:
		return False

#def record(length):
## use arecord
	
while(True):
	if (itIsTime(morning) or itIsTime(evening)):
		pass
		#record(recLength)
	time.sleep(600) #sleep until morning/evening service

