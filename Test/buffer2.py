#As per old style code

filepath="/home/abhishek/Desktop/M.Sc-GIS/data/NYC_MUSEUMS_GEO/NYC_MUSEUMS_GEO.shp"
iface.addVectorLayer(filepath,"powerline","ogr")
layer=iface.activeLayer()
feats = [ feat for feat in layer.getFeatures() ]

epsg = layer.crs().postgisSrid()

uri = "Polygon?crs=epsg:" + str(epsg) + "&field=id:integer""&index=yes"

mem_layer = QgsVectorLayer(uri,'square_buffer','memory')

prov = mem_layer.dataProvider()

for i, feat in enumerate(feats):
    new_feat = QgsFeature()
    new_feat.setAttributes([i])
    tmp_feat = feat.geometry().buffer(0.2, 8).boundingBox().asWktPolygon()
    new_feat.setGeometry(QgsGeometry.fromWkt(tmp_feat))
    prov.addFeatures([new_feat])

QgsProject.instance().addMapLayer(mem_layer)
