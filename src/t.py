import time

def year():
	return int(time.strftime("%Y"))
def month():
	return int(time.strftime("%m"))
def day():
	return int(time.strftime("%d"))
def weekday():
	return int(time.strftime("%w"))
def hour():
	return int(time.strftime("%H"))
def minute():
	return int(time.strftime("%M"))
def second():
	return int(time.strftime("%S"))