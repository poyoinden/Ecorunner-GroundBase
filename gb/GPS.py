""" Class for the gps object """
class GPS(object):
	def __init__(self, longtitude, lattitude, speed, timestamp):
		self.longtitude = longtitude
		self.lattitude = lattitude
		self.speed = speed
		self.timestamp = timestamp
         
	def getLongtitude(self):
		return self.longtitude

	def getLattitude(self):
		return self.lattitude

	def getSpeed(self):
		return self.speed

	def getTimestamp(self):
		return self.timestamp

	def toString(self):
		return "GPS: Longtitude: " + str(self.longtitude) + ", Lattitude: " + str(self.lattitude) + ", Speed: " + str(self.speed) +", Timestamp: " + str(self.timestamp)
