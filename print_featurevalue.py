iterator=iface.activeLayer().getFeatures()
features=list(iterator)
for i in features:
    print(i[0])