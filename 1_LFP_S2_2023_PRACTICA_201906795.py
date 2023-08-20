
import os


#Variables globales
archivo_local = {'extension': None, 'validador': False, 'data': None}
inventario = {}
flagexistenciainventario = False
banderas = {'archivoinventario': False, 'movimientos': False}
contadores = {'automatizacion': 0}

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
   #ruta = 'test1.inv'
   #Automatizacion-B
   if (contadores['automatizacion'] < 1):
      ruta = 'test1.inv'
   else:
      ruta = 'test1.mov'

   contadores['automatizacion'] += 1


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
      

      try:
         archivo_local['extension']= str(extensionvalida)
         archivo_local['validador']= True
         archivo_local['data']= listaDatos
      except:
         print("Error al almacenar variables")





   except:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('! Error: Al abrir el archivo. !')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      menu()
    
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

def ordenarmovimientos():
   print('ordenar movimientos')
   listaDatos = archivo_local['data']
   print('------------------------------------------------')
   print(listaDatos)

   for i in range (0,len(listaDatos)):
      movimiento, producto = listaDatos[i][0].split()
      cantidad = listaDatos[i][1]
      ubicacion = listaDatos[i][2]

      print(movimiento, producto,cantidad, ubicacion)

      #++++++++++++++++++++++++++++++++++++++++++++
      # [ AGREGAR STOCK ]
      if (movimiento == 'agregar_stock'):
         
         #Producto Existe 
         #Valida existencia ubicacion
         if (ubicacion in inventario): 
            #Validar existencia producto
            if (producto in inventario[str(ubicacion)]):
               print('si existe el producto ', producto,' en la ubicacion ', ubicacion)
            else:
               print('NO existe el producto ', producto,' en la ubicacion ', ubicacion)
            
         else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('! ERROR no se encontro la ubicacion: ',ubicacion, ' | Linea: ', (i+1))
            print('¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡')
            banderas['movimientos'] = False
            break
            

         
      elif (movimiento == 'vender_producto'):
         print('vender')
      #++++++++++++++++++++++++++++++++++++++++++++
      # [ VENDER PRODUCTO ]
         #Validar existencia ubicacion (Bodega)
         #if

         #Validar existencia producto
         ##if

         #Validar operacion valida
         ###if
            #Validar operacion no den numero negativo (sin existencias)

    

#/////////////////////////////////////////////////
def opcion1():
   #Validador
   banderas['archivoinventario'] = False

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
      banderas['archivoinventario'] = True
     

     
   else:
      print('Inventario NO fueron leidos.')
  
   
   
   
   #Menu
   menu()



#/////////////////////////////////////////////////
def opcion2():
   #Validar si hay inventario
   if banderas['archivoinventario'] == True:
      print('# Cargar inventario inicial:')
      extensionarchivo = '.mov'
      abrirarchivo(extensionarchivo)

      #Evaluar
      if archivo_local['validador'] == True and archivo_local['extension'] == extensionarchivo:
         print('*******************************')
         print('* Archivo leido correctamente *')
         print('*******************************')
         #print(archivo_local['data'])

         ordenarmovimientos()

         print(banderas['movimientos'])

      else:
         print('Inventario NO fueron leidos.')
   else:
     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
     print('! Carge un inventario antes para continuar !')
     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
     print('\n presione una tecla para continuar')
     input()
     menu()
   

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