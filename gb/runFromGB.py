from SensorData import SensorData
from GPS import GPS
from parseMessage import parseMessage
from readMessage import nextMessage
from addToGBDatabase import addToDatabase
from cleardb import cleardb
import sys
import re
import time
import boto.sqs
from boto.sqs.message import Message
import MySQLdb
from writeDBToFile import writeDBToFile
from readFromGBDatabase import readFromGBDatabase

print "Starting runFromGB.py"

# Connect to the queue server
conn = boto.sqs.connect_to_region("eu-west-2", aws_access_key_id = "AKIAJAR3NWUEFXUP2DUA", aws_secret_access_key = "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")
receiveQueue = conn.get_queue('Eco2GB')

# Clear the database before running
db = MySQLdb.connect("localhost", "root", "reverse", "mydata")
cursor = db.cursor()
#cleardb()

print "Starting runFromGB.py main loop."
while(True):	
	try:
		message = nextMessage(receiveQueue)
		addToDatabase(message)
		print readFromGBDatabase()
		time.sleep(.005)
	
	except KeyboardInterrupt:
		print "Wrong."
		writeDBToFile()
		sys.exit()

