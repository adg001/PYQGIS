from PyQt5.QtGui import *
filepath="/home/abhishek/Desktop/PGDGIS_MScGIS/Mississippi/mississippi.shp"
iface.addVectorLayer(filepath,"layer","ogr")
layer=iface.activeLayer()
single_symbols=layer.renderer()
symbol=single_symbols.symbol()
#Set fill colour
symbol.setColor(QColor.fromRgb(255,128,0))
#Set fill style
symbol.symbolLayer(0).setBrushStyle(Qt.BrushStyle(Qt.FDiagPattern))
#Set stroke colour
symbol.symbolLayer(0).setStrokeColor(QColor(194,128,0))
#Refresh
layer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer.id())
