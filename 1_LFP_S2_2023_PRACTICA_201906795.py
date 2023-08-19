
import os


#Variables globales
archivo_local = {'extension': None, 'validador': False, 'data': None}
inventario = {}
flagexistenciainventario = False

#Inicializar variables globales
archivo_local['extension']= None
archivo_local['validador']= False
archivo_local['data']= None




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
     

    #SWITCH
   if opcion == 1:
      opcion1()
   elif opcion == 2:
      opcion2()
   elif opcion == 3:
      opcion3()
   elif opcion == 4:
      opcion4()


def abrirarchivo(extensionvalida):
   archivo_local['validador']= False
   #Mensaje
   print('\nSeleccione un archivo'+ str(extensionvalida)+'\n')
   print('-------------------------------------------------------------------')
   print('Nota: el archivo debe estar en la misma carpeta que el proyecto.')
   print('Nota 2: si desea salir presione el numero " 4 ".')
   print('-------------------------------------------------------------------')
   
   #ruta = input("Ingrese la ruta del archivo: ")
   #Automatizacion
   ruta = 'test1.inv'

   while True:
      #print('ruta', ruta)
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
                  #New array por ; punto y coma
                  newarray = array[i].split(';')
                  listaDatos.append(newarray)



      #Almacenar Archivo
      #print(listaDatos) 
      #print(listaDatos[0]) 
      #print(listaDatos[0][0]) 

      try:
         archivo_local['extension']= str(extensionvalida)
         archivo_local['validador']= True
         archivo_local['data']= listaDatos
      except:
         print("Error al almacenar variables")





   except:
      print("Error: Al abrir el archivo.")
    
#/////////////////////////////////////////////////

def ordenarinventario():
   print('ordenando...')
   listaDatos = archivo_local['data']
   

   #++++++++++++++++++++++++++++++++++++++++++++
   #Agregar ubicaciones a inventario
   for i in range (0,len(listaDatos)):
      ubicacion = listaDatos[i][3]

      #Evaluar ubicacion
      if ubicacion in inventario:
         print(str(ubicacion) +' ya se encuentra en el inventario')
      else:
         print('agregando nueva ubicacion ', ubicacion)
         inventario[str(ubicacion)] = {}

   #++++++++++++++++++++++++++++++++++++++++++++
   #Agregar productos a inventario
   for i in range (0,len(listaDatos)):

      instruccionproducto = listaDatos[i][0]
      instruccion, producto = instruccionproducto.split()
      cantidad = listaDatos[i][1]
      precio = listaDatos[i][2]
      tempubicacion = listaDatos[i][3]

      #Validar instruccion
      if instruccion == 'crear_producto':
         #Validar si existe el producto
         if (producto in inventario[str(tempubicacion)]):
            print('producto: ', producto, 'NO se agrego a ', tempubicacion, ' porque ya existe el producto')
         else:
            print('agregando produto ', producto, ' a ', tempubicacion)
            inventario[str(tempubicacion)][str(producto)] = {'cantidad':float(cantidad),'precio':float(precio)}
            
      else:
         print('no se agrego el producto porque la instruccion es diferente.\n'+ str(instruccion) +' != crear_producto')
      
      #++++++++++++++++++++++++++++++++++++++++++++
   print('-------------------------------')
   print(inventario)
   print('-------------------------------')
   


    

#/////////////////////////////////////////////////
def opcion1():
  print('# Cargar inventario inicial:')
  extensionarchivo = '.inv'
  abrirarchivo(extensionarchivo)

  #Evaluar
  if archivo_local['validador'] == True and archivo_local['extension'] == extensionarchivo:
     print('*******************************')
     print('* Archivo leido correctamente *')
     print('*******************************')
     #print(archivo_local['data'])

     ordenarinventario()

     print('********************************')
     print('* Lista ordenada correctamente *')
     print('********************************')

     #Validador
     flagexistenciainventario = True 
  else:
     print('Inventario NO fueron leidos.')
  
  



#/////////////////////////////////////////////////
def opcion2():
   #Validar si hay inventario
   if flagexistenciainventario == True:
      print('# Cargar inventario inicial:')
      extensionarchivo = '.mov'
      abrirarchivo(extensionarchivo)

      #Evaluar
      if archivo_local['validador'] == True and archivo_local['extension'] == extensionarchivo:
         print('*******************************')
         print('* Archivo leido correctamente *')
         print('*******************************')
         print(archivo_local['data'])
      else:
         print('Inventario NO fueron leidos.')
   else:
     print('Carge un inventario antes para continuar')
   

#/////////////////////////////////////////////////
def opcion3():
   print('opcion3')

#/////////////////////////////////////////////////
def opcion4():
   print('opcion4')
#/////////////////////////////////////////////////



################################################################

print(mensajebienvenida()) 

menu()



################################################################