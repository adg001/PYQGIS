# Problem Statement: Reprojecting the raster layer

#step 1: load the layer
filepath="/home/abhishek/Desktop/M.Sc-GIS/data/SatImage/SatImage.tif"
layer=QgsRasterLayer(filepath,"Satellite","gdal")
QgsProject.instance().addMapLayers([layer])
outpath="/home/abhishek/out.tif"

#STEP 2: Finally, we run the gdal warp algorithm by inserting the correct parameters,
#including the layer reference, current projection, desired projection, None for changes
#to the resolution, 0 to represent nearest neighbor resampling, None for additional
#parameters, 0 –Byte output raster data type (1 for int16), and an output name
#for the reprojected image:

params={'INPUT':filepath,'SOURCE_CRS':'EPSG:4326','TARGET_CRS':'EPSG:3722','RESAMPLING':None,'NODATA':0,'TARGET_RESOLUTION':None,'OUTPUT':outpath}
processing.run("gdal:warpreproject",params)
