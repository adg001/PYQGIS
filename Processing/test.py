from qgis import core
from PyQt5.QtWidgets import *
from qgis.utils import iface
from qgis.core import QgsProject
import processing

envPath = QFileDialog.getOpenFileName(QFileDialog(), "Environment Layer Select", "/home/abhishek/MSc.GIS/")[0]
env = iface.addVectorLayer(envPath, "", "ogr")
env.setName("Environment")
atbnPath = QFileDialog.getOpenFileName(QFileDialog(), "Environment Layer Select", "/home/abhishek/MSc.GIS/")[0]
atbn = iface.addVectorLayer(atbnPath, "", "ogr")
atbn.setName("Autobahn")
atbn = QgsProject.instance().mapLayersByName("Autobahn")[0] 
param = { 'INPUT' : atbn, 'DISTANCE' : 20, 'SEGMENTS' : 5, 'END_CAP_STYLE' : 0, 'JOIN_STYLE' : 0, 'MITER_LIMIT' : 2, 'DISSOLVE' : False, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:buffer", param)
autobahn20 = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])
autobahn20.setName("Autobahn 20")
