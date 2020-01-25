from PyQt5.QtGui import *
filepath="/home/abhishek/Desktop/PGDGIS_MScGIS/MS_UrbanAnC10/MS_UrbanAnC10.shp"
iface.addVectorLayer(filepath,"layer","ogr")
layer=iface.activeLayer()
#Now we build some nested python tuples defining the symbol graduation. Each item in the tuple contains a range label, range start value, range end value, and a color name:
population = (
("Village", 0.0, 3159.0, "cyan"),
("Small town", 3160.0, 4388.0, "blue"),
("Town", 43889.0, 6105.0, "green"),
("City", 6106.0, 10481.0, "yellow"),
("Large City", 10482.0, 27165, "orange"),
("Metropolis", 27165.0, 1060061.0, "red"))
#Then we establish a python list to hold our QGIS renderer objects:
ranges = []
#Next we loop through our range list, build the QGIS symbols, and add them to the renderer list:
for label, lower, upper, color in population:
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    sym.setColor(QColor(color))
    rng = QgsRendererRange(lower, upper, sym, label)
    ranges.append(rng)
#Now reference the field name containing the population values in the shapefile attributes:
field = "POP"
#Then we create the renderer:
renderer = QgsGraduatedSymbolRenderer(field, ranges)
#We assign the renderer to the layer:
layer.setRenderer(renderer)
#And finally, we add the map to the layer:
QgsProject.instance().addMapLayers([layer])