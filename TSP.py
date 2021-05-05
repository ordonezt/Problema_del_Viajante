# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Usuario
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP, guardar_resultados
from nodos_lib import Nodo, crear_nodos
from copy import copy
from random import random
import numpy as np
import time
import glob

def tsp_resolver(archivo_path, tipo_heuristica=3):
    
    print('Procesando ' + archivo_path[-13:] + ' con heuristica {}'.format(tipo_heuristica))
    
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
            # print(archivo_path)
            # print('El camino es: {}'.format(camino_id))
            # print('El costo fue: {}'.format(ciudad.g))
            # print('Nodos abiertos: {}'.format(nodos_abiertos))
            # print('Tiempo de ejecucion: {} segundos'.format(tiempo_transcurrido))
            # print('Velocidad: {} nodos/segundos'.format(nodos_abiertos/tiempo_transcurrido))
            
            guardar_resultados(archivo_path, ciudad, nodos_abiertos, tiempo_transcurrido, heuristica=tipo_heuristica)
            break
        else:
            #La metemos en la lista de ciudades cerradas
            cerradas.append(ciudad)
            
            #Obtengo todo el camino actual
            camino = ciudad.get_herencia()
            camino_cerrado = copy(camino)
            #Agrego el nodo actual al camino
            camino.append(ciudad)
            
            # camino_id = []
            # for ciudad_i in camino_cerrado:
            #     camino_id.append(ciudad_i.identificador)
            # camino_id.reverse()
            # camino_id.append(ciudad.identificador)
            # print("Agregue a cerradas lo siguiente", camino_id, "con un costo de {}".format(ciudad.get_costo()))
            
            #Si el camino ya tiene todas las ciudades agrego como hijo la meta
            n_recorridas = len(camino)
            if n_recorridas >= n:
                meta = Nodo(0, meta=True)
                ciudad.set_hijo(meta, matriz_costos)
                abiertas.append(meta)
                
                # camino_meta = meta.get_herencia()
                # camino_id = []
                # for ciudad_i in camino_meta:
                #     camino_id.append(ciudad_i.identificador)
                # camino_id.reverse()
                # camino_id.append(meta.identificador)
                # print("Agregue a abiertas lo siguiente", camino_id, "con un costo de {}".format(meta.get_costo()))
            
            #Recorro todas las ciudades para agregar a los hijos queno esten en el camino
            for ciudad_no_visitada in ciudades:
                #Si la ciudad no esta en la herencia es un hijo
                if not any(nodo.identificador == ciudad_no_visitada.identificador for nodo in camino):
                    #Hago una copia del hijo
                    hijo = copy(ciudad_no_visitada)
                    
                    #Le cargo la heuristica
                    if tipo_heuristica == 0:
                        hijo.h = 0
                    elif tipo_heuristica == 1:
                        hijo.h = costo_minimo * ((n - n_recorridas + 1) ** 2) / (n+1)
                    elif tipo_heuristica == 2:
                        hijo.h = costo_minimo * (n - n_recorridas + 1) * n_recorridas / (n+1)
                    elif tipo_heuristica == 3:
                        hijo.h = costo_minimo * (n - n_recorridas + 1)
                    else:
                        hijo.h = 0
                    
                    #Defino la relacion padre-hijo
                    ciudad.set_hijo(hijo, matriz_costos)
                    
                    #Inserto el nodo nuevo en la lista abierta
                    abiertas.append(hijo)
                
                    # camino_id = []
                    # camino_hijo = hijo.get_herencia()
                    # for ciudad_i in camino_hijo:
                    #     camino_id.append(ciudad_i.identificador)
                    # camino_id.reverse()
                    # camino_id.append(hijo.identificador)
                    #print("Agregue a abiertas lo siguiente", camino_id, "con un costo de {}".format(hijo.get_costo()))
    else:
        print('Error, lista abierta vacia')

def tsp_resolver_todos():
    
    archivos = glob.glob('Recursos_de_la_catedra/Datos_no_euclidianos/*.txt')
    
    tiempo_inicial = time.perf_counter()
    
    for archivo in archivos:
        for i in range(1,3+1): #Poner rango que 
            if i != 2:
                tsp_resolver(archivo, tipo_heuristica=i)

    tiempo_final = time.perf_counter()
    tiempo_total = tiempo_final - tiempo_inicial
    # print('Tiempo total: {}'.format(tiempo_total))
    