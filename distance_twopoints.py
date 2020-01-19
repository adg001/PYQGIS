d = QgsDistanceArea()
d.setEllipsoid('WGS84')

# Let's create two points.
# Santa claus is a workaholic and needs a summer break,
# lets see how far is Tenerife from his home
santa = QgsPointXY(15.631929, 73.827193)
tenerife = QgsPointXY(15.289882, 73.980409)

print("Distance in meters: ", d.measureLine(santa, tenerife))