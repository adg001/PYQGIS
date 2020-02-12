for x in QgsApplication.processingRegistry().algorithms():
    if "centroids" in x.id():
        print(x.id(),"->",x.displayName())
        
import processing
params={'INPUT':"/home/abhishek/MSc.GIS/ne_10m_admin_0_countries_2/ne_10m_admin_0_countries.shp",'ALL_PARTS':False,'OUTPUT':"/home/abhishek/output.shp"}
processing.run("native:centroids",params)
