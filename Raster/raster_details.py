#Problem Statement: load the raster file ad check its properties.

#step 1: get the filepath and load the file
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/SatImage/SatImage.tif"
layer=iface.addRasterLayer(filepath,"satellite image","gdal")

#step 2: get all the functionalities provided by raster file
print(dir(layer))

#step 3: width and height
print("width=",layer.width()," "," height=",layer.height())
