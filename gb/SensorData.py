class SensorData(object):
	def __init__(self, sensorId, msgType, data, timestamp):
		self.sensorId = sensorId
		self.msgType = msgType
		self.data = data
		self.timestamp = timestamp
         
	def getSensorId(self):
		return self.sensorId

	def getMsgType(self):
		return self.msgType

	def getData(self):
		return self.data

	def getTimestamp(self):
		return self.timestamp

	def toString(self):
		return "SensorId: " + str(self.sensorId) + ", MessageType: " + str(self.msgType) + ", Data: " + str(self.data) + ", timestamp: " + str(self.timestamp)
