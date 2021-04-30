from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from nodos_lib import Nodo, crear_nodos
from copy import copy
from random import seed
import random
import numpy as np
from math import factorial
from collections import deque
class Nodo(object):
    """docstring for Nodo"""
    def __init__(self,g,h,index_name):
        super(Nodo, self).__init__()
        self.costos_hijos = []
        self.costos_hijo_anterior = []
        self.hijos = deque([]) 
        self.padres = []
        self.g = g #funcion costo asignado
        self.h = h #funcion costo heuristica
        self.f = self.h+self.g #funcion soto total
        self.costo_acumulado = 0
        self.index_name = index_name # numero de ciudad
        self.hijos_visitados = []
        self.ciudad = index_name[len(index_name)-1]
    def add_hijo(self,matriz_costos,matriz_heur,index,index_name):
         ### agrego un hijo del nodo padre ##
        self.hijos.append(create_node(matriz_costos[index],matriz_heur[index],index_name))

    def create_node(self,g,h,index_name):
        new_node = Nodo(g,h,index_name)
    def set_parent(self,nodo_padre):
        self.padres = nodo_padre

def Cargar_Hijos(nodos_vector,matriz_costos):
    for i in nodos_vector:
        for j in range(n): # los posibles hijos son [0,1,2,....]
            if j != i.index_name :
            #if i.index_name != j.index_name: #un nodo no puede ser su propio hijo
                i.hijos.append(j) 
            

def Encontrar_camino(lista_nodos_abierta,lista_nodos_cerrada,matriz_costos,minimo_costo):
    ### inicialmente en la lista abierta solo tengo el camino 1-1 cuyo g = 0 y h no tiene sentido evaluarlo
    #lista_nodos_cerrada.append(lista_nodos_abierta.pop(0))
    print("minimo_costo", minimo_costo)
    lista_ciudades = []
    
    for i in range(n):
        lista_ciudades.append(i)
    print("lista de ciudades", lista_ciudades)
    h=0
    lista_de_costos = []
    ultimo_nodo = "inicio"
    nodo = lista_nodos_abierta[0]
    
    lista_nodos_abierta = [] 
    for i in nodo.hijos:
        #### INICIALIZAMOS UNA LISTA DE NODOS ABIERTA
        if nodo.ciudad != i:

            index_name = nodo.index_name+[i]
            #h = minimo_costo *(n - len(index_name) )
        
            nodo_a_expandir = Nodo(matriz_costos[i][nodo.index_name],h,index_name) 
            print(nodo_a_expandir.f)
            nodo_a_expandir.set_parent(nodo)
            lista_nodos_abierta.append(nodo_a_expandir)

    while( ultimo_nodo != "meta"):
        #### iteramos hasta que la ultima ciudad del camino se 0
        #### elejimos el mejor nodo a expandir evaluando el minimo F = g+h
        h = minimo_costo *(n - len(nodo.index_name) )
        for nodo in lista_nodos_abierta:

            lista_de_costos.append(nodo.f)
        #print("minimo costo encontrado : " +str(np.min(lista_de_costos)))
        nodo_a_expandir = lista_nodos_abierta[np.argmin(lista_de_costos)]
        #print("el proximo nodo a expandir es :" , nodo_a_expandir.index_name)
        print("con costo :",nodo_a_expandir.f)
        #print(nodo_a_expandir.ciudad)
        ### tomamos ahora el nodo y lo colocamos en la lista cerrada
        lista_nodos_cerrada.append(lista_nodos_abierta.pop(np.argmin(lista_de_costos)))
        print("ciudad",nodo_a_expandir.ciudad)
        ### preguntamos si el nodo de la lista cerrada tiene como ultimo destino la meta
        if nodo_a_expandir.ciudad == 0:
            ## si es asi marcamos la meta para salir del loop
            ultimo_nodo = "meta"
        else:
            ## si no es asi agregamos a la lista abierta los nodos frontera siguientes al nodo expandido

            ## armamos la lista de ciudades que puede visitar ese nodo
            for i in lista_ciudades:
                if i not in nodo_a_expandir.index_name and i != nodo_a_expandir.ciudad:
                    nodo_a_expandir.hijos.append(i)
            print("posibles ciudades a visitar por este nodo : ", nodo_a_expandir.hijos )
            ## armamos la lista abierta agregando los nodos hijos de este nodo
            for i in nodo_a_expandir.hijos:
                    index_name = nodo_a_expandir.index_name+[i]
                    #h = minimo_costo *(n - len(index_name) )
                    nodo = Nodo(matriz_costos[i][nodo_a_expandir.ciudad],h,index_name)
                    lista_nodos_abierta.append(nodo)
            #visitadas.append(nodo_a_expandir.ciudad)
            nodo = nodo_a_expandir

            print("la lista de nodos abierta posee")    
            for i in lista_nodos_abierta:
                print(str(i.index_name)+"con costo "+str(i.f) )

            lista_de_costos = []
            if len(nodo.index_name) == n-1 :

                # como el index_name va a haciendo un append de las ciudades, cuando llego a la longitud n-1 ya estoy en el final
                ultimo_nodo = "meta"
                camino_final = lista_nodos_abierta.pop()
        #break
    print("camino final " , camino_final.index_name)
    costo_total = 0
    for i in range(len(camino_final.index_name)):
        costo_total = costo_total + matriz_costos[camino_final.index_name[i]][camino_final.index_name[i-1]]

    print("con costo total",costo_total)

        
archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_07.txt'

 #Leemos el archivo
lineas = leer_lineas_archivo(archivo_path)

# cantidad de ciudades (nodos) a crear
n = calc_dim(lineas[0])

#Creamos la matriz de costos
matriz_costos = matrix_TSP(n, lineas)
## armo un vector de valores heuristicos para cada nodo 
## funcion heurisitica h[n] = [n-i]*min(costo_del_nivel)
## buscamos el valor minimo en toda la matriz
min_values = []
for i in matriz_costos:
    
    min_values.append(i[i>0])
minimo_costo = np.min(min_values)   
print("El minimo costo encontrado en toda la matriz es : "+str(minimo_costo))

lista_nodos_abierta =[]
lista_nodos_cerrada =[]
lista_caminos = []

### creo la lista abierta ###
    
for i, nodo_i in enumerate(range(n)):
    lista_nodos_abierta.append(Nodo(0,0,[nodo_i]))

### TOMO UN NODO DE INICIO AL AZAR ###  
for i in range(n):
    lista_nodos_abierta[n-1].index_name=n-1
#random.shuffle(lista_nodos_abierta_sorted)
primer_ciudad = lista_nodos_abierta[0]
print("La ciudad de inicio es: "+str(primer_ciudad.index_name) )



### empiezo a expandir por el metodo de expandir el primero el mejor ###
## cual es el hijo de menor coste?
costo_optimo = np.inf
#lista_nodos_cerrada.append(lista_nodos_abierta[0]) # coloco el primer nodo a expandir en la lista cerrada

#### CARGO LOS HIJOS POSIBLES DE CADA NODO (EN ESTOS CASOS CADA NODO PUEDE TENER DE HIJO A CUALQUIER NODO)
Cargar_Hijos(lista_nodos_abierta,matriz_costos) # FUNCIONA
#for i in lista_nodos_abierta:
#   print(i.hijos)

lista_nodos_abierta[0].set_parent(0) # la primer ciudad es su propio padre en principio

vector_costos=[]
lista_nodos_abierta[0].costo_acumulado = 0


Camino_final = Encontrar_camino(lista_nodos_abierta,lista_nodos_cerrada,matriz_costos,minimo_costo)

