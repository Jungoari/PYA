#-*- coding:utf-8 -*-
import os
import datetime
import alarm


__commands__ = ['create', 'delete', 'edit', 'list', 'sleepmode'] #커맨드 모음
__alarms__ = [] #전체 알람 저장소




def main_shell():
	while True:
		in_ = input("pyalarm>")

		

a = alarm.alarm('alarmname',[1,2,3,4,5,6,0],[18,42])
a.startalarm()


			
#main_shell()
