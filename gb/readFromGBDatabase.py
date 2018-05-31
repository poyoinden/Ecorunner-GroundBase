import MySQLdb
import time

""" Method for retreiving latest values to the MySQL database. 
INPUT: None.
OUTPUT: Dictionary with entries for "rpm", "throttle", "current", "voltage", "GPS".
"""
def readFromGBDatabase():
	db = MySQLdb.connect("localhost","root","reverse","mydata")
	cursor = db.cursor()

	results_dict = {"rpm":9.51,"throttle":0,"current":0,"voltage":0,"GPS":(-0.009384, 51.540589)}
	id_results = ["rpm", "throttle", "current", "voltage", "GPS"]

	# Retreive all latest data points from SQL db
	results_all = []
	list = ["Rpm1", "Throttle", "Current1", "Voltage1", "GPS"] 	# Excluding voltage2 and current2.

	try:
		for i in range(len(list)):
			cursor.execute("SELECT * FROM " + list[i] + " ORDER BY id DESC LIMIT 1;")
			results = cursor.fetchall()[0]

			# Catch mistake in previous database configuration.
			if len(results[1]) < 10:
				results_dict[id_results[i]] = results[2]
			else:
				results_dict[id_results[i]] = (results[1], results[2])

			results_all.append(results)

	except:
		print "An error occurred while retreiving information from the databse."

	db.close()
	return results_dict


if __name__ == "__main__":
	tic = time.time()
	for i in range(1000):
		latest_values = readFromGBDatabase()

	print latest_values
	print (time.time() - tic)