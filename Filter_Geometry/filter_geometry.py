from qgis.core import QgsFeature
lyrPts = QgsVectorLayer("/home/abhishek/MSc.GIS/MSCities_Geo_Pts/MSCities_Geo_Pts.shp","MSCities_Geo_Pts", "ogr")
lyrPoly = QgsVectorLayer("/home/abhishek/MSc.GIS/GIS_CensusTract/GIS_CensusTract_poly.shp","GIS_CensusTract_poly", "ogr")
QgsProject.instance().addMapLayers([lyrPoly,lyrPts])
ftsPoly = lyrPoly.getFeatures()
for feat in ftsPoly:
    geomPoly = feat.geometry()
    bbox = geomPoly.boundingBox()
    req = QgsFeatureRequest()
    filterRect = req.setFilterRect(bbox)
    featsPnt = lyrPts.getFeatures(filterRect)
    for featPnt in featsPnt:
        if featPnt.geometry().within(geomPoly):
            print(featPnt.id())
            lyrPts.select(featPnt.id())

iface.setActiveLayer(lyrPoly)
iface.zoomToActiveLayer() 
