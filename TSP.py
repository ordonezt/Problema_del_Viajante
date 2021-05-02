# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Usuario
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from nodos_lib import Nodo, crear_nodos
from copy import copy
from random import random
import numpy as np
import time
import glob

def tsp_resolver(archivo_path):
       
    #Leemos el archivo
    lineas = leer_lineas_archivo(archivo_path)
    n = calc_dim(lineas[0])
    
    #Creamos la matriz de costos
    matriz_costos = matrix_TSP(n, lineas)
    
    costo_minimo = min(matriz_costos[np.nonzero(matriz_costos)])
    
    #Creamos las ciudades
    ciudades = crear_nodos(n)
    
    #Creamos las listas de ciudades abiertas y cerradas, arrancan vacias
    abiertas = []
    cerradas = []
    
    #Colocamos la ciudad 0 en abierta y todas las demas son hijas de esta
    #asi arranca el algoritmo
    ciudad_inicio = ciudades.pop(0)
    
    abiertas.append(ciudad_inicio)
    
    nodos_abiertos = 0
    
    tiempo_inicial = time.perf_counter()
    
    while len(abiertas) != 0:
        #Ordenamos los nodos abiertos por funcion de costo
        abiertas = sorted(abiertas, key=lambda x: x.f)
        
        #Sacamos la ciudad con menor costo
        ciudad = abiertas.pop(0)
        #Incrementamos la variable de cantidad de nodos abiertos
        nodos_abiertos = nodos_abiertos + 1
        
        #Si la ciudad es la meta, terminamos, imprimo todo
        if(ciudad.is_meta()):
            tiempo_final = time.perf_counter()
            tiempo_transcurrido = tiempo_final - tiempo_inicial
            camino = ciudad.get_herencia()
            camino_id = []
            for ciudad_i in camino:
                camino_id.append(ciudad_i.identificador)
            camino_id.reverse()
            camino_id.append(ciudad.identificador)
            print(archivo_path)
            print('El camino es: {}'.format(camino_id))
            print('El costo fue: {}'.format(ciudad.g))
            print('Nodos abiertos: {}'.format(nodos_abiertos))
            print('Tiempo de ejecucion: {} segundos'.format(tiempo_transcurrido))
            print('Velocidad: {} nodos/segundos'.format(nodos_abiertos/tiempo_transcurrido))
            break
        else:
            #La metemos en la lista de ciudades cerradas
            cerradas.append(ciudad)
            
            #Obtengo todo el camino actual
            camino = ciudad.get_herencia()
            #Agrego el nodo actual al camino
            camino.append(ciudad)
            
            #Si el camino ya tiene todas las ciudades agrego como hijo la meta
            n_recorridas = len(camino)
            if n_recorridas >= n:
                meta = Nodo(0, meta=True)
                ciudad.set_hijo(meta, matriz_costos)
                abiertas.append(meta)
            
            #Recorro todas las ciudades para agregar a los hijos queno esten en el camino
            for ciudad_no_visitada in ciudades:
                #Si la ciudad no esta en la herencia es un hijo
                if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
                    #Hago una copia del hijo
                    hijo = copy(ciudad_no_visitada)
                    #Le cargo la heuristica
                    hijo.h = costo_minimo * (n - n_recorridas + 1)#((n - n_recorridas + 1) ** 2) / (n+1)#(n - n_recorridas + 1) * n_recorridas / (n+1)
                    #Defino la relacion padre-hijo
                    ciudad.set_hijo(hijo, matriz_costos)
                    
                    #Inserto el nodo nuevo en la lista abierta
                    abiertas.append(hijo)
            

def tsp_resolver_todos():
    archivos = glob.glob('Recursos_de_la_catedra/Datos_no_euclidianos/*.txt')
    
    tiempo_inicial = time.perf_counter()
    
    for archivo in archivos:
        print('#######################################')
        print('#######################################')
        tsp_resolver(archivo)
    
    print('#######################################')
    print('#######################################\n')
    tiempo_final = time.perf_counter()
    
    tiempo_total = tiempo_final - tiempo_inicial
    
    print('Tiempo total: {}'.format(tiempo_total))
    
# #Para correr el algoritmo como script descomentar
# archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_04.txt'

# #Leemos el archivo
# lineas = leer_lineas_archivo(archivo_path)
# n = calc_dim(lineas[0])

# #Creamos la matriz de costos
# matriz_costos = matrix_TSP(n, lineas)

# costo_minimo = min(matriz_costos[np.nonzero(matriz_costos)])

# #Creamos las ciudades
# ciudades = crear_nodos(n)

# #Creamos las listas de ciudades abiertas y cerradas, arrancan vacias
# abiertas = []
# cerradas = []

# #Asignar valor heuristico a cada ciudad
# #ToDo

# #Colocamos la ciudad 0 en abierta y todas las demas son hijas de esta
# #asi arranca el algoritmo
# ciudad_inicio = ciudades.pop(0)
# # for ciudad in ciudades:
# #     ciudad_inicio.set_hijo(ciudad)

# abiertas.append(ciudad_inicio)

# nodos_abiertos = 0

# tiempo_inicial = time.perf_counter()

# while len(abiertas) != 0:
#     #Ordenamos los nodos abiertos por funcion de costo
#     #abiertas_costos = sorted(abiertas, key=lambda x: x.f)
#     #Por las dudas que haya costos iguales ordenamos por identificador
#     #abiertas = sorted(abiertas_costos, key=lambda x: x.identificador)
#     abiertas = sorted(abiertas, key=lambda x: x.f)
    
#     #Sacamos la ciudad con menor costo
#     ciudad = abiertas.pop(0)
#     nodos_abiertos = nodos_abiertos + 1
    
#     if(ciudad.is_meta()):
#         tiempo_final = time.perf_counter()
#         tiempo_transcurrido = tiempo_final - tiempo_inicial
#         camino = ciudad.get_herencia()
#         camino_id = []
#         for ciudad_i in camino:
#             camino_id.append(ciudad_i.identificador)
#         camino_id.reverse()
#         camino_id.append(ciudad.identificador)
#         print(archivo_path)
#         print('El camino es: {}'.format(camino_id))
#         print('El costo fue: {}'.format(ciudad.g))
#         print('Nodos abiertos: {}'.format(nodos_abiertos))
#         print('Tiempo de ejecucion: {} segundos'.format(tiempo_transcurrido))
#         print('Velocidad: {} nodos/segundos'.format(nodos_abiertos/tiempo_transcurrido))
#         break
#     else:
#         #La metemos en la lista de ciudades cerradas
#         cerradas.append(ciudad)
        
#         #Obtengo todo el camino actual
#         camino = ciudad.get_herencia()
#         camino.append(ciudad)
        
#         #Si el camino ya tiene todas las ciudades agrego como hijo la meta
#         n_recorridas = len(camino)
#         if n_recorridas >= n:
#             meta = Nodo(0, meta=True)
#             ciudad.set_hijo(meta, matriz_costos)
#             abiertas.append(meta)
        
#         #Recorro todas las ciudades para agregar a los hijos queno esten en el camino
#         for ciudad_no_visitada in ciudades:
#             #Si la ciudad no esta en la herencia es un hijo
#             if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
#                 hijo = copy(ciudad_no_visitada)
#                 hijo.h = (n - n_recorridas) * costo_minimo
#                 ciudad.set_hijo(hijo, matriz_costos)
                
#                 #Recorro la lista para ver si el nodo no esta en abiertas o si esta con mayor costo
#                 hay_que_insertar = True
#                 # for i, ciudad_abierta in enumerate(abiertas):
#                 #     if ciudad_abierta.identificador == hijo.identificador:
#                 #         if ciudad_abierta.get_costo() >= hijo.get_costo():
#                 #             hay_que_insertar = True
#                 #             #abiertas.pop(i)                           
#                 #         else:
#                 #             hay_que_insertar = False
                
#                 if hay_que_insertar == True:
#                     abiertas.append(hijo)
        