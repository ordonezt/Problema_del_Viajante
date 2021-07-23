# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Grupo 1
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP,\
    guardar_resultados, imprimir_camino, SA_res
from nodos_lib import Nodo, crear_ciudades, calcular_costo_camino
import sys
import time
import matplotlib.pyplot as plt

# import glob
estimacion_recocido_simulado = True

if len(sys.argv) != 4:
    print('Debe indicar un solo archivo de entrada y las configuraciones')
    print('Ejemplo:\npython a_estrella.py TSP_IN_01.txt 4 si')
    exit()

archivo = sys.argv[1]


tipo_heuristica = int(sys.argv[2])

aproximacion = sys.argv[3]

if aproximacion == 'si':
    msg_aprox = ' y con aproximacion'
else:
    msg_aprox = ''
    
archivo_path = 'Entradas/' + archivo
print('Procesando ' + archivo_path[-13:] + ' con heuristica {}'.format(tipo_heuristica) + msg_aprox)

#Leemos el archivo
lineas = leer_lineas_archivo(archivo_path)
n = calc_dim(lineas[0])

#Creamos la matriz de costos
matriz_costos = matrix_TSP(n, lineas)

#Creamos las n ciudades
ciudades = crear_ciudades(n)

#Si el usuario asi lo selecciono calculamos un costo aproximado
if aproximacion == 'si':
    if estimacion_recocido_simulado == False:
        #Camino aproximado: 0 --> 1 --> 2 --> 3 --> ... --> n-1 --> n --> 0
        camino_aproximado = ciudades
        camino_aproximado.append(camino_aproximado[0])
        costo_aproximado = calcular_costo_camino(camino_aproximado, matriz_costos)
    else:
        #Camino aproximado: Recocido simulado del mapa
        costo_aproximado = SA_res(int(archivo[-6:-4]))
    
#Creamos las listas de nodos abiertos y cerrados, arrancan vacias
abiertos = []
cerrados = []
nodos_abiertos = 0

#Colocamos la ciudad 0 en el nodo de inicio
ciudad_inicio = ciudades.pop(0)
nodo_inicial = Nodo(ciudad_inicio)

#Agregamos el nodo de inicio a la lista de nodos abiertos (es el unico hasta el momento)
abiertos.append(nodo_inicial)

#Descomentar para imprimir
imprimir_camino(nodo_inicial, mensaje="Agregue a abiertos")

#Empieza a correr el tiempo...
tiempo_inicial = time.perf_counter()

#Variables para los graficos y post analisis, ignorar
vector_tiempos = []
vector_nodos_abiertos = []
vector_velocidades = []
vector_tamanio_abiertos = []

#Mientras la lista de nodos abiertos no este vacia estamos bien
while len(abiertos) != 0:
    #Ordenamos los nodos abiertos por funcion de costo f
    abiertos = sorted(abiertos, key=lambda x: x.f)
    
    #Sacamos el nodo con menor costo
    nodo = abiertos.pop(0)
    #Incrementamos la variable de cantidad de nodos abiertos
    nodos_abiertos = nodos_abiertos + 1
    
    #Variables para los graficos y post analisis, ignorar
    tiempo_parcial = time.perf_counter() - tiempo_inicial
    velocidad = nodos_abiertos / tiempo_parcial
    tamanio_abiertos = sys.getsizeof(abiertos)
    vector_tiempos.append(tiempo_parcial)
    vector_nodos_abiertos.append(nodos_abiertos)
    vector_tamanio_abiertos.append(tamanio_abiertos)
    if nodos_abiertos != 1:
        vector_velocidades.append(velocidad)
    
    #Si el nodo es meta, terminamos, imprimo todo
    if(nodo.is_meta()):
        #Guardo el tiempo de finalizacion
        tiempo_final = time.perf_counter()
        tiempo_transcurrido = tiempo_final - tiempo_inicial
        
        #Imprimo los resultados
        imprimir_camino(nodo, 'El camino optimo es')
        print('Nodos abiertos: {}'.format(nodos_abiertos))
        print('Tiempo de ejecucion: {} segundos'.format(tiempo_transcurrido))
        print('Velocidad: {} nodos/segundos'.format(nodos_abiertos/tiempo_transcurrido))
        
        #Genero el archivo de salida
        guardar_resultados(archivo_path, nodo, nodos_abiertos, tiempo_transcurrido, aproximacion, heuristica=tipo_heuristica)
        break
    else:
        #Si el nodo no era meta, lo mandamos a la lista de nodos cerrados
        cerrados.append(nodo)
        
        #Obtengo todo el camino actual
        camino = nodo.get_herencia()
        camino.append(nodo.ciudad_cabecera)
        #En "camino" tengo todas las ciudades que conforman ese nodo

        #Descomentar para imprimir (debug)
        imprimir_camino(nodo, mensaje="Agregue a cerrados")
        
        #Si el camino ya tiene todas las ciudades... genero el nodo meta
        n_recorridas = len(camino)
        if n_recorridas >= n:
            #Creo un nodo de meta
            meta = Nodo(0, meta=True)
            #Se lo agrego como hijo al nodo actual
            nodo.set_hijo(meta, matriz_costos, tipo_heuristica)
            #Agrego este nodo a la lista abierta
            abiertos.append(meta)
            
            #Descomentar para imprimir
            imprimir_camino(meta, mensaje="Agregue a abiertos")
        
        #Recorro la lista de ciudades buscando las que no esten en el camino bajo analisis para generar nodos hijos
        for ciudad_no_visitada in ciudades:
            #Si la ciudad no esta en el camino... Tenemos un nuevo nodo que generar
            if not any(ciudad_no_visitada == ciudad_del_camino for ciudad_del_camino in camino):
                
                #Hago un nuevo nodo cuya ciudad cabecera es una ciudad no visitada por el nodo bajo analisis
                hijo = Nodo(ciudad_no_visitada)
                
                #Defino la relacion padre-hijo
                nodo.set_hijo(hijo, matriz_costos, tipo_heuristica)
                
                #Si el usuario eligio usar la aproximacion... la usamos
                if aproximacion == 'si':
                    #Si el costo del nodo generado es menor al aproximado lo validamos, si no, se descarta
                    if hijo.get_costo() <= costo_aproximado:
                        #Inserto el nodo nuevo en la lista abierta
                        abiertos.append(hijo)
                        #Descomentar para imprimir
                        imprimir_camino(hijo, mensaje="Agregue a abiertos")
                    else:
                        print("No hace falta agregar, costo actual: {}, costo aprox: {}".format(hijo.get_costo(), costo_aproximado))
                else:
                    #Inserto el nodo nuevo en la lista abierta
                    abiertos.append(hijo)
                    #Descomentar para imprimir
                    imprimir_camino(hijo, mensaje="Agregue a abiertos")
            
                #Vuelvo al loop: ordeno la lista abiertos, extraigo el de menor costo, etc...
else:
    #Si la lista de nodos abiertos se vacio sin encontrar un resultado significa que el
    #mapa no tiene solucion o el algoritmo no funciona correctamente
    print('Error, lista abierta vacia')

if aproximacion == 'si':
    msg_aprox = 'mejorado_'
else:
    msg_aprox = ''
    
#Graficamos Tiempo vs Nodos abiertos
plt.figure()
plt.plot(vector_nodos_abiertos, vector_tiempos)
plt.xlabel('Nodos abiertos')
plt.ylabel('Tiempo [s]')
plt.title(archivo + ' h{}'.format(tipo_heuristica) + ' ' + msg_aprox[0:-1])
plt.savefig('Resultados/' + archivo[0:9] + '_{}_'.format(tipo_heuristica) + msg_aprox +'tiempo' + '.png')
    
#Graficamos Velocidad vs Nodos abiertos
plt.figure()
plt.plot(vector_nodos_abiertos[1:], vector_velocidades)
plt.xlabel('Nodos abiertos')
plt.ylabel('Velocidad [nodos/segundo]')
plt.title(archivo + ' h{}'.format(tipo_heuristica) + ' ' + msg_aprox[0:-1])
plt.savefig('Resultados/' + archivo[0:9] + '_{}_'.format(tipo_heuristica) + msg_aprox +'velocidad' + '.png')

#Graficamos Almacenamiento vs Nodos abiertos
plt.figure()
plt.plot(vector_nodos_abiertos, vector_tamanio_abiertos)
plt.xlabel('Nodos abiertos')
plt.ylabel('Almacenamiento [bytes]')
plt.title(archivo + ' h{}'.format(tipo_heuristica) + ' ' + msg_aprox[0:-1])
plt.savefig('Resultados/' + archivo[0:9] + '_{}_'.format(tipo_heuristica) + msg_aprox +'almacenamiento' + '.png')
    
print('Umbral = {}'.format(costo_aproximado))