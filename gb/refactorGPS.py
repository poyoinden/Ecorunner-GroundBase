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
#	print toDecimal('00422.530132', '5159.981901')
#	print toDecimal('00202.234470', '4906.195493')
#	print toDecimal('00202.249846', '4906.178389')
#	print toDecimal('00202.250278', '4906.181853')
#	print toDecimal('00202.250330', '4906.181930')
#	print toDecimal('00422.573848', '5159.972468')
#	print toDecimal('00422.602826', '5159.981004')
#	print toDecimal('00422.569904', '5159.976496')
#	print toDecimal('00422.577231', '5159.979423')
#	print toDecimal('00422.587480', '5159.982014')
#	print toDecimal('00422.597289', '5159.983450')
#	print toDecimal('00422.602115', '5159.981409')
#	print toDecimal('00422.605359', '5159.979105')
#	print toDecimal('00422.604023', '5159.975464')
#	print toDecimal('00422.602313', '5159.973968')
#	print toDecimal('00422.599168', '5159.973880')
#	print toDecimal('00422.579619', '5159.971361')
#	print toDecimal('00422.573848', '5159.972467')
#	print toDecimal('00422.582082', '5159.969553')

	print toDecimal('00530.841581', '5227.418689')




#templates:
#type-safe, expressive, and can increase runtime performance by both shifting computation to compile-time and enabling optimizations that can't be applied to equivalent runtime code.
#
#
#

