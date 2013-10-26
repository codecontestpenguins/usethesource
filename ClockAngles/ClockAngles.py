#!/bin/env python2.7

filename = "SampleInput.txt"

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

	def getHourMinuteAngle(self):
		angle_diff = abs(self.getHourAngle() - self.getMinuteAngle())
		if (angle_diff > 180):
			angle_diff = 360 - angle_diff
		return angle_diff

	def getHourSecondAngle(self):
		angle_diff = abs(self.getHourAngle() - self.getSecondAngle())
		if (angle_diff > 180):
			angle_diff = 360 - angle_diff
		return angle_diff

	def getMinuteSecondAngle(self):
		angle_diff = abs(self.getMinuteAngle() - self.getSecondAngle())
		if (angle_diff > 180):
			angle_diff = 360 - angle_diff
		return angle_diff

	def printAngleDifferences(self):
		# format: hour-minute, hour-second, minute-second
		print "%.2f, %.2f, %.2f" % (round(self.getHourMinuteAngle(),2), round(self.getHourSecondAngle(),2), round(self.getMinuteSecondAngle(),2))

def main():
	f = open(filename, 'r')

	# Read in number of inputs
	n = int(f.readline())

	# Read in each line (corresponds to one time HH:MM:SS and it put it in times
	for i in range(n):
		line = f.readline()
		time = line.rstrip('\n\r')

		times.append(Time(time));

	f.close()

	# Print number of times
	print n

	# Print each set of angle differences
	for time in times:
		time.printAngleDifferences()

main()
