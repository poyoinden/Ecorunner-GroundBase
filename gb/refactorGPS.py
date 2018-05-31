def toDecimal(lon, lat):
	s = list(lat)
	degstr = s[0] + s[1] + "."
	minstr = s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10] + s[10]
	minstr = float(minstr) / 6
	minstr = str(minstr).replace(".", "")

	latres =  float(degstr + minstr)

	s = list(lon)
	degstr = s[0] + s[1] + s[2] + "."
	minstr = s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10] + s[11]
	minstr = float(minstr) / 6
	minstr = str(minstr).replace(".", "")

	lonres = float(degstr + minstr)

	return latres, lonres

if __name__ == "__main__":
	print toDecimal('00422.530132', '5159.981901')
