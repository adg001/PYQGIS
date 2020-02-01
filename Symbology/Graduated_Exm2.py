filepath="/home/abhishek/Desktop/PGDGIS_MScGIS/TestZipCodes/TestZipCodes.shp"
iface.addVectorLayer(filepath,"Patients by Zip Code","ogr")
target_field = "Patient_Da"
layer=iface.activeLayer()
#Creates Symbology for each value in range of values. 
#Values are # of patients per zip code
#Hard codes min value, max value, symbol (color), and label for each range of values.
#Then QgsSymbolRenderer takes field from attribute table and item from 
#myRangeList and applies them to join_layer. Color values are hex codes, 
#in a graduated fashion from light pink to black depending on intensity
def apply_graduated_symbology():
     myRangeList = []
     symbol = QgsSymbol.defaultSymbol(layer.geometryType())     
     symbol.setColor(QColor("#f5c9c9"))                              
     myRange = QgsRendererRange(0, 3, symbol, 'Group 1')                   
     myRangeList.append(myRange)                                     
     
     symbol = QgsSymbol.defaultSymbol(layer.geometryType())
     symbol.setColor(QColor("#000000"))
     myRange = QgsRendererRange(3.1, 6, symbol, 'Group 2')
     myRangeList.append(myRange)
     
     myRenderer = QgsGraduatedSymbolRenderer(target_field, myRangeList)  
     myRenderer.setMode(QgsGraduatedSymbolRenderer.Custom)               
     
     layer.setRenderer(myRenderer)                                  
     print(f"Graduated color scheme applied")
    
apply_graduated_symbology()