# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Usuario
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from nodos_lib import Nodo, crear_nodos
from copy import copy
#from python_tsp.exact import solve_tsp_dynamic_programming

def tsp_resolver(archivo_path):
       
    lineas = leer_lineas_archivo(archivo_path)
    n = calc_dim(lineas[0])
    
    #Creamos la matriz de costos
    matriz_costos = matrix_TSP(n, lineas)
    
    heuristicas = [0 for i in range(n)]
    
    #Creamos las ciudades
    ciudades = crear_nodos(n, heuristicas)
    
    #Creamos las listas de ciudades abiertas y cerradas, arrancan vacias
    abiertas = []
    cerradas = []
    
    #Asignar valor heuristico a cada ciudad
    #ToDo
    
    #Colocamos la ciudad 0 en abierta y todas las demas son hijas de esta
    #asi arranca el algoritmo
    ciudad_inicio = ciudades.pop(0)
    # for ciudad in ciudades:
    #     ciudad_inicio.set_hijo(ciudad)
    
    abiertas.append(ciudad_inicio)
    
    nodos_abiertos = 0
    
    while len(abiertas) != 0:
        #Ordenamos los nodos abiertos por funcion de costo
        abiertas_costos = sorted(abiertas, key=lambda x: x.f)
        #Por las dudas que haya costos iguales ordenamos por identificador
        abiertas = sorted(abiertas_costos, key=lambda x: x.identificador)
        
        #Sacamos la ciudad con menor costo
        ciudad = abiertas.pop(0)
        nodos_abiertos = nodos_abiertos + 1
        
        if(ciudad.is_meta()):
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
            break
        else:
            #La metemos en la lista de ciudades cerradas
            cerradas.append(ciudad)
            
            #Obtengo todo el camino actual
            camino = ciudad.get_herencia()
            camino.append(ciudad)
            
            #Si el camino ya tiene todas las ciudades agrego como hijo la meta
            if len(camino) >= n:
                meta = Nodo(0, meta=True)
                ciudad.set_hijo(meta, matriz_costos)
                abiertas.append(meta)
            
            #Recorro todas las ciudades para agregar a los hijos queno esten en el camino
            for ciudad_no_visitada in ciudades:
                #Si la ciudad no esta en la herencia es un hijo
                if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
                    hijo = copy(ciudad_no_visitada)
                    
                    ciudad.set_hijo(hijo, matriz_costos)
                    
                    #Recorro la lista para ver si el nodo no esta en abiertas o si esta con mayor costo
                    hay_que_insertar = True
                    for i, ciudad_abierta in enumerate(abiertas):
                        if ciudad_abierta.identificador == hijo.identificador:
                            if ciudad_abierta.get_costo() > hijo.get_costo():
                                hay_que_insertar = True
                                abiertas.pop(i)                           
                            else:
                                hay_que_insertar = False
                    
                    if hay_que_insertar == True:
                        abiertas.append(hijo)
            


# #Para correr el algoritmo como script descomentar
# archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_01.txt'

# #Leemos el archivo
# lineas = leer_lineas_archivo(archivo_path)
# n = calc_dim(lineas[0])

# #Creamos la matriz de costos
# matriz_costos = matrix_TSP(n, lineas)

# heuristicas = [0 for i in range(n)]

# #Creamos las ciudades
# ciudades = crear_nodos(n, heuristicas)

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

# while len(abiertas) != 0:
#     #Ordenamos los nodos abiertos por funcion de costo
#     abiertas_costos = sorted(abiertas, key=lambda x: x.f)
#     #Por las dudas que haya costos iguales ordenamos por identificador
#     abiertas = sorted(abiertas_costos, key=lambda x: x.identificador)
    
#     #Sacamos la ciudad con menor costo
#     ciudad = abiertas.pop(0)
#     nodos_abiertos = nodos_abiertos + 1
    
#     if(ciudad.is_meta()):
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
#         break
#     else:
#         #La metemos en la lista de ciudades cerradas
#         cerradas.append(ciudad)
        
#         #Obtengo todo el camino actual
#         camino = ciudad.get_herencia()
#         camino.append(ciudad)
        
#         #Si el camino ya tiene todas las ciudades agrego como hijo la meta
#         if len(camino) >= n:
#             meta = Nodo(0, meta=True)
#             ciudad.set_hijo(meta, matriz_costos)
#             abiertas.append(meta)
        
#         #Recorro todas las ciudades para agregar a los hijos queno esten en el camino
#         for ciudad_no_visitada in ciudades:
#             #Si la ciudad no esta en la herencia es un hijo
#             if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
#                 hijo = copy(ciudad_no_visitada)
                
#                 ciudad.set_hijo(hijo, matriz_costos)
                
#                 #Recorro la lista para ver si el nodo no esta en abiertas o si esta con mayor costo
#                 hay_que_insertar = True
#                 for i, ciudad_abierta in enumerate(abiertas):
#                     if ciudad_abierta.identificador == hijo.identificador:
#                         if ciudad_abierta.get_costo() > hijo.get_costo():
#                             hay_que_insertar = True
#                             abiertas.pop(i)                           
#                         else:
#                             hay_que_insertar = False
                
#                 if hay_que_insertar == True:
#                     abiertas.append(hijo)
        