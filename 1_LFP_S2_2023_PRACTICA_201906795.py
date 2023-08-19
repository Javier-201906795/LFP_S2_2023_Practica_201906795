
import os


#Variables globales
archivo = {'extension': None, 'validador': False, 'data': None}

#Inicializar variables globales
archivo['extension']= None
archivo['validador']= False
archivo['data']= None




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


def abrirarchivo(extensionvalida):
    #Mensaje
    print('\nSeleccione un archivo'+ str(extensionvalida)+'\n')
    print('-------------------------------------------------------------------')
    print('Nota: el archivo debe estar en la misma carpeta que el proyecto.')
    print('Nota 2: si desea salir presione el numero " 4 ".')
    print('-------------------------------------------------------------------')
    
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        print('ruta', ruta)
        #Salir 
        if ruta == '4':
           break
        #Validar extension
        nombre, extension = os.path.splitext(ruta)
        print('extension',extension)
        if extension == str(extensionvalida):
            print("\nArchivo valido\n")
            break
        else:
            print("\nArchivo invalido\n")
            ruta = input("\nIngrese la ruta del archivo: ")

    
    #Abrir archivo  
    listaDatos = []
    try:
      with open(ruta, "r") as archivo:
        for linea in archivo:
            #Array por salto de linea
            array = linea.split('\n')
            for i in range(len(array)):
                if array[i] == '' or array[i] == ' ':
                  None
                else:
                  listaDatos.append(array[i])
    except:
      print("Error: Al abrir el archivo.")
    
    print(listaDatos) 

    

#/////////////////////////////////////////////////
def opcion1():
  print('# Cargar inventario inicial:')
  abrirarchivo('.inv')
  # listaDatos = []
  # print("\nHa seleccionado cargar archivo .inv\n")
  # ruta = input("Ingrese la ruta del archivo: ")

  # while True:
  #     nombre, extension = os.path.splitext(ruta)
  #     if extension == ".inv":
  #         print("\nArchivo valido\n")
  #         break
  #     else:
  #         print("\nArchivo invalido\n")
  #         ruta = input("\nIngrese la ruta del archivo: ")

  # with open(ruta, "r") as archivo:
  #         for linea in archivo:
  #             array = linea.split(',')
  #             for i in range(len(array)):
  #                 listaDatos.append(array[i])
  
  # print(listaDatos)




#/////////////////////////////////////////////////
def opcion2():
   print('opcion 2')

#/////////////////////////////////////////////////
def opcion3():
   print('opcion3')

#/////////////////////////////////////////////////
def opcion4():
   print('opcion4')
#/////////////////////////////////////////////////



################################################################

print(mensajebienvenida()) 

opcionmenu = menu()

#SWITCH
if opcionmenu == 1:
   opcion1()
elif opcionmenu == 2:
   opcion2()
elif opcionmenu == 3:
   opcion3()
elif opcionmenu == 4:
   opcion4()


################################################################