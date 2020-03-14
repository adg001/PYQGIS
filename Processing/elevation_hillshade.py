# Problem Statement: Creating Elevation Hillshade

#step 1: load the layer
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/dem/dem.asc"
layer=QgsRasterLayer(filepath,"hillshade","gdal")
outpath="/home/abhishek/Desktop/hillshade.tif"
params={'INPUT':filepath,'BAND':1,'Z_FACTOR':1.0,'SCALE':1.0,'AZIMUTH':315.0,'ALTITUDE':45.0,'COMPUTE_EDGES':False,'ZEVENBERGEN':False,'OUTPUT':outpath}
processing.run("gdal:hillshade",params)

filepath1="/home/abhishek/Desktop/hillshade.tif"
layer1=QgsRasterLayer(filepath1,"output","gdal")
QgsProject.instance().addMapLayers([layer1])