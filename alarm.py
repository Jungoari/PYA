import main
import t
import time
import threading

class alarm:

	ringtime = [] # 0,0
	ringday = [] #0,1,2,3,4,5,6
	alarmname = ''

	nmin = t.hour() * 60 + t.second()
	dmin = ringtime[0] * 60 + ringtime[1]

	def waitloop():

		while True:
			for day in ringday:
				if day == time.weekdays():

					if nmin >= dmin: #already passed, waiting for next day
						time.sleep(1000 * 60 * (24 * 60 * 60 * 1000 - nmin))
					else: #normal waiting procedure
						time.sleep(1000 * 60 * (dmin - nmin))

					#alarm ring
					#TODO: alarmring.py
					print('ALARMRING')

	alarmthread = threading.Thread(target=waitloop)


	def __init__(self, name, days, time):
		alarmname = name
		ringday = days
		ringtime = time

	def startalarm():
		alarmthread.start()

#######################################












