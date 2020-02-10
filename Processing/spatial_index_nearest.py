filepath="/home/abhishek/MSc.GIS/NYC_MUSEUMS_GEO/NYC_MUSEUMS_GEO.shp"
iface.addVectorLayer(filepath,"Museums","ogr")
layer=iface.activeLayer()
index = QgsSpatialIndex(layer.getFeatures())
nearest = index.nearestNeighbor(QgsPointXY(25.4, 12.7), 5)
print(nearest)
intersect = index.intersects(QgsRectangle(22.5, 15.3, 23.1, 17.2))
print(intersect)
