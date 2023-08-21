
import os


#Variables globales
archivo_local = {'extension': None, 'validador': False, 'data': None}
inventario = {}
flagexistenciainventario = False
banderas = {'archivoinventario': False, 'movimientos': False}
errores = {'archivo-inv':[], 'archivo-mov':[],'errores-inv':False, 'errores-mov':False, 'errores-invtxt': True}

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

   print('bandera', banderas['archivoinventario'])
   mensaje =  '\n\n# Sistema de inventario:\n'
   if (banderas['archivoinventario'] == True):
      mensaje += '## [ Inventario cargado ]\n'
   if (banderas['movimientos'] == True):
      mensaje += '### [ Movimientos cargado ]\n'

   mensaje += '\n'
   mensaje += '1) Cargar inventario inicial\n'
   mensaje += '2) Cargar instrucciones movimientos\n'
   mensaje += '3) Crear informe de inventario\n'
   mensaje += '4) Salir\n'
   mensaje += '\n'
   print('================================================================')
   print(mensaje)
   #Ingresar opcion
   opcion = input()
   #Validar opcion
   try:
      opcion = int(opcion)
      opcionvalida = opcion
   except:
      print("Ingrese un opcion numerica, porfavor vuelva a intentar.")
     
   print('================================================================')
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
         #print(str(ubicacion) +' ya se encuentra en el inventario')
         pass
      else:
         #print(' • Agregando nueva ubicacion ', ubicacion)
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
            print('██ Error producto: ', producto, 'NO se agrego a ', tempubicacion, ' porque ya existe el producto', ' ##Linea: ',(i+1))
         else:
            print(' • Agregando produto ', producto, ' a ', tempubicacion)
            inventario[str(tempubicacion)][str(producto)] = {'cantidad':float(cantidad),'precio':float(precio)}
            
      else:
         print('██ Error no se agrego el producto porque la instruccion es diferente.\n'+ str(instruccion) +' != crear_producto '+ ' ##Linea '+str(i+1) )
      
      #++++++++++++++++++++++++++++++++++++++++++++
   print('-------------------------------')
   print('   [ INVENTARIO ]')
   print(inventario)
   print('-------------------------------')
   
#/////////////////////////////////////////////////

def ordenarmovimientos():
   #Validador
   banderas['movimientos'] = False
   print('ordenar movimientos')
   listaDatos = archivo_local['data']
   print('------------------------------------------------')
   print(listaDatos)
   print('------------------------------------------------')

   for i in range (0,len(listaDatos)):
      movimiento, producto = listaDatos[i][0].split()
      cantidad = listaDatos[i][1]
      ubicacion = listaDatos[i][2]

      #print(movimiento, producto,cantidad, ubicacion)

      #++++++++++++++++++++++++++++++++++++++++++++
      # [ AGREGAR STOCK ]
      if (movimiento == 'agregar_stock'):
         #Producto Existe 
         #Valida existencia ubicacion
         if (ubicacion in inventario): 
            #Validar existencia producto
            if (producto in inventario[str(ubicacion)]):
               #Actualizar inventario
               antiguacantidad = inventario[str(ubicacion)][str(producto)]['cantidad']
               nuevacantidad = float(antiguacantidad) + float(cantidad)
               inventario[str(ubicacion)][str(producto)]['cantidad'] = nuevacantidad
               print(' • Se agrego el producto ', producto,' en la ubicacion ', ubicacion, ' | ',antiguacantidad, ' + ', cantidad,' -> ',inventario[str(ubicacion)][str(producto)]['cantidad'], ' ## Linea: ', (i+1))
               #Validador
               banderas['movimientos'] = True
            else:
               mensaje = '██ NO existe el producto ', producto,' en la ubicacion ', ubicacion, ' ## Linea: ',(i+1)
               print(mensaje)
               if (errores['errores-mov'] == True):
                  input()
            
         else:
            mensaje = '██ ERROR no se encontro la ubicacion: '+ str(ubicacion) + ' ## Linea: ' + str((i+1))
            print(mensaje)
            if (errores['errores-mov'] == True):
               input()
            
            

         
      elif (movimiento == 'vender_producto'):
      #++++++++++++++++++++++++++++++++++++++++++++
      # [ VENDER PRODUCTO ]
         #Validar existencia ubicacion (Bodega)
         if (ubicacion in inventario): 
            #Validar existencia producto
            if (producto in inventario[str(ubicacion)]):
               #Validar operacion valida
               ##operacioes
               cantidadproducto = inventario[str(ubicacion)][str(producto)]['cantidad']
               venta = float(cantidad)
               nuevacantidad = float(cantidadproducto) - venta
               #Validar operacion no den numero negativo (sin existencias)
               if (nuevacantidad >= 0):
                  inventario[str(ubicacion)][str(producto)]['cantidad'] = nuevacantidad
                  print(' • Venta de ',cantidad,' ', producto, ' de ',ubicacion,'. | Existencias: ', cantidadproducto,' - ',venta,' -> ',nuevacantidad, ' ## Linea: ' ,str((i+1)) )
                  #Validador
                  banderas['movimientos'] = True
               else:
                  mensaje ='██ Error: NO hay suficientes '+str(producto)+' en ' +str(ubicacion)+' | Existencias:' +str(cantidadproducto) +' - '+ str(venta)+ ' -> '+str(nuevacantidad) + ' ## Linea: ' + str((i+1))
                  print(mensaje)
                  if (errores['errores-mov'] == True):
                     input()
                  
               
            else:
               mensaje = '██ Error: NO existe el producto ' +  str(producto) + ' en la ubicacion ' + str(ubicacion)  + ' ## Linea: ' + str((i+1))
               print(mensaje)
               if (errores['errores-mov'] == True):
                  input()
        
         else:
            mensaje = '██ Error: NO se encontro la ubicacion: '+ str(ubicacion) + ' ## Linea: ' +str(i+1)
            print(mensaje)
            if (errores['errores-mov'] == True):
                  input()

#/////////////////////////////////////////////////
def crearinformeinventariomensaje():
   mensajeinventario =  'Informe de Inventario: \n'
   mensajeinventario += '\n'
   mensajeinventario += ' ___________________________________________________________________\n'
   mensajeinventario += '|   Producto  | Cantidad | Precio und. | Valor Total |   Ubicacion  | \n'
   mensajeinventario += ' -------------------------------------------------------------------\n'

   #Inventario
   #Obtener lista de ubicaciones
   listaubicaciones = list(inventario)
   #Obtener lista de productos
   listaproductos = []
   #Recorre ubicaicones
   for i in range (0,len(listaubicaciones)):
      ubicacion = listaubicaciones[i]
      #Recorre productos
      for producto in inventario[str(ubicacion)]:
         #Obtiene precio
         precio = inventario[str(ubicacion)][str(producto)]['precio']
         cantidad = inventario[str(ubicacion)][str(producto)]['cantidad']
         valortotal = float(precio) + float(cantidad)
         #Imprimir valores 
         #Configuraciones Imprimir valores
         espaciosproducto = 13
         espacioscantidad = 10
         espaciospreciound = 13
         espaciosvalortotal = 13
         espaciosubicacion = 13
         #Formato de valores
         cantidad = f"{cantidad:.{1}f}"
         precio = f"{precio:.{2}f}"
         valortotal = f"{valortotal:.{2}f}"
         #Estructura con espacios para su tabulacion
         txtproducto = str(producto)[0:(espaciosproducto-1)].ljust(espaciosproducto," ")
         txtcantidad = str(cantidad)[0:(espaciosproducto-1)].rjust(espacioscantidad," ")
         txtpreciound = str(precio)[0:(espaciospreciound-1)].rjust((espaciospreciound-2),"¸")
         txtvalortotal = str(valortotal)[0:(espaciosvalortotal-1)].rjust((espaciosvalortotal-2),"¸")
         txtubicacion = str(ubicacion)[0:(espaciosubicacion-1)].center(espaciosubicacion+1)
         #Agregar nueva linea
         mensajeinventario += '|'+txtproducto+'|'+txtcantidad+'| Q'+txtpreciound+'| Q'+txtvalortotal+'|'+txtubicacion+'|\n'
           
         
         
   
   mensajeinventario += ' -------------------------------------------------------------------\n'

   
   


   return mensajeinventario

#/////////////////////////////////////////////////
def creararchivoinventario(texto):
   #Validador
   errores['errores-invtxt']=True
   print('• Creando archivo inventario_201906795.txt')
   try:
      #crear archivo  
      archivo = open("inventario_201906795.txt", "a")
      archivo.write(texto)
      archivo.close()
      print('• Escritura del contenido correctamente')
      #Validador
      errores['errores-invtxt']=False
   except:
      print('Error al crear archivo inventario_201906795.txt')

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

         print('Validador movimientos ->',banderas['movimientos'])

         menu()
      else:
         print('Error: Inventario NO fueron leidos.')
   else:
     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
     print('! Carge un inventario antes para continuar !')
     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
     print('\n presione una tecla para continuar')
     input()
     menu()
   

#/////////////////////////////////////////////////
def opcion3():
   print('# Crer Informe de invantario.')

   if banderas['archivoinventario'] == True and banderas['movimientos'] == True:

      print()
      print('**********************************************************************************')

      textoinventario = crearinformeinventariomensaje()
      print(textoinventario)

      print('**********************************************************************************')
      
      creararchivoinventario(textoinventario)

      #Validador
      if (errores['errores-invtxt'] == False):
         print('*********************************************************')
         print('* Archivo inventario_201906795.txt creado correctamente *')
         print('*********************************************************')

      
   elif banderas['archivoinventario'] == False:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('! Carge un inventario antes para continuar !')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
   elif banderas['movimientos'] == False:
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print('! Carge un listado de movimientos antes para continuar !')
      print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

   #menu()

#/////////////////////////////////////////////////
def opcion4():
   print('Salir.')
#/////////////////////////////////////////////////



################################################################

print(mensajebienvenida()) 

menu()



################################################################