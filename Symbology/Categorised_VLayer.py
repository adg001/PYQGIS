from PyQt5.QtGui import *
filepath="/home/abhishek/Desktop/PGDGIS_MScGIS/landuse_shp/landuse.shp"
iface.addVectorLayer(filepath,"landuse","ogr")
layer=iface.activeLayer()
#Next we’ll create our three land use categories using a python dictionary with a field value as the key, color name, and label:
landuse = {
"0":("yellow", "Developed"),
"1":("darkcyan", "Water"),
"2":("green", "Land")}
#Now we can build our categorized renderer items:
categories = []
for terrain, (color, label) in landuse.items():
    sym = QgsSymbol.defaultSymbol(layer.geometryType())
    sym.setColor(QColor(color))
    category = QgsRendererCategory(terrain, sym, label)
    categories.append(category)
#We name the field containing the land use value:
field = "DN"
#Next we build the renderer:
renderer = QgsCategorizedSymbolRenderer(field, categories)
#We add the renderer to the layer:
layer.setRenderer(renderer)
#And finally we add the categorized layer to the map:
QgsProject.instance().addMapLayers([layer])


