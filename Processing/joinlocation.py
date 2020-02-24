import processing
import datetime
t0 = datetime.datetime.now()
print("QGIS Join attributes by location ...")
processing.runAndLoadResults(
   "qgis:joinattributesbylocation", 
   {'INPUT':'E:/Geodata/NaturalEarth/vector_v4/natural_earth_vector/110m_cultural/ne_110m_populated_places.shp',
   'JOIN':'E:/Geodata/NaturalEarth/vector_v4/natural_earth_vector/10m_cultural/ne_10m_admin_0_countries.shp',
   'PREDICATE':[5],'JOIN_FIELDS':['SOVEREIGNT'],
   'METHOD':0,'DISCARD_NONMATCHING':False,'OUTPUT':'memory:'})
