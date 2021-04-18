# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Usuario
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from nodos_lib import Nodo, crear_nodos
from copy import copy
#from python_tsp.exact import solve_tsp_dynamic_programming


# filename="Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_01.txt"

# lineas=leer_lineas_archivo(filename)


# #print((lineas[0]))
# #print((lineas[1]))
# #print((lineas[2]))

# n=calc_dim(lineas[0])

# # print(len(lineas))

# # print(lineas)
      
# matrix=matrix_TSP(n,lineas)

# print(matrix)


# #permutation, distance = solve_tsp_dynamic_programming(matrix)

# #print("Camino")
# #print(permutation)


# def tsp_resolver(archivo_path):
    
# #     # Pasos del algoritmo A*:
# #     #     Armar 2 listas, una vacia y una cerrada
# #     #     Asignarle todos los nodos como hijos al nodo de inicio
# #     #     Ponemos el nodo de inicio en la lista abierta
        
# #     #     Mientras que haya nodos en la lista abierta:
# #     #         Ordenar la lista abierta de menor (costo) a mayor
# #     #         Agarrar el de menor costo y pasarlo a la lista cerrada
            
# #     #         Era el nodo destino?
# #     #             No:
# #     #                 Pasar todos sus hijos a la lista abierta si es que no estan
# #     #             Si:
# #     #                 Terminar
    
#     #Leemos el archivo
#     lineas = leer_lineas_archivo(archivo_path)
#     n = calc_dim(lineas[0])
    
#     #Creamos la matriz de costos
#     matriz_costos = matrix_TSP(n, lineas)
    
#     #Creamos las ciudades
#     ciudades = crear_nodos(n)
    
#     #Creamos las listas de ciudades abiertas y cerradas, arrancan vacias
#     abiertas = []
#     cerradas = []
    
#     #Asignar valor heuristico a cada ciudad
#     #ToDo
    
#     #Colocamos la ciudad 0 en abierta y todas las demas son hijas de esta
#     #asi arranca el algoritmo
#     ciudad_inicio = ciudades.pop(0)
#     # for ciudad in ciudades:
#     #     ciudad_inicio.set_hijo(ciudad)
    
#     abiertas.append(ciudad_inicio)
    
#     while len(abiertas) != 0:
#         #Ordenamos los nodos abiertos por funcion de costo
#         abiertas_costos = sorted(abiertas, key=lambda x: x.f)
#         #Por las dudas que haya costos iguales ordenamos por identificador
#         abiertas = sorted(abiertas_costos, key=lambda x: x.identificador)
        
#         #Sacamos la ciudad con menor costo
#         ciudad = abiertas.pop(0)
        
#         if(ciudad.is_meta()):
#             print('Terminamos')
#             break
#         else:
#             #La metemos en la lista de ciudades cerradas
#             cerradas.append(ciudad)
            
#             #Obtengo todo el camino actual
#             camino = ciudad.get_herencia()
#             camino.append(ciudad)
            
#             #Recorro todas las ciudades para agregar a los hijos
#             for ciudad_no_visitada in ciudades:
#                 #Si la ciudad no esta en la herencia es un hijo
#                 if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
#                     print('hijo')
#                     ciudad.set_hijo(ciudad_no_visitada)
            


#Para correr el algoritmo como script descomentar
archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_01.txt'

#Leemos el archivo
lineas = leer_lineas_archivo(archivo_path)
n = calc_dim(lineas[0])

#Creamos la matriz de costos
matriz_costos = matrix_TSP(n, lineas)

#Creamos las ciudades
ciudades = crear_nodos(n)

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

while len(abiertas) != 0:
    #Ordenamos los nodos abiertos por funcion de costo
    abiertas_costos = sorted(abiertas, key=lambda x: x.f)
    #Por las dudas que haya costos iguales ordenamos por identificador
    abiertas = sorted(abiertas_costos, key=lambda x: x.identificador)
    
    #Sacamos la ciudad con menor costo
    ciudad = abiertas.pop(0)
    
    if(ciudad.is_meta()):
        print('Terminamos')
        break
    else:
        #La metemos en la lista de ciudades cerradas
        cerradas.append(ciudad)
        
        #Obtengo todo el camino actual
        camino = ciudad.get_herencia()
        camino.append(ciudad)
        
        #Recorro todas las ciudades para agregar a los hijos
        for ciudad_no_visitada in ciudades:
            #Si la ciudad no esta en la herencia es un hijo
            if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
                print('hijo')
                ciudad.set_hijo(copy(ciudad_no_visitada))
