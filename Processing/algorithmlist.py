#Problem Statement: Display list of Algorithm names in the QGIS Software
count=0
for alg in QgsApplication.processingRegistry().algorithms():
    count=count+1
    print(alg.id(),"->",alg.displayName())
print("No of Algorithms are=",count)