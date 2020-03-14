#Problem Statement: Swapping of raster bands


#step 1: We will load this raster and swap the order of the first and second bands.
#Then, we will add it to the map. To do this, we need to perform the following steps:
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/FalseColor.tif"
layer=QgsRasterLayer(filepath,"FalseColor","gdal")

#step 2: ow, we must access the layer renderer in order to manipulate the order of the
#bands displayed. Note that this change does not affect the underlying data:
ren=layer.renderer()

#step 3: Next, we will set the red band to band 2:
ren.setRedBand(2)

#step 4:Now, we will set the green band to band 1:
ren.setGreenBand(1)

#step 5: add the altererd raster layer to the map
QgsProject.instance().addMapLayers([layer])
