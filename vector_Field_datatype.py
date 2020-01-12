location=r"/home/abhishek/MSc.GIS/curso-qgis-python-master/datos/ne_110m_admin_0_countries.shp"
layer=iface.addVectorLayer(location,"","ogr")
for field in layer.fields():
    print(field.name(), field.typeName())