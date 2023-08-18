




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
inventario['Bodega-A'] ={'productos':{'nombre':'manzana'}}


#print(inventario)
print(inventario['Bodega-A'])
print(inventario['Bodega-A']['productos'])



inventario['Bodega-A']['productos']



