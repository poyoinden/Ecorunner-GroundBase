from __future__ import division
import math

def rpmToKMHDisplay(rpm):
	if(rpm == -1):
		return 0

	else:
		wheelCirc = 0.235 * 2 * math.pi
		rps = int(rpm) / 60
		speed = rps * wheelCirc * 3.6
		speedToWrite = int(round(speed))%100
		return speedToWrite
