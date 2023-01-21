import numpy as np 

import os

os.system("cls")


asientos=np.empty([6,33], dtype="U200")

registro_clientes = np.empty([6,33], dtype="int")




def llenarAsientos():

    for fila in range(0,6):

        for columna in range(0,33):

            asientos [fila,columna] = "O"

                

def mostrarUbicaciones():

    for fila in range(0,6):

        for columna in range(0,33):

            print(asientos[fila, columna], end=" ")

        print()

        

    

def comprarPasajes():

    print("\n--PRECIOS DE ASIENTOS--\n")

    print("1) No reclina : $50.000")

    print("2) Asiento comun : $60.000")

    print("3) Espacio adicional para piernas: $80.000")

    print("4) Atras ")

    opcion_precios = int(input("\nIngrese opcion a elegir : "))

    

    if opcion_precios == 1 :

        print("\n ingrese el número de asiento a comprar : ")

        nro_asiento = int(input())

        contador = 1

        for fila in range(0,6):

            for columna in range(0,33):

                #preguntamos si el contador es igual a la cabaña que quiero comprar

                if contador  == nro_asiento :

                    #pregunto si ya está reservada

                    if asientos[fila, columna] == "O":

                        print("asiento disponible!\n")

                        registro_clientes[fila, columna] = int(input("ingrese su rut para completar el registro : "))

                        asientos[fila, columna] = "X"

                        print("\nCompra exitosa")

                    else:

                        print("\nAsiento ocupado!")

                contador += 1  



    if opcion_precios == 2 :

        print("\n ingrese el número de asiento a comprar : ")

        nro_asiento = int(input())

        contador = 1

        for fila in range(0,6):

            for columna in range(0,33):

                #preguntamos si el contador es igual a la cabaña que quiero comprar

                if contador  == nro_asiento :

                    #pregunto si ya está reservada

                    if asientos[fila, columna] == "O":

                        print("asiento disponible!\n")

                        registro_clientes[fila, columna] = int(input("ingrese su rut para completar el registro : "))

                        asientos[fila, columna] = "X"

                        print("\nCompra exitosa")

                    else:

                        print("\nAsiento ocupado!")

                contador += 1

    if opcion_precios == 3 :

        print("\n ingrese el número de asiento a comprar : ")

        nro_asiento = int(input())

        contador = 1

        for fila in range(0,6):

            for columna in range(0,33):

                #preguntamos si el contador es igual a la cabaña que quiero comprar

                if contador  == nro_asiento :

                    #pregunto si ya está reservada

                    if asientos[fila, columna] == "O":

                        print("asiento disponible!\n")

                        registro_clientes[fila, columna] = int(input("ingrese su rut para completar el registro : "))

                        asientos[fila, columna] = "X"

                        print("\nCompra exitosa")

                    else:

                        print("\nAsiento ocupado!")

                contador += 1

    if opcion_precios ==4 :

        print()

def verListado():

    #ordeno el arreglo con la funcion "sorted" y con el ciclo for, puedo recorrer ese arreglo

    for  fila  in sorted(registro_clientes):

        for columna in sorted(registro_clientes):

            print(asientos[0])



        

    







opcion = 0

llenarAsientos()

#menú

while opcion != 7 :

    print("------\nRESERVA DE PASAJES \n------")

    print("1) Comprar pasajes")

    print("2) Mostrar ubicaciones disponibles")

    print("3) Ver listado de pasajeros")

    print("4) Buscar pasajero")

    print("5) Reasignar asiento")

    print("6) Mostrar ganancias totales")

    print("7) Salir ")

    try:

        opcion = int(input())

        if opcion in (1,2,3,4,5,6,7):

            if opcion == 1:

                comprarPasajes()

            if opcion == 2:

                mostrarUbicaciones()

            if opcion == 3:

                verListado()

            if opcion == 4:

                buscarPasajero()

            if opcion == 5:

                reasignarAsiento()

            if opcion == 6:

                mostrarGnanacias()

            if opcion == 7:

                print("hasta pronto")

                break

    except ValueError:

        print("ingrese solo números")











