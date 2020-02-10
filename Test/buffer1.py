#As per new processing algorithms.

outFn="/home/abhishek/Desktop/M.Sc-GIS/buffer1.shp"
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/shapefiles_toulouse/gis_osm_powerlines_07_1.shp"
iface.addVectorLayer(filepath,"powerline","ogr")
layer=iface.activeLayer()
bufferDist=50

fields=layer.fields()
feats=layer.getFeatures()

writer=QgsVectorFileWriter(outFn,'UTF-8',fields,QgsWkbTypes.Polygon,layer.sourceCrs(),'ESRI Shapefile')
for feat in feats:
    geom=feat.geometry()
    buff=geom.buffer(bufferDist,5,QgsGeometry.CapFlat,QgsGeometry.JoinStyleMiter,2.0)
    feat.setGeometry(buff)
    writer.addFeature(feat)
    
iface.addVectorLayer(outFn,'',"org")
del(writer)
