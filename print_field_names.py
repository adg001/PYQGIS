layer=iface.activeLayer()
fields=layer.fields()
field_names=[field.name() for field in fields]
print(field_names)