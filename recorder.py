import time

morning = {hour: 10, minutes: 10, day: 6}
evening = {hour: 17, minutes: 10, day: 6}
recLength = 70

while(True):
	if (itIsTime(morning) || itiIsTime(evening):
		record(recLength)
	time.sleep(600)

def itIsTime(serviceTime):
	currTime = time.gmtime()
	if (currTime.tm_wday == morning.day && 
		currTime.tm_hour == serviceTime.hour &&
		currTime.tm_min >= serviceTime.minutes):
		return True
	else:
		return False

def record(length):
	
