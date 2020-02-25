""" Import data libraries """
from qgis import core
from PyQt5.QtWidgets import *
from qgis.utils import iface
from qgis.core import QgsProject
import processing

""" Task 1. Adding Geopackae as Layers into QGIS """


""" 1.2. Creating a Dialog Box to ask for User Input on File to Add """
envPath = QFileDialog.getOpenFileName(QFileDialog(), "Environment Layer Select", "/home/abhishek/Desktop/M.Sc-GIS/data")[0]

""" 1.3. Adding Vector Layers into QGIS """
env = iface.addVectorLayer(envPath, "", "ogr")
env.setName("Environment")

atbnPath = QFileDialog.getOpenFileName(QFileDialog(), "Autobahn Layer Select", "/home/abhishek/Desktop/M.Sc-GIS/data")[0]
atbn = iface.addVectorLayer(atbnPath, "", "ogr")
atbn.setName("Autobahn")

""" Task 2. Adding Buffers to Autobahn Layer """


# 2.3. Creating a Buffer with a Standalone Script 

param = { 'INPUT' : atbn, 'DISTANCE' : 20, 'SEGMENTS' : 5, 'END_CAP_STYLE' : 0, 'JOIN_STYLE' : 0, 'MITER_LIMIT' : 2, 'DISSOLVE' : False, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:buffer", param)
autobahn20 = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])
autobahn20.setName("Autobahn 20")


""" 2.4. Creating 2 more Buffers """
param = { 'INPUT' : autobahn20, 'DISTANCE' : 100, 'SEGMENTS' : 5, 'END_CAP_STYLE' : 0, 'JOIN_STYLE' : 0, 'MITER_LIMIT' : 2, 'DISSOLVE' : False, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:buffer", param)
autobahn100 = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])
autobahn100.setName("Autobahn 100")

param = { 'INPUT' : autobahn100, 'DISTANCE' : 200, 'SEGMENTS' : 5, 'END_CAP_STYLE' : 0, 'JOIN_STYLE' : 0, 'MITER_LIMIT' : 2, 'DISSOLVE' : False, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:buffer", param)
autobahn300 = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])
autobahn300.setName("Autobahn 300")

""" Task 3. Performing Union on the Buffer Areas """
param = { 'INPUT' : autobahn20, 'OVERLAY' : autobahn100, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:union", param)
innerImpactArea = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])
innerImpactArea.setName("Inner Impact Area")

param = { 'INPUT' : innerImpactArea, 'OVERLAY' : autobahn300, 'OUTPUT' : 'memory:' }
algoOutput = processing.run("qgis:union", param)
impactArea = QgsProject.instance().addMapLayer(algoOutput['OUTPUT'])
impactArea.setName("Impact Area")
