


mensajeinventario = 'Producto      Cantidad    Precio und.    Valor Total    Ubicacion \n'
lista = ['manzana', 'pera', 'Uvas', 'caja de comflakes edicion especial de colleccion']

print(mensajeinventario)
for producto in lista:
    mensaje = producto.ljust(15," ") + '|'
    print(mensaje)