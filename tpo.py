# coding=utf-8
import random
#Funciones

#Funcion que imprime el menu por pantalla
#Se agregan las opciones necesarias segun el programa de cada uno.
def imprimirMenu():
    print("")
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Elige la opcion 1")   
    print("2 - Elige la opcion 2")
    print("3 - Elige la opcion 3")
    print("0 - Salir")
    print("********************************************")
    print("")
    
    return


#Funcion que valida que las opciones elegidas del menu sean las correctas.
#Solo valida numeros. Si se ingresa letras se corta el programa.
#Agregar las opciones necesarias segun el programa de cada uno.

def validarOpcionMenu(opcion):
    flag=True
    if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=0: #Se ha ingresado un valor invalido por menu
        flag=False
    
    return flag

def cargar_eventos():
    #eventos indices: 0: Casamiento, 1: quince, 2: cumpleaños, 3:bautismo, 4: otros
    cant_eventos = random.randint(10, 30)
    eventos = [0,0,0,0,0]
    for i in range(cant_eventos):
        evento = random.randint(0,4)
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

    return eventos, cant_eventos

def calcular_fact(evento, lista):
    if evento == 1:
        if lista[0] <= 50:
            precio = lista[0] * 75
        elif lista[0] > 50 and lista[0] < 100:
            precio = lista[0] * 65
        else:
            precio = lista[0] * 60
    elif evento == 2:
        if lista[0] <= 50:
            precio = lista[0] * 85
        elif lista[0] > 50 and lista[0] < 100:
            precio = lista[0] * 75
        else:
            precio = lista[0] * 70
    elif evento == 3:
        if lista[0] <= 50:
            precio = lista[0] * 65
        else:
            precio = lista[0] * 55
    elif evento == 4:
        if lista[0] <= 50:
            precio = lista[0] * 75
        else:
            precio = lista[0] * 65
    elif evento == 5:
        if lista[0] <= 50:
            precio = lista[0] * 100
        elif lista[0] > 50 and lista[0] < 100:
            precio = lista[0] * 90
        else:
            precio = lista[0] * 80
        
    return precio

def cargar_datos():

    # indices: 0: fotos, 1: facturacion
    casamientos = [0,0]
    quinces = [0,0]
    cumpleanios = [0,0]
    bautismos = [0,0]
    otros = [0,0]

    casamientos[0] = random.randint(30, 300)
    casamientos[1] = calcular_fact(1, casamientos)
    
    quinces[0] = random.randint(30, 300)
    quinces[1] = calcular_fact(2, quinces)
    
    cumpleanios[0] = random.randint(30, 300)
    cumpleanios[1] = calcular_fact(3, cumpleanios)
    
    bautismos[0] = random.randint(30, 300)
    bautismos[1] = calcular_fact(4, bautismos)
    
    otros[0] = random.randint(30, 300)
    otros[1] = calcular_fact(5, otros)

    return casamientos, quinces, cumpleanios, bautismos, otros

ca, q, cu, b, o = cargar_datos()

def total_fact(ca, q, cu, b, o):
    total_mes = ca[1] + q[1] + cu[1] + b[1] + o[1]
    return total_mes 

def fact_evento(e, ca, q, cu, b, o):
    facturaciones = [0, 0, 0, 0, 0]
    facturaciones[0] = e[0] * ca[1]
    facturaciones[1] = e[1] * q[1]
    facturaciones[2] = e[2] * cu[1]
    facturaciones[3] = e[3] * b[1]
    facturaciones[4] = e[4] * o[1]
    
    return facturaciones

e, cant_e = cargar_eventos()
facturaciones = fact_evento(e, ca, q, cu, b, o)

def burbujeo(facturaciones, e): # a chequear, anda raro
    largo = len(facturaciones)
    fact_ordenada = []
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo-1):
            if facturaciones[i]<facturaciones[i+1]:
                aux = facturaciones[i]
                facturaciones[i] = facturaciones[i+1]
                facturaciones[i+1] = aux
                fact_ordenada.append(facturaciones[i])
                aux = e[i]
                e[i] = e[i+1]
                e[i+1] = aux
                desordenada = True
    return fact_ordenada
    
def mostrar_detalle_eventos_tipo(tipo, eventos, facturaciones, fotos):
    if tipo < 0 or tipo > 4:
        print("Tipo de evento inválido. Debe ser un número del 0 al 4.")
        return

    nombres_tipos = ["Casamientos", "Quinceañeras", "Cumpleaños", "Bautismos", "Otros"]
    nombre_tipo_seleccionado = nombres_tipos[tipo - 1]

    print("Detalle de eventos de tipo:", nombre_tipo_seleccionado)
    
    for i in range(len(eventos)):
        if eventos[i] == tipo:
            print("Evento", i + 1, ":")
            print("  Facturación:", facturaciones[i])
            print("  Cantidad de fotos:", fotos[i])
            print()

    # Ejemplo de uso de la función
    # Supongamos que tienes las listas 'eventos', 'facturaciones' y 'fotos' que contienen la información de los eventos
    # eventos = [1, 2, 3, 4, 2, 1, 5, 3, 2]
    # facturaciones = [200, 300, 150, 100, 250, 180, 400, 120, 350]
    # fotos = [100, 150, 80, 60, 120, 90, 200, 70, 180]

    tipo_seleccionado = int(input("Ingrese el tipo de evento (1-5) para ver detalles: "))
    mostrar_detalle_eventos_tipo(tipo_seleccionado, eventos, facturaciones, fotos)

#************************   
#Programa principal
#************************   

print("Bienvenido al programa")
print("")

#Leer la primera vez la opcion del menu
imprimirMenu()
opcion = int(input("Ingrese la opcion elegida del menu principal: "))



#Comienzo del proceso de las opciones del menu elegidas.
while opcion!=0:
    
    flagMenu = validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, vuelva a ingresar...")
        print()
        opcion = int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu = validarOpcionMenu(opcion)

    #opciones validas del menú
    if opcion==1:
        print("Total de facturacion del mes y cantidad de eventos:")
        print("La cantidad de eventos fue de: ", cant_e, " y el total facturado es de: ", total_fact(ca, q, cu, b, o))
        
    elif opcion==2:
        print("Has elegido la opcion 2") 
        print(fact_evento(e, ca, q, cu, b, o))
        print(burbujeo(facturaciones, e))
    elif opcion==3:
        print("Has elegido la opcion 3")
        # Solicita al usuario el tipo de evento que desea ver
        tipo_seleccionado = int(input("Ingrese el tipo de evento (0-4) para ver detalles: "))
    
        # Llama a la función para mostrar los detalles de eventos del tipo seleccionado
        mostrar_detalle_eventos_tipo(tipo_seleccionado, facturaciones, fotos)

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

print("FIN DEL PROGRAMA")
    
    

#Fin del programa
