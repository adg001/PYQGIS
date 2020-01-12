uri = "/home/abhishek/MSc.GIS/ne_10m_admin_0_countries_2/ne_10m_admin_0_countries.shp"
vlayer = iface.addVectorLayer(uri, "countries", "ogr")
#Below statement opens attribute layer table
#iface.showAttributeTable(vlayer)
#line no(6-7) displays all the fields available in the shapefile
for field in vlayer.fields():
    print(field.name())
#line no(9-10) displays the data from the "admin" field
for feature in vlayer.getFeatures():
    print(feature["ADMIN"])