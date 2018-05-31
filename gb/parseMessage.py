from SensorData import SensorData
from GPS import GPS
import re

""" Method for parsing incoming strings called messages """
def parseMessage(inputString):
	# Split the string in parts into a list
	splitUp = re.split(',', inputString)
	length = len(splitUp)

	# Create a sensor data object from the message 
	if splitUp[0] == 'se' and length == 5:
		try:
			se = SensorData(splitUp[1], splitUp[2], splitUp[3], splitUp[4])
			return se			
		
		except IndexError:
			print "Invalid strategy instruction format, instruction not created" 

	# Create a gps object from the message 
	elif splitUp[0] == 'gp' and length == 5:
		try:
			gp = GPS(splitUp[1], splitUp[2], splitUp[3], splitUp[4])
			return gp			
		
		except IndexError:
			print "Invalid strategy instruction format, instruction not created" 

	else:
		print('Invalid message input')
