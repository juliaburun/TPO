# coding=utf-8
import random
#Funciones

#Funcion que imprime el menu por pantalla
def imprimirMenu():
    print("")
    print("********************************************")
    print("Debe elegir una opcion, solo números enteros")
    print("1 - Total de la facturación")   
    print("2 - Facturación por tipo de evento")
    print("3 - Listado detallado facturado")
    print("4 - Por selección de tipo de evento")
    print("0 - Salir")
    print("********************************************")
    print("")
    
    return

#Funcion que valida que las opciones elegidas del menu sean las correctas.
#Solo valida numeros. Si se ingresa letras se corta el programa.

def validarOpcionMenu(opcion):
    flag=True
    if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=0: #Se ha ingresado un valor invalido por menu
        flag=False
    
    return flag

def cargar_eventos():
    #eventos indices: 0: Casamiento, 1: quince, 2: cumpleaños, 3:bautismo, 4: otros
    #cant_eventos = [0,0,0,0,0]
    #for i in range(0,len(cant_eventos),1):
    #    cant_eventos[i] = random.randint(10,30)

    #return cant_eventos
    eventos = [0,0,0,0,0]
    cant_eventos = random.randint(10, 30)
    for i in range(cant_eventos):
        evento = random.randint(1,5)
        if evento == 1:
            eventos[0] += 1
        elif evento == 2:
            eventos[1] += 1
        elif evento == 3:
            eventos[2] += 1
        elif evento == 4:
            eventos[3] += 1
        elif evento == 5:
            eventos[4] += 1

    return eventos

def calcular_fact(evento, cantidad_fotos):
    if evento == 1:
        if cantidad_fotos <= 50:
            precio = cantidad_fotos * 75
        elif cantidad_fotos > 50 and cantidad_fotos < 100:
            precio = cantidad_fotos * 65
        else:
            precio = cantidad_fotos * 60
    elif evento == 2:
        if cantidad_fotos <= 50:
            precio = cantidad_fotos * 85
        elif cantidad_fotos > 50 and cantidad_fotos < 100:
            precio = cantidad_fotos * 75
        else:
            precio = cantidad_fotos * 70
    elif evento == 3:
        if cantidad_fotos <= 50:
            precio = cantidad_fotos * 65
        else:
            precio = cantidad_fotos * 55
    elif evento == 4:
        if cantidad_fotos <= 50:
            precio = cantidad_fotos * 75
        else:
            precio = cantidad_fotos * 65
    elif evento == 5:
        if cantidad_fotos <= 50:
            precio = cantidad_fotos * 100
        elif cantidad_fotos > 50 and cantidad_fotos < 100:
            precio = cantidad_fotos * 90
        else:
            precio = cantidad_fotos * 80
        
    return precio

def cargar_datos():
    casamientos = []
    quinces = []
    cumpleanios = []
    bautismos = []
    otros = []
    
    for x in range(len(eventos)):
        for i in range(eventos[x]):
            cantidad_fotos = random.randint(30, 300)
            total_facturado = calcular_fact(x+1, cantidad_fotos)
            if x == 0:
                casamientos.append([cantidad_fotos, total_facturado])
            elif x == 1:
                quinces.append([cantidad_fotos, total_facturado])
            elif x == 2:
                cumpleanios.append([cantidad_fotos, total_facturado])
            elif x == 3:
                bautismos.append([cantidad_fotos, total_facturado])
            elif x == 4:
               otros.append([cantidad_fotos, total_facturado])
            # indices: 0: fotos, 1: facturacion
           
        
    return casamientos, quinces, cumpleanios, bautismos, otros #[[adentro de casami],[adentro de quin],...]



def total_fact():
    # listaDatosCargados = cargar_datos()
    i = 0
    total_mes = 0
    while (i < len(listaDatosCargados)):
        for x in range(len(listaDatosCargados[i])):
            total_mes += listaDatosCargados[i][x][1] 
        i = i+1
    
    return total_mes 

def total_eventos():
    # eventos = cargar_eventos()
    i = 0 
    total = 0
    while(i < len(eventos)):
        total += eventos[i]
        i += 1
    return total

def fact_evento():
  
    i = 0
    facturaciones=[]
    fotosSacadasTotal=[]

    while (i < len(listaDatosCargados)):
        total_mesFotos = 0
        total_mesFactura=0

        for x in range(len(listaDatosCargados[i])):
            total_mesFotos += listaDatosCargados[i][x][0]  
            total_mesFactura += listaDatosCargados[i][x][1]  
        
        facturaciones.append(total_mesFactura)
        fotosSacadasTotal.append(total_mesFotos)
        i = i+1
    

    return facturaciones, fotosSacadasTotal

def burbujeo(e):
    facturaciones, fotos = fact_evento()
    largo = len(facturaciones)
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo-1, 0, -1):
            if facturaciones[i]>facturaciones[i-1]:
                # Intercambiar elementos en facturaciones
                facturaciones[i], facturaciones[i-1] = facturaciones[i-1], facturaciones[i]
                # Intercambiar elementos en e (eventos)
                e[i], e[i-1] = e[i-1], e[i]
                desordenada = True
    return facturaciones, e

def burbujeoCompleto(e):
    largo = len(e)
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo-1):
            if e[i][1] < e[i+1][1]:  # Comparamos el segundo elemento (facturación)
                e[i], e[i+1] = e[i+1], e[i]  # Intercambiamos las sublistas
                desordenada = True
    return e

def mostrar_total_facturacion_por_tipo():
    # eventos = cargar_eventos()
    # lista con índices de tipos de evento
    tipos_evento = [1, 2, 3, 4, 5]
    # Ordenar la lista
    facturaciones, tipos_evento = burbujeo(tipos_evento)
    i=0

    print("Total de facturación por tipo de evento y cantidad de eventos ordenado por facturación:")
    for tipo in tipos_evento:
        if tipo == 1:
            print("Casamiento")
        elif tipo == 2:
            print("Quinceaños")
        elif tipo == 3:
            print("Cumpleaños")
        elif tipo == 4:
            print("Bautismo")
        elif tipo == 5:
            print("Otros")
        
        print("Total facturado:", facturaciones[i], "Pesos")
        print("Cantidad de eventos:", eventos[i])
        print("")
        i+=1
        
def mostrar_total_facturacion_detallado():
    lista_combinada = []
    for idx, lista in enumerate(listaDatosCargados, start=1):
        for sublista in lista:
            sublista.append(idx)  
            lista_combinada.append(sublista)

    lista_ordenada = burbujeoCompleto(lista_combinada)
    for detalle in lista_ordenada:
        if detalle[2] == 1:
            print("Casamientos ","Cantidad:", detalle[0]," $ ",detalle[1] )
        elif detalle[2] == 2:
            print("Quinceañeras ","Cantidad:", detalle[0]," $ ",detalle[1] )
        elif detalle[2] == 3:
            print("Cumpleaños ","Cantidad:", detalle[0]," $ ",detalle[1] )
        elif detalle[2] == 4:
            print("Bautismos ","Cantidad:", detalle[0]," $ ",detalle[1] )
        elif detalle[2] == 5:
            print("Otros ","Cantidad:", detalle[0]," $ ",detalle[1] )


def mostrar_detalle_eventos_tipo(tipo): #eventos es historial de cantidad de veces que se realizo

    facturaciones, fotos = fact_evento()
    # eventos = cargar_eventos()
    if tipo < 0 or tipo > 4:
        print("Tipo de evento inválido. Debe ser un número del 1 al 5.")
        return

    nombres_tipos = [1, 2, 3, 4, 5]
    nombre_tipo_seleccionado = nombres_tipos[tipo]
    
    if nombre_tipo_seleccionado == 1:
        print("Detalle de evento Casamientos")
    elif nombre_tipo_seleccionado == 2:
        print("Detalle de evento Quinceañeras")
    elif nombre_tipo_seleccionado == 3:
        print("Detalle de evento Cumpleaños")
    elif nombre_tipo_seleccionado == 4:
        print("Detalle de evento Bautismos")
    elif nombre_tipo_seleccionado == 5:
        print("Detalle de evento Otros")

    print("Cantidad de eventos realizados:", eventos[nombre_tipo_seleccionado - 1])
    print("Facturación:", facturaciones[nombre_tipo_seleccionado - 1], "Pesos")
    print("Cantidad de fotos:", fotos[nombre_tipo_seleccionado - 1])

    
#************************   
#Programa principal
#************************   
eventos = cargar_eventos()
listaDatosCargados = cargar_datos()
print(listaDatosCargados)
print("Bienvenido al programa")
print("")

#Leer la primera vez la opcion del menu
imprimirMenu()
opcion = int(input("Ingrese la opcion elegida del menu principal: "))

#Comienzo del proceso de las opciones del menu elegidas.
while opcion!=0:
    
    flagMenu = validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opción de menu invalida, vuelva a ingresar...")
        print()
        opcion = int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu = validarOpcionMenu(opcion)

    #opciones validas del menú
    if opcion==1:
        print("Total de facturación del mes y cantidad de eventos:")
        print("La cantidad de eventos fue de:", total_eventos(), " y el total facturado es de: $", total_fact())
        
    elif opcion==2:
        # Agrupados por tipo de evento
        print("Total de facturación por tipo de evento y la cantidad de eventos ordenados por facturación:") 
        print("---------------")
        mostrar_total_facturacion_por_tipo()
      
    elif opcion==3:
        # Todos los items, sin agrupar
        print("Listado completo del total facturado de cada evento con su tipo, ordenado por total facturado:")
        
        mostrar_total_facturacion_detallado()
    elif opcion==4:
        print("Has elegido la opcion 4")
        # Solicita al usuario el tipo de evento que desea ver
        tipo_seleccionado = int(input("Ingrese el tipo de evento (1-5) para ver detalles: "))
        mostrar_detalle_eventos_tipo(tipo_seleccionado - 1)

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

print("FIN DEL PROGRAMA")
    
#Fin del programa