import MySQLdb
import datetime
import os
import os.path

def writeDBToFile():

	# Open database connection
	db = MySQLdb.connect("localhost","root","reverse","mydata" )
	cursor = db.cursor()

	# Set the name of the output file to a timestamp
	date = datetime.date.today().strftime('%d-%m-%y,')
	time = datetime.datetime.now().strftime('%H:%M:%S')


	save_path = '/home/eco-runner/Gerda2/gb/logs'
	name = date + time + ".txt"

	completeName = os.path.join(save_path, name)

	output = open(completeName, "w")

	# Check the throttle data in the database
	sql = "SELECT * FROM Throttle"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	except:
	   print "Error: unable to fetch data"


	# Check the strategy commands in the database
	sql = "SELECT * FROM Rpm1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	except:
	   print "Error: unable to fetch data"

	# Check the current1 data in the database
	sql = "SELECT * FROM Current1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	except:
	   print "Error: unable to fetch data"

	# Check the current2 data in the database
	sql = "SELECT * FROM Current2"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	except:
	   print "Error: unable to fetch data"

	# Check the voltage1 data in the database
	sql = "SELECT * FROM Voltage1"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)

	except:
	   print "Error: unable to fetch data"


	# Check the voltage2 data in the database
	sql = "SELECT * FROM Voltage2"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     s_type = row[1]
	     data = row[2]
	     timestamp = row[3]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s" % \
		    (s_id, s_type, data, timestamp)
	   
	except:
	   print "Error: unable to fetch data"


	# Check the GPS data in the database
	sql = "SELECT * FROM GPS"

	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Fetch all the rows in a list of lists.
	   results = cursor.fetchall()
	   for row in results:
	     s_id = row[0]
	     longtitude = row[1]
	     lattitude = row[2]
	     speed = row[3]
	     timestamp = row[4]
	     # Now print fetched result
	     print>>output, "%s, %s, %s, %s, %s" % \
		    (s_id, longtitude, lattitude, speed, timestamp)

	except:
	   print "Error: unable to fetch data"

	# disconnect from server
	print "--- Database written to file: " + name + " ---"
	db.close()
