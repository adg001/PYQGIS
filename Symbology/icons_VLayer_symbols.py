from PyQt5.QtGui import *
filepath="/home/abhishek/MSc.GIS/NYC_MUSEUMS_GEO/NYC_MUSEUMS_GEO.shp"
iface.addVectorLayer(filepath,"layer","ogr")
layer=iface.activeLayer()
#Now we’ll use a python dictionary to define the font properties:
fontStyle = {}
fontStyle['color'] = '#000000'
fontStyle['font'] = 'Webdings'
fontStyle['chr'] = 'G'
fontStyle['size'] = '6'
#Now we’ll create a font symbol layer:
symlyr=QgsFontMarkerSymbolLayer.create(fontStyle)
#Then we’ll change out the default symbol layer of the vector layer with our font symbol information:
ss=layer.renderer()
s=ss.symbol().changeSymbolLayer(0,symlyr)
QgsProject.instance().addMapLayers([layer])