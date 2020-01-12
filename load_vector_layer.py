layer = QgsVectorLayer("/home/abhishek/MSc.GIS/geospatial-python-master/data/NYC_MUSEUMS_LAMBERTNYC_MUSEUMS_GEO.shp",
"New York City Museums", "ogr")
QgsProject.instance().addMapLayers([layer])
