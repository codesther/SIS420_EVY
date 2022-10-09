'''Loaiza Alvarez Nicol Noelia
Lopez Camacho Camila Salome
Orosco Sardan Katerine
Rospilloso Ramirez Alex Mauricio
Vallejos Yarhui Esther

Agente basado en objetivos (simple)
Observacion del entorno: Totalmente osbervable porque se ve todo el laberinto
Numero de agentes: Agente Individual porque solo existe un agente en el laberinto
Incertidumbre/Azar: Determinista porque no cambia
Influencia de las acciones: Episodico porque las acciones tomadas no influyen en el resto
Tiempo: Dinámico porque toma las decisiones de dar un paso bajo un determinado tiempo
Tipos de datos: Continuo porque algunos datos se verán alterados durante la ejecución del programa
Conocimiento: Entorno conocido'''

import random
import time

#Creamos las variables que manejaran la creación del laberinto (filas, columnas y paredes)
laberinto = []
numeroFilas = int(input("Introduzca el número de filas "))
numeroColumnas = int(input("Introduzca el número de columnas "))
numeroParedes = int(input("Introduzca el número de paredes "))
contadorMonedas = int(input("Introduzca el numero de monedas "))
espaciosVacios = numeroFilas * numeroColumnas - numeroParedes

#Creamos el laberinto en base a listas, añadiendo paredes que son #
def crearlaberinto():
    for i in range(numeroFilas):
        laberinto.append([])
        for j in range(numeroColumnas):
            laberinto[i].append("#")

#Función dedicada a imprimir el laberinto por filas
def imprimirlaberinto():
    for indice in range(numeroFilas):
        print(laberinto[indice])

#Función que crea un espacio vacio en los bordes del laberinto, representados por un " "
def crearespacioorigen():
    indicecasillaorigen = random.randrange(1, 5)
    if indicecasillaorigen == 1 and espaciosVacios > 0:
        espaciocolumna = random.randrange(0, numeroColumnas-1)
        laberinto[0][espaciocolumna] = " "
        puntox = espaciocolumna
        puntoy = 0
        borrarparedes(puntox,puntoy)
    elif indicecasillaorigen == 2 and espaciosVacios > 0:
        espaciofila = random.randrange(0, numeroFilas - 1)
        laberinto[espaciofila][numeroColumnas-1] = " "
        puntox = numeroColumnas - 1
        puntoy = espaciofila
        borrarparedes(puntox,puntoy)
    elif indicecasillaorigen == 3 and espaciosVacios > 0:
        espaciocolumna = random.randrange(0, numeroColumnas-1)
        laberinto[numeroFilas-1][espaciocolumna] = " "
        puntox = espaciocolumna
        puntoy = numeroFilas - 1
        borrarparedes(puntox,puntoy)
    elif indicecasillaorigen == 4 and espaciosVacios > 0:
        espaciofila = random.randrange(0, numeroFilas-1)
        laberinto[espaciofila][0] = " "
        puntox = 0
        puntoy = espaciofila
        borrarparedes(puntox,puntoy)

#Función que borra las paredes a partir del primer punto que creamos, haciendo un camino seguido, reemplazando las paredes # por " "
def borrarparedes(puntox,puntoy):
    espaciosVacios = numeroFilas * numeroColumnas - numeroParedes
    while espaciosVacios > 1:
        direccion = random.randrange(1,5)
        if direccion == 1:
            puntoxauxiliar = puntox + 1
            if puntoxauxiliar <= numeroColumnas - 1:
                puntox = puntoxauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
        elif direccion == 2:
            puntoyauxiliar = puntoy + 1
            if puntoyauxiliar <= numeroFilas - 1:
                puntoy = puntoyauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
        elif direccion == 3:
            puntoxauxiliar = puntox - 1
            if puntoxauxiliar >= 0:
                puntox = puntoxauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
        elif direccion == 4:
            puntoyauxiliar = puntoy - 1
            if puntoyauxiliar >= 0:
                puntoy = puntoyauxiliar
                if laberinto[puntoy][puntox] == "#":
                    laberinto[puntoy][puntox] = " "
                    espaciosVacios = espaciosVacios - 1
    crearmoneda()
    generarcaracter()

#Función que crea el caracter en un punto del laberinto, representado por *
def generarcaracter():
    puntogenerado = False
    while puntogenerado == False:
        puntox = random.randrange(0,numeroColumnas)
        puntoy = random.randrange(0,numeroFilas)
        if laberinto[puntoy][puntox] == " ":
            laberinto[puntoy][puntox] = "*"
            puntogenerado = True
    caminarcaracter(puntox,puntoy)

#Función que hará que el caracter se mueva por los espacios vacíos permitidos en base a un número de pasos que le daremos
def caminarcaracter(puntoxcaracter,puntoycaracter):
    segundos = 0
    monedasRecogidas = 0
    while monedasRecogidas < contadorMonedas:
        direccion = random.randrange(1, 5)
        if direccion == 1:
            puntoxcaracterauxiliar = puntoxcaracter + 1
            if puntoxcaracterauxiliar <= numeroColumnas - 1:
                if laberinto[puntoycaracter][puntoxcaracterauxiliar] == " " or laberinto[puntoycaracter][puntoxcaracterauxiliar] == "o":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    if laberinto[puntoycaracter][puntoxcaracterauxiliar] == "o":
                        monedasRecogidas = monedasRecogidas + 1
                    puntoxcaracter = puntoxcaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print(" ")
                    imprimirlaberinto()
        if direccion == 2:
            puntoycaracterauxiliar = puntoycaracter + 1
            if puntoycaracterauxiliar <= numeroFilas - 1:
                if laberinto[puntoycaracterauxiliar][puntoxcaracter] == " " or laberinto[puntoycaracterauxiliar][puntoxcaracter] == "o":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    if laberinto[puntoycaracterauxiliar][puntoxcaracter] == "o":
                        monedasRecogidas = monedasRecogidas + 1
                    puntoycaracter = puntoycaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print(" ")
                    imprimirlaberinto()
        if direccion == 3:
            puntoxcaracterauxiliar = puntoxcaracter - 1
            if puntoxcaracterauxiliar >= 0:
                if laberinto[puntoycaracter][puntoxcaracterauxiliar] == " " or laberinto[puntoycaracter][puntoxcaracterauxiliar] == "o":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    if laberinto[puntoycaracter][puntoxcaracterauxiliar] == "o":
                        monedasRecogidas = monedasRecogidas + 1
                    puntoxcaracter = puntoxcaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print(" ")
                    imprimirlaberinto()
        if direccion == 4:
            puntoycaracterauxiliar = puntoycaracter - 1
            if puntoycaracterauxiliar >= 0:
                if laberinto[puntoycaracterauxiliar][puntoxcaracter] == " " or laberinto[puntoycaracterauxiliar][puntoxcaracter] == "o":
                    laberinto[puntoycaracter][puntoxcaracter] = " "
                    if laberinto[puntoycaracterauxiliar][puntoxcaracter] == "o":
                        monedasRecogidas = monedasRecogidas + 1
                    puntoycaracter = puntoycaracterauxiliar
                    laberinto[puntoycaracter][puntoxcaracter] = "*"
                    print(" ")
                    imprimirlaberinto()
        segundos = segundos + 0.8
        time.sleep(0.8)
    print(segundos)

#Crea las monedas objetivo en base a un valor dado por el usuario
def crearmoneda():
    global contadorMonedas
    contadorMonedasAux = contadorMonedas
    while contadorMonedasAux > 0:
        puntoxmoneda = random.randrange(0,numeroColumnas)
        puntoymoneda = random.randrange(0,numeroFilas)
        if laberinto[puntoymoneda][puntoxmoneda] == " ":
            laberinto[puntoymoneda][puntoxmoneda] = "o"
            contadorMonedasAux = contadorMonedasAux - 1


crearlaberinto()
crearespacioorigen()
