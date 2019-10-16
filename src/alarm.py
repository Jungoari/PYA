#-*- coding:utf-8 -*-
import main, threading, time, t

class alarm:

	def nmin(self):
		return t.hour() * 60 + t.minute()

	def dmin(self):
		return self.ringtime[0] * 60 + self.ringtime[1]

	def waitloop(self):
		print('[alarm] thread started')
		print('[alarm] nmin=%d, dmin=%d'%(self.nmin(),self.dmin()))
		while True:

			daychk = False
			for day in self.ringday:
				if day == t.weekday():
					daychk = True


			if daychk and self.nmin()<self.dmin():

				if self.nmin()<self.dmin()-2:
					#normal waiting procedure
					print('[alarm] waiting for %d mins'%(self.dmin()-2 - self.nmin()))
					time.sleep(60 * (self.dmin()-2 - self.nmin()))

				while self.nmin() != self.dmin():
					print('[alarm] not yet')
					time.sleep(1)
				#alarm ring
				#TODO: alarmring.py
				print('ALARMRING')

			else:
				print('[alarm] time passed, waiting for %d mins'%((24 * 60 - self.nmin())))
				time.sleep(24 * 60 * 60 - self.nmin() * 60)
				continue



	def __init__(self, name, days, time):
		self.alarmname = name
		self.ringday = days
		self.ringtime = time

		self.alarmthread = threading.Thread(target=self.waitloop)

	def startalarm(self):
		self.alarmthread.start()













