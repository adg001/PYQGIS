#Problem Statement: Querying the value of a raster at a specified point

#step 1: load the layer
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/SatImage/SatImage.tif"
layer=QgsRasterLayer(filepath,"Satellite","gdal")
QgsProject.instance().addMapLayers([layer])

#step 2: Next, get the layer's center point from its QgsRectangle extent object, which will
#return a tuple with the x and y values:

c = layer.extent().center()

#step 3: Now, using the layer's data provider, we can query the data value at that point using
#the identify() method:

qry = layer.dataProvider().identify(c,QgsRaster.IdentifyFormatValue)

#step 4: Because a query error won't throw an exception, we must validate the query:
qry.isValid()

#step 5: Finally, we can view the query results, which will return a Python dictionary with each
#band number as the key pointing to the data values in that band:

print(qry.results())
