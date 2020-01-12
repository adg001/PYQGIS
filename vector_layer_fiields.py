location=r"/home/abhishek/MSc.GIS/curso-qgis-python-master/datos/ne_110m_admin_0_countries.shp"
layer = QgsVectorLayer("location","","ogr")
layer1=iface.addVectorLayer(location,"","ogr")
for field in layer1.fields():
    print(field.name())






