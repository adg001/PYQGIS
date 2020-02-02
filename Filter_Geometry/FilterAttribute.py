from qgis.utils import iface
lyrPts = QgsVectorLayer("/home/abhishek/MSc.GIS/MSCities_Geo_Pts/MSCities_Geo_Pts.shp","MSCities_Geo_Pts", "ogr")
QgsProject.instance().addMapLayers([lyrPts])
selection = lyrPts.getFeatures(QgsFeatureRequest().setFilterExpression(u'"PLACEFP10" = 81520'))
lyrPts.selectByIds([s.id() for s in selection])
iface.mapCanvas().zoomToSelected()
iface.mapCanvas().refresh()