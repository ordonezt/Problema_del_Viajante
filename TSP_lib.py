# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:36:06 2021

@author: Usuario
"""
import numpy as np
from datetime import timedelta

def leer_archivo(filename):
        
        f = open (filename,'r')
        mensaje = f.read()
        print(mensaje)
        f.close()
        
        return 0
    
def leer_lineas_archivo(filename):
    
        f = open (filename,'r')
        mensaje = f.readlines()
        f.close()
        
        return mensaje

def calc_dim(lineas):
    m=''
    for i in lineas:
        if (i!=';'):
            m=m+i;

    n=int(m)
    return(n)
    
def matrix_TSP(n,lin):
    
    matrix= np.zeros(shape=(n,n))
    datos=''
    cont=0
    
    if (len(lin)==(n-1)):
        return(0)
    
    if (len(lin)!=(n-1)):
        lineas=lin[1]
        datos=lineas.replace(";"," ")
        data=datos.split()
    
        for i in range(n):
            for j in range(n):
                if( j>i ):
                    matrix[i,j]=data[cont]
                    matrix[j,i]=data[cont]
                    cont=cont+1
    
        return(matrix)

def guardar_resultados(path_archivo, meta, nodos_abiertos, tiempo, heuristica=None):
    # La información que contendrá el archivo de salida es la siguiente:

    # TSP_OUT_xx_XXX.txt:
    
    # strCamino;<CR>
    # CT;<CR>
    # NA;<CR>
    # strTiempoEj;<CR>
    # EOF
    
    # Donde:   
    # strCamino es un string con el camino encontrado, de la forma "1;2;3;4;5;1;"
    # CT es el costo total del camino encontrado.
    # NA es la cantidad de nodos abiertos durante el proceso.
    # strTiempoEj es un string con el tiempo de ejecución.
    if heuristica != None:
        heuristica_str = str(heuristica)
    else:
        heuristica_str = ''
        
    id_archivo = path_archivo[-6:-4]
    extension = '.txt'
    path = 'Resultados_TSP/TSP_OUT_' + id_archivo + '_BBMO' + heuristica_str + extension
    
    with open(path, 'w+') as archivo:
        
        #formo la string del camino
        camino = meta.get_herencia()
        camino_id = []
        for ciudad_i in camino:
            camino_id.append(ciudad_i.identificador)
        camino_id.reverse()
        camino_id.append(meta.identificador)
        archivo.write(str(camino_id) + ';\n')
        
        #Escribo el costo
        archivo.write(str(meta.get_costo()) + ';\n')
        
        #Escribo la cantidad de nodos abiertos
        archivo.write(str(nodos_abiertos) + ';\n')
        
        #Escribo el tiempo de ejecucion
        tiempo_str = str(timedelta(seconds=tiempo))
        archivo.write(tiempo_str + ';\n')
        