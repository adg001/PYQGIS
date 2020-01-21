filepath="/home/abhishek/Desktop/M.Sc-GIS/data/natural_earth_vector/10m_cultural/ne_10m_populated_places_simple.shp"
layer=QgsVectorLayer(filepath,"Popolated Places","ogr")
QgsProject.instance().addMapLayers([layer])
layer=iface.activeLayer()
query='"pop_max" > 1000000'
selection=layer.getFeatures(QgsFeatureRequest().setFilterExpression(query))
layer.selectByIds([k.id() for k in selection])