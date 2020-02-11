import processing
params = {'INPUT':"/home/abhishek/Desktop/M.Sc-GIS/data/union/building.shp",'OVERLAY':"/home/abhishek/Desktop/M.Sc-GIS/data/union/walkway.shp",'OUTPUT':"/home/abhishek/Desktop/M.Sc-GIS/union.shp"}
processing.run('qgis:union',params)