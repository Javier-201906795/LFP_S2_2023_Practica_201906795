




print("Hola mundo")


# diccionario
productos = {}


productos['manzana']={'cantidad':100,'precio':2.5,'ubicacion':'bodeaga-A'}
productos['pera']={'cantidad':80,'precio':5.0,'ubicacion':'bodeaga-B'}



print(productos)
print('------')
print(productos['manzana'])
print('------')
print(productos['manzana']['cantidad'])
print('------')

print('### Buscando Peras ###')
if 'pera' in productos:
    print("hay peras")
else:
    print("no hay peras")


print('### Buscando Uvas ###')
if 'uva' in productos:
    print("hay uvas")
else:
    print("no hay uvas")


print('### Buscando Peras en bodega-B ###')
if 'bodeaga-B' in productos['pera']['ubicacion']:
    print("SI hay peras en bodega-b")
else:
    print("no hay peras en bodega-b")


print()
print('----------------------------------------')
#Diccionarios

inventario = {}

#inventario['Bodega-A'] ={'productos':['manzana']}
inventario['Bodega-A'] ={'productos':{'manzana':'objeto1'}}


#print(inventario)
print(inventario['Bodega-A'])
print(inventario['Bodega-A']['productos'])



inventario['Bodega-A']['productos']['pera'] = "objeto2"


print(inventario['Bodega-A']['productos'])

print()
print()
print()
print()
print()
print('----------------------------------------')

#Diccionarios Estructura

inventario = {}
#Crear producto
inventario['Bodega-A'] ={'productos':{'manzana':{'cantidad':100,'precio':2.50}}}

print(inventario['Bodega-A']['productos'])
print(inventario['Bodega-A']['productos']['manzana'])
print(inventario['Bodega-A']['productos']['manzana']['cantidad'])
print(inventario['Bodega-A']['productos']['manzana']['precio'])

print('#### agregar producto a bodega A')

inventario['Bodega-A']['productos']['pera'] = {'cantidad':80,'precio':4.50}

print(inventario['Bodega-A']['productos'])
print(inventario['Bodega-A']['productos']['pera'])
print(inventario['Bodega-A']['productos']['pera']['cantidad'])
print(inventario['Bodega-A']['productos']['pera']['precio'])

inventario['Bodega-B'] ={'productos':{'manzana':{'cantidad':50,'precio':2.50}}}

print('//////')
print(inventario)
print(inventario['Bodega-B'])
print(inventario['Bodega-A'])


print('### Valida si hay manzanas en bodega A')
if 'manzana' in inventario['Bodega-A']['productos']:
    print("hay manzanas")
else:
    print("no hay manzanas")



print('### Valida si hay uvas en bodega A')
if 'uva' in inventario['Bodega-A']['productos']:
    print("hay uvas")
else:
    print("no hay uvass")
