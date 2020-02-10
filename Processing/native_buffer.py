def buffer(input, distance, output, before_processing_reproject_to_epsg_number=None):
    params = {'INPUT': input,
              'DISTANCE': distance,
              'END_CAP_STYLE': 0 , # - 0: Round - 1: Flat - 2: Square
              'DISSOLVE': False,
              'OUTPUT': output}
    feedback = qgis.core.QgsProcessingFeedback()
    alg_name = 'native:buffer'
    # print(processing.algorithmHelp(alg_name)) # tool tips
    result = processing.run(alg_name, params, feedback=feedback)
    return  result
    
buffer_result = buffer(input=r'/home/abhishek/MSc.GIS/NYC_MUSEUMS_GEO/NYC_MUSEUMS_GEO.shp', distance=100, output=r'/home/abhishek/Desktop/output.shp')
print(buffer_result)