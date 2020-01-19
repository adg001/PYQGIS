layer = QgsVectorLayer("/home/abhishek/Downloads/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp","countries", "ogr")
QgsProject.instance().addMapLayers([layer])
d = QgsDistanceArea()
d.setEllipsoid('WGS84')
query = '"name" LIKE \'I%\''
features = layer.getFeatures(QgsFeatureRequest().setFilterExpression(query))
for f in features:
     geom = f.geometry()
     name = f.attribute('NAME')
     print(name)
     print("Perimeter (m):", d.measurePerimeter(geom))
     print("Area (m2):", d.measureArea(geom))
     print("Area (km2):", d.convertAreaMeasurement(d.measureArea(geom), QgsUnitTypes.AreaSquareKilometers))