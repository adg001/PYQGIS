from qgis.core import QgsProject
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/tl_2013_06_tract/tl_2013_06_tract.shp"
shp = QgsVectorLayer(filepath, 'tracts_pop', "ogr")
QgsProject.instance().addMapLayer(shp)
iface.addVectorLayer(filepath,"tract","ogr")
uri = "file:///home/abhishek/Desktop/M.Sc-GIS/data/ca_tracts_pop.csv?delimiter=,"
csv = QgsVectorLayer(uri, 'ca_tracts_pop', 'delimitedtext')
QgsProject.instance().addMapLayer(csv)
shpField='GEOID'
csvField='GEO.id2'
joinObject =  QgsVectorLayerJoinInfo()
joinObject.joinLayerId = csv.id()
joinObject.joinFieldName = csvField
joinObject.targetFieldName = shpField
joinObject.memoryCache = True
shp.addJoin(joinObject)
shpField='GEOID'
csvField='GEO.id2'
params={'INPUT':shp,'FIELD':shpField,'INPUT_2':csv, 'FIELD_2':csvField, 'output_layer': None}
result = processing.run('qgis:joinattributestable', params)
