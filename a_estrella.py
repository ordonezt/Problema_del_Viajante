# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Grupo 1
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP,\
    guardar_resultados, imprimir_camino
from nodos_lib import Nodo, crear_nodos
from copy import copy
import sys
import numpy as np
import time
# import glob

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print('Debe indicar un solo archivo de entrada y a lo sumo el tipo de heuristica [0;3]')
    print('Ejemplo:\n>>> a_estrella.py TSP_IN_01.txt 3')
    exit()

archivo = sys.argv[1]

if len(sys.argv) == 3:
    tipo_heuristica = sys.argv[2]
else:
    tipo_heuristica = 3
    
archivo_path = 'Entradas/' + archivo
print('Procesando ' + archivo_path[-13:] + ' con heuristica {}'.format(tipo_heuristica))

#Leemos el archivo
lineas = leer_lineas_archivo(archivo_path)
n = calc_dim(lineas[0])

#Creamos la matriz de costos
matriz_costos = matrix_TSP(n, lineas)

#Buscamos el minimo costo en todo el mapa
costo_minimo = min(matriz_costos[np.nonzero(matriz_costos)])

#Creamos las n ciudades
ciudades = crear_nodos(n)

#Creamos las listas de ciudades abiertas y cerradas, arrancan vacias
abiertas = []
cerradas = []
nodos_abiertos = 0

#Colocamos la ciudad 0 en abierta y todas las demas son hijas de esta
#asi arranca el algoritmo
ciudad_inicio = ciudades.pop(0)
abiertas.append(ciudad_inicio)

#Descomentar para imprimir
imprimir_camino(ciudad_inicio, mensaje="Agregue a abiertas")

#Empieza a correr el tiempo...
tiempo_inicial = time.perf_counter()

while len(abiertas) != 0:
    #Ordenamos los nodos abiertos por funcion de costo f
    abiertas = sorted(abiertas, key=lambda x: x.f)
    
    #Sacamos la ciudad con menor costo (la )
    ciudad = abiertas.pop(0)
    #Incrementamos la variable de cantidad de nodos abiertos
    nodos_abiertos = nodos_abiertos + 1
    
    #Si la ciudad es la meta, terminamos, imprimo todo
    if(ciudad.is_meta()):
        #Guardo el tiempo de finalizacion
        tiempo_final = time.perf_counter()
        tiempo_transcurrido = tiempo_final - tiempo_inicial
        
        #Imprimo los resultados
        imprimir_camino(ciudad, 'El camino optimo es')
        print('Nodos abiertos: {}'.format(nodos_abiertos))
        print('Tiempo de ejecucion: {} segundos'.format(tiempo_transcurrido))
        print('Velocidad: {} nodos/segundos'.format(nodos_abiertos/tiempo_transcurrido))
        
        #Genero el archivo de salida
        guardar_resultados(archivo_path, ciudad, nodos_abiertos, tiempo_transcurrido, heuristica=tipo_heuristica)
        break
    else:
        #Si la ciudad no era la meta, la mandamos a la lista de caminos cerrados
        cerradas.append(ciudad)
        
        #Obtengo todo el camino actual
        camino = ciudad.get_herencia()
        #Agrego el nodo actual al camino
        camino.append(ciudad)
        #En "camino" tengo todas las ciudades que conforman ese camino

        #Descomentar para imprimir (debug)
        imprimir_camino(ciudad, mensaje="Agregue a cerradas")
        
        #Si el camino ya tiene todas las ciudades agrego como hijo la ciudad meta
        n_recorridas = len(camino)
        if n_recorridas >= n:
            #Creo un nodo de meta
            meta = Nodo(0, meta=True)
            #Se lo agrego como hijo a la ciudad actual
            ciudad.set_hijo(meta, matriz_costos)
            #Agrego este camino a la lista abierta
            abiertas.append(meta)
            
            #Descomentar para imprimir
            imprimir_camino(meta, mensaje="Agregue a abiertas")
        
        #Recorro la lista de ciudades buscando las que no esten en el camino para agregarlas como hijo
        for ciudad_no_visitada in ciudades:
            #Si la ciudad no esta en la herencia la agrego como hijo
            if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
                
                #Hago una copia del hijo y la agrego
                hijo = copy(ciudad_no_visitada)
                
                #Le cargo la heuristica
                if tipo_heuristica == 0:
                    hijo.h = 0
                elif tipo_heuristica == 1:
                    hijo.h = costo_minimo * ((n + 1 - n_recorridas) ** 2) / (n+1)
                elif tipo_heuristica == 2:
                    hijo.h = costo_minimo * (n + 1 - n_recorridas) * n_recorridas / (n+1)
                elif tipo_heuristica == 3:
                    hijo.h = costo_minimo * (n + 1 - n_recorridas)
                else:
                    hijo.h = 0
                
                #Defino la relacion padre-hijo
                ciudad.set_hijo(hijo, matriz_costos)
                
                #Inserto el nodo nuevo en la lista abierta
                abiertas.append(hijo)
            
                #Descomentar para imprimir
                imprimir_camino(hijo, mensaje="Agregue a abiertas")
                #Vuelvo al loop: ordeno la lista abiertas, extraigo el de menor costo, etc...
else:
    print('Error, lista abierta vacia')

# def tsp_resolver_todos():
    
#     archivos = glob.glob('Recursos_de_la_catedra/Datos_no_euclidianos/*.txt')
    
#     tiempo_inicial = time.perf_counter()
    
#     for archivo in archivos:
#         for i in range(1,3+1): #Poner rango de heuristicas que quieras probar
#             if i != 2:
#                 tsp_resolver(archivo, tipo_heuristica=i)

#     tiempo_final = time.perf_counter()
#     tiempo_total = tiempo_final - tiempo_inicial
#     # print('Tiempo total: {}'.format(tiempo_total))
    