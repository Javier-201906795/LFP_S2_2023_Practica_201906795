




def mensajebienvenida():
    mensaje =  '----------------------------------------------------------\n'
    mensaje += 'Practica 1 - LAB. Lenguajes formales y de programacion\n'
    mensaje += '---------------------------------------------------------\n'
    mensaje += '      Nombre: Javier Yllescas  | Carne: 20190675\n'
    mensaje += '---------------------------------------------------------\n'
    return mensaje


def menu():
    opcionvalida = 0

    mensaje =  '# Sistema de inventario:\n\n'
    mensaje += '1) Cargar inventario inicial\n'
    mensaje += '2) Cargar instrucciones movimientos\n'
    mensaje += '3) Crear informe de inventario\n'
    mensaje += '4) Salir\n'
    mensaje += '\n'
    print(mensaje)
    #Ingresar opcion
    opcion = input()
    #Validar opcion
    try:
      opcion = int(opcion)
      opcionvalida = opcion
    except:
      print("Ingrese un opcion numerica, porfavor vuelva a intentar.")
     

    return opcionvalida


def opcion1():
   print('opcion 1')

def opcion2():
   print('opcion 2')

def opcion3():
   print('opcion3')

def opcion4():
   print('opcion4')




################################################################

print(mensajebienvenida()) 

opcionmenu = menu()

print('opcion seleccionada: ', opcionmenu)

#SWITCH
if opcionmenu == 1:
   opcion1()
elif opcionmenu == 2:
   opcion2()
elif opcionmenu == 3:
   opcion3()
elif opcionmenu == 4:
   opcion4()
