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
    
#************************   
#Programa principal
#************************   

print("Bienvenido al programa")
print("")

#Leer la primera vez la opcion del menu
imprimirMenu()
opcion = int(input("Ingrese la opcion elegida del menu principal: "))

# indices: 0: facturacion, 1: cantidad de fotos
casamientos = [0,0]
quinces = [0,0]
cumpleanios = [0,0]
bautismos = [0,0]
otros = [0,0]
cant_eventos = random.randint(10, 30)

#eventos indices: 0: Casamiento, 1: quince, 2: cumpleaños, 3:bautismo, 4: otros
def cargar_eventos():
    eventos = [0,0,0,0,0]
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

def calcular_fact(evento, lista):
    if evento == 1:
        if lista[1] <= 50:
            precio = lista[1] * 75
        elif lista[1] > 50 and lista[1] < 100:
            precio = lista[1] * 65
        else:
            precio = lista[1] * 60
    elif evento == 2:
        if lista[1] <= 50:
            precio = lista[1] * 85
        elif lista[1] > 50 and lista[1] < 100:
            precio = lista[1] * 75
        else:
            precio = lista[1] * 70
    elif evento == 3:
        if lista[1] <= 50:
            precio = lista[1] * 65
        else:
            precio = lista[1] * 55
    elif evento == 4:
        if lista[1] <= 50:
            precio = lista[1] * 75
        else:
            precio = lista[1] * 65
    elif evento == 5:
        if lista[1] <= 50:
            precio = lista[1] * 100
        elif lista[1] > 50 and lista[1] < 100:
            precio = lista[1] * 90
        else:
            precio = lista[1] * 80
        
    return precio

def cargar_datos():

    casamientos[0] = calcular_fact(1, casamientos)
    casamientos[1] = random.randint(30, 300)

    quinces[0] = calcular_fact(2, quinces)
    quinces[1] = random.randint(30, 300)

    cumpleanios[0] = calcular_fact(3, cumpleanios)
    cumpleanios[1] = random.randint(30, 300)

    bautismos[0] = calcular_fact(4, bautismos)
    bautismos[1] = random.randint(30, 300)

    otros[0] = calcular_fact(5, otros)
    otros[1] = random.randint(30, 300)

cargar_eventos()
cargar_datos()

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
        
    elif opcion==2:
        print("Has elegido la opcion 2")
        #proceso de datos para opcion 2
        #impresion de datos para opcion 2
    elif opcion==3:
        print("Has elegido la opcion 3")
        #proceso de datos para opcion 3
        #impresion de datos para opcion 3

    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")
    
    

#Fin del programa
