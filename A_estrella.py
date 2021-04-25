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
		
		self.hijos = deque([]) 
		self.padres = 0
		self.g = g #funcion costo asignado
		self.h = h #funcion costo heuristica
		self.f = self.h+self.g #funcion soto total
		self.costo_acumulado = 0
		self.index_name = index_name # numero de ciudad
		self.hijos_visitados = []

	def add_hijo(self,matriz_costos,matriz_heur,index,index_name):
		 ### agrego un hijo del nodo padre ##
		self.hijos.append(create_node(matriz_costos[index],matriz_heur[index],index_name))

	def create_node(self,g,h,index_name):
		new_node = Nodo(g,h,index_name)
	def set_parent(self,index_parent):
		self.padres = index_parent

def Cargar_Hijos(nodos_vector):
	for i in nodos_vector:
		for j in range(n): # los posibles hijos son [0,1,2,....]
			if j != i.index_name :
			#if i.index_name != j.index_name: #un nodo no puede ser su propio hijo
				i.hijos.append(j) 

def Encontrar_camino(nodo,costo_inicial,lista_nodos_cerrada,lista_nodos_abierta,cantidad_caminos,lista_caminos):
	flag_ciudad_elegida = False
	visitados = []
	lista_nodos_abierta_aux =[]
	indices_hijos = [] # vector para almacenar el numero de los indices hijos
	index_a_visitar = 0
	
	#### nodo es el nodo a explorar, costo_inicial es el costo acumulado, costo_optimo es el acumulado mas bajo
	if nodo.index_name == 0:
		costo_inicial = 0

	### evaluamos los indices de los nodos visitados
	#print("nodo actual:",nodo.index_name) 
	#print("padre :",nodo.padres)
	
	costo = matriz_costos[nodo.index_name][nodo.padres] + costo_inicial + nodo.h
	if nodo.index_name !=0:
		lista_nodos_cerrada.append(nodo)
	
	#print("costo",costo)



	for i in lista_nodos_cerrada:
		visitados.append(i.index_name)
	for i in nodo.hijos:
		indices_hijos.append(i)
	#print("costo "+str(costo)+" para ir del :"+str(nodo.padres)+" a "+str(nodo.index_name))
	nodo.costo_acumulado = costo
	
	#### LLEGAMOS AL FINAL DE UNA RAMA	
	if( len(lista_nodos_cerrada) ) == n:

		#print("visitados rama",visitados)
		lista_nodos_abierta[0].set_parent(nodo.index_name)
		lista_nodos_cerrada.append(lista_nodos_abierta[0])

		#agregamos el costo de ir de la ultima ciudad al objetivo
		costo = matriz_costos[nodo.index_name][0] + nodo.h + costo

		# 
		if visitados not in lista_caminos:
			lista_caminos.append(visitados)
		
		#if costo < np.min(vector_costos):
		vector_costos.append(costo)

		if cantidad_caminos == factorial(n-1):
		# se recorrieron todos los caminos posibles
			print("sale")
			print("cantidad de nodos: ",cantidad_caminos*n)
			#print(lista_caminos)
			print("El mejor camino es:",lista_caminos[vector_costos.index(np.min(vector_costos))-1 ] )
			#print(vector_costos)
			return lista_nodos_cerrada
		else:
		# no se han recorrido todos los caminos posibles, por lo que sumo 1
			cantidad_caminos = cantidad_caminos + 1
			lista_nodos_cerrada = [lista_nodos_abierta[0]]


			Encontrar_camino(lista_nodos_abierta[0],np.inf,lista_nodos_cerrada,lista_nodos_abierta,cantidad_caminos,lista_caminos)
		
	else:
		#print("visitados parcial",visitados)
		lista_nodos_abierta_aux =deque(copy(nodo.hijos))
		# no llegue al final entonces sigo con el hijo que no haya visitado
		#print(indices_hijos)
				
		for i in nodo.hijos: 

				#print("hijos posibles:",nodo.hijos)
				#print("visitados:",visitados)
				if i not in visitados:
					
					### de los nodos a visitar posibles, tomo el primero y hago un shift left del vector
					### asi voy a realizar la combinatoria de todos los caminos posibles
					
					index_a_visitar = i

					nodo.hijos.rotate(1) # reacomodo los nodos para tomar el siguiente
				

					break
					
			
		lista_nodos_abierta[i].set_parent(nodo.index_name)
			 			
		Encontrar_camino(lista_nodos_abierta[i],costo,lista_nodos_cerrada,lista_nodos_abierta,cantidad_caminos,lista_caminos)
		
	




archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_01.txt'

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
lista_nodos_abierta_sorted =[]
lista_nodos_cerrada =[]
lista_nodos_previos=[]
lista_caminos = []

### creo la lista abierta ###
    
for i, nodo_i in enumerate(range(n)):
    lista_nodos_abierta.append(Nodo(0,0,nodo_i))
lista_nodos_abierta_sorted =copy(lista_nodos_abierta)
### TOMO UN NODO DE INICIO AL AZAR ###	
for i in range(n):
	lista_nodos_abierta[n-1].index_name=n-1
#random.shuffle(lista_nodos_abierta_sorted)
primer_ciudad = lista_nodos_abierta_sorted[0]
print("La ciudad de inicio es: "+str(primer_ciudad.index_name) )



### empiezo a expandir por el metodo de expandir el primero el mejor ###
## cual es el hijo de menor coste?
costo_optimo = np.inf
#lista_nodos_cerrada.append(lista_nodos_abierta[0]) # coloco el primer nodo a expandir en la lista cerrada

#### CARGO LOS HIJOS POSIBLES DE CADA NODO (EN ESTOS CASOS CADA NODO PUEDE TENER DE HIJO A CUALQUIER NODO)
Cargar_Hijos(lista_nodos_abierta) # FUNCIONA
#for i in lista_nodos_abierta:
# 	print(i.hijos)

lista_nodos_abierta[0].set_parent(0) # la primer ciudad es su propio padre en principio
vector_costos=[]
vector_costos.append(costo_optimo)
lista_nodos_cerrada.append(lista_nodos_abierta[0])
#lista_nodos_cerrada.append(lista_nodos_abierta[0])
#lista_nodos_abierta[1].set_parent(0)
Camino_final = Encontrar_camino(lista_nodos_abierta[0],costo_optimo,lista_nodos_cerrada,lista_nodos_abierta,0,lista_caminos)

#for i in Camino_final:
	#print(i.index_name)
	
print(np.min(vector_costos))