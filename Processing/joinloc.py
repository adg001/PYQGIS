#Problem Statement: Perform table join by location of 2 shapefile

#Step 1: Load the shapefile
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/natural_earth_vector/110m_cultural/ne_110m_populated_places.shp"
shp=QgsVectorLayer(filepath,"Pop","ogr")
QgsProject.instance().addMapLayer(shp)

filepath="/home/abhishek/Desktop/M.Sc-GIS/data/natural_earth_vector/10m_cultural/ne_10m_admin_0_countries.shp"
shp1=QgsVectorLayer(filepath,"countries","ogr")
QgsProject.instance().addMapLayer(shp1)

outpath="/home/abhishek/Desktop/joinloc.shp"

params={'INPUT':shp,'JOIN':shp1,'PREDICATE':[5],'JOIN_FIELDS':['SOVEREIGNT'],
'METHOD':0,'DISCARD_NONMATCHING':False,'OUTPUT':outpath}
   
processing.run("qgis:joinattributesbylocation",params)
