layer = QgsVectorLayer("/home/abhishek/Downloads/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp","countries", "ogr")
QgsProject.instance().addMapLayers([layer])
query = '"name" LIKE \'J%\''
features = layer.getFeatures(QgsFeatureRequest().setFilterExpression(query))
for f in features:
     geom = f.geometry()
     name = f.attribute('NAME')
     print(name)
     print('Area: ', geom.area())
     print('Perimeter: ', geom.length())
    