for x in QgsApplication.processingRegistry().algorithms():
    if "dissolve" in x.id():
        print(x.id(),"->",x.displayName())