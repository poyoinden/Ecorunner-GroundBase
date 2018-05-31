import MySQLdb
import time
import sys
import math

while(True):
	try:
		# Connect to the database
		db = MySQLdb.connect("localhost","root","reverse","mydata" )
		cursor = db.cursor()
		result = ""

		"""
		# Print the current last value for power 1 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Power1 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Power 1: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Power 1: " + "x" + ", "


		# Print the current last value for power 2 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Power2 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Power 2: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Power 2: " + "x" + ", "


		# Print the current last value for power 3 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Power3 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Power 3: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Power 3: " + "x" + ", "

		"""

		# Print the current last value for rpm 1 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Rpm1 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Rpm: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Rpm: " + "x" + ", "

		"""


		# Print the current last value for rpm 2 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Rpm2 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Rpm 2: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Rpm 2: " + "x" + ", "


		# Print the current last value for rpm 3 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Rpm3 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Rpm 3: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Rpm 3: " + "x" + ", "


		# Print the current last value for voltage 1 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Voltage1 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Voltage 1: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Voltage 1: " + "x" + ", "


		# Print the current last value for voltage 2 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Voltage2 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Voltage 2: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Voltage 2: " + "x" + ", "


		# Print the current last value for current 1 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Current1 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Current 1: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Current 1: " + "x" + ", "


		# Print the current last value for current 2 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Current2 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Current 2: " + str(lastRow[0][2]) + ", "


		except IndexError:
			result += "Current 2: " + "x" + ", "

		"""

		# Print the current last value for rpm 1 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM Rpm1 ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			kh = ms*3.6
			rpm = float(lastRow[0][2])
			ms = rpm*0.475*math.pi/60
			result += "Speed (RPM): " + str(kh) + ", "


		except IndexError:
			result += "Speed (RPM): " + "x" + ", "


		# Print the current last value for rpm 1 and if the table is empty print "x"
		try:
			cursor.execute("SELECT * FROM GPS ORDER BY id DESC LIMIT 1;")
			lastRow = cursor.fetchall()
			result += "Speed (GPS): " + str(lastRow[0][3])


		except IndexError:
			result += "Speed (GPS): " + "x" 


	
		result += "\n------------------------------------------------------------"
		print result

		time.sleep(.1)
		db.close()
	

	except KeyboardInterrupt:
		sys.exit()
