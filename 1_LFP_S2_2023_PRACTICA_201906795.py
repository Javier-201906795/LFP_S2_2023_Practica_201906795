




def mensajebienvenida():
    mensaje =  '----------------------------------------------------------\n'
    mensaje += 'Practica 1 - LAB. Lenguajes formales y de programacion\n'
    mensaje += '---------------------------------------------------------\n'
    mensaje += '      Nombre: Javier Yllescas  | Carne: 20190675\n'
    mensaje += '---------------------------------------------------------\n'
    return mensaje


def menu():
    mensaje =  '# Sistema de inventario:\n\n'
    mensaje += '1) Cargar inventario inicial\n'
    mensaje += '2) Cargar instrucciones movimientos\n'
    mensaje += '3) Crear informe de inventario\n'
    mensaje += '4) Salir\n'
    mensaje += '\n'
    return mensaje








################################################################

print(mensajebienvenida()) 
print(menu())
#Seleccione una opcion
opcion = input()
print(opcion)
#Validar opcion
try:
  opcion = int(opcion)
except:
  print("Ingrese un opcion numerica, porfavor vuelva a intentar.")


if opcion == 1:
    print('hola')

