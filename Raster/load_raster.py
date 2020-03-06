urlWithParams = 'url=https://sedac.ciesin.columbia.edu:443/geoserver/ows?SERVICE=WMS&layers=ipcc:ipcc-synthetic-vulnerability-climate-2005-2050-2100&format=image/png&crs=EPSG:4326&styles='
raster_layer = QgsRasterLayer(urlWithParams, 'Climate Vulnerability', 'wms')
if not raster_layer.isValid():
  print("Layer failed to load!")
QgsProject.instance().addMapLayer(raster_layer)
