layers = iface.mapCanvas().layers() 
for layer in layers: 
    print(layer) 
    print(layer.name()) 
    print(layer.id()) 
    print('------') 
 
activeLayer = iface.activeLayer() 
print('active layer: ' + activeLayer.name()) 
