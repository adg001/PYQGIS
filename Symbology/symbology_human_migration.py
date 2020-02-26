filepath="/home/abhishek/Desktop/M.Sc-GIS/data/countries/countries.shp"
filepath2="/home/abhishek/Desktop/M.Sc-GIS/data/human_migration_routes/human_migration_routes.shp"
countries=QgsVectorLayer(filepath,"countries","ogr")
routes=QgsVectorLayer(filepath2,"routes","ogr")

symlyr=QgsArrowSymbolLayer()
symlyr.setIsCurved(True)
symlyr.setIsRepeated(False)

symbol1=routes.renderer()
s=symbol1.symbol()
s.changeSymbolLayer(0,symlyr)

QgsProject.instance().addMapLayers([routes,countries])
