#!/bin/env python2.7
times = []

class Time:
	def __init__(self, time_str):
		times_list = time_str.split(':')
		self.h = int(times_list[0]) # hour
		self.m = int(times_list[1]) # minutes
		self.s = int(times_list[2]) # seconds
		self.s_tot = self.h * 3600 + self.m * 60 + self.s # time in seconds

	def __str__(self):
		return str(self.h) + ":" + str(self.m) + ":" + str(self.s)

	def getHourAngle(self):
		# angle = 360 / (12 * 60 * 60) = 1/120 deg/s
		angle = self.s_tot/120.0
		return angle % 360

	def getMinuteAngle(self):
		# angle = 360 / (60 * 60) = 1/10 deg/s
		angle = self.s_tot/10.0
		return angle % 360

	def getSecondAngle(self):
		# angle = 360 / 60  deg/s = 6 deg/s
		angle = self.s_tot*6.0
		return angle % 360

	def printAngles(self):
		print "Angles: h = %.2f, m = %.2f, s = %.2f" % (self.getHourAngle(), self.getMinuteAngle(), self.getSecondAngle())


def main():
	f = open('SampleInput.txt', 'r')

	# Read in number of inputs
	n = int(f.readline())

	# Read in each line (corresponds to one time HH:MM:SS and it put it in times
	for i in range(n):
		line = f.readline()
		time = line.rstrip('\n\r')

		times.append(Time(time));

	f.close()

	# TESTING
	for time in times:
		print str(time) + " = hour " + str(time.h) + " minute " + str(time.m) + " second " + str(time.s)
		time.printAngles()



main()
