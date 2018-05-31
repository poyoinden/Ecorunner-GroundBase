""" NOTE: DOES NOT WORK. USE 'toDecimal(lon, lat)' in 'refactorGPS.py' Extremely redundant conversion algorithm for nmea latitute and longtitude values to decimal values """
def toDecimal(value, typ):
	try:	
		if typ == "lat":
			first, last = int(str(list(value)[0] + list(value)[1])), float(''.join(list(value)[2:]))
			return first + (last/60)

		elif typ == "lon":
			first, last = int(str(list(value)[0] + list(value)[1] + list(value)[2])), float(''.join(list(value)[3:]))
			return first + (last/60)

		else:
			pass

	except ValueError:
		print "Incorrect value for conversion entered"

