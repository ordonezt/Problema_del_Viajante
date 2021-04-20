
from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from nodos_lib import Nodo, crear_nodos
from copy import copy
from random import seed
import random
import numpy as np

class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self,g,h,index_name):
		super(Nodo, self).__init__()
		
		self.hijos = [] 
		self.padre = 0
		self.g = g #funcion costo asignado
		self.h = h #funcion costo heuristica
		self.f = self.h+self.g #funcion soto total
		self.index_name = index_name # numero de ciudad

	def add_hijo(self,matriz_costos,matriz_heur,index,index_name):
		 ### agrego un hijo del nodo padre ##
		self.hijos.append(create_node(matriz_costos[index],matriz_heur[index],index_name))

	def create_node(self,g,h,index_name):
		new_node = Nodo(g,h,index_name)
	def set_parent(self,index_parent):
		self.padre = index_parent


def FindBest(ciudad,matriz_costos,matriz_heur,lista_nodos_previos):
	##########	FUNCION ENCARGADA DE ENCONTRAR EL HIJO CON EL MENOR COSTO #######

	costo_previo = 100000 ## costo para la primer comparacion
	costo_act = 0	
	if len(lista_nodos_previos) < n: #chequeo si no recorri toda la rama
			
		for i in range(n):
			# para que no se compare consigo misma
			if i not in lista_nodos_previos:    
				costo_act = matriz_costos[i][ciudad.index_name]
				if costo_act < costo_previo:
					# si el costo actual es menor al anterior, me quedo con ese nodo
					#print(i)
					nodo_hijo = lista_nodos_abierta[i]
					## cargo los costos de ese nodo hijo
					nodo_hijo.g = costo_act
					nodo_hijo.h = matriz_heur[i][ciudad.index_name]
					## cargo el indice del padre
					nodo_hijo.set_parent(ciudad.index_name)
					# ahora el costo siguiente debe ser mas bajo
					costo_previo = costo_act 	

		return nodo_hijo
	else:
		return False
# #Para correr el algoritmo como script descomentar
archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_06.txt'

 #Leemos el archivo
lineas = leer_lineas_archivo(archivo_path)

# cantidad de ciudades (nodos) a crear
n = calc_dim(lineas[0])

#Creamos la matriz de costos
matriz_costos = matrix_TSP(n, lineas)

matriz_heur = matrix_TSP(n, lineas)
lista_nodos_abierta =[]
lista_nodos_abierta_sorted =[]
lista_nodos_cerrada =[]
lista_nodos_previos=[]
costo_total = 0
### creo la lista abierta ###
    
for i, nodo_i in enumerate(range(n)):
    lista_nodos_abierta.append(Nodo(0,0,nodo_i))
lista_nodos_abierta_sorted =copy(lista_nodos_abierta)
### TOMO UN NODO DE INICIO AL AZAR ###	
random.shuffle(lista_nodos_abierta_sorted)
primer_ciudad = lista_nodos_abierta_sorted[0]
print("La ciudad de inicio es: "+str(primer_ciudad.index_name) )

lista_nodos_previos.append(primer_ciudad.index_name) # en esta lista guardo los nodos leidos

### empiezo a expandir por el metodo de expandir el primero el mejor ###
## cual es el hijo de menor coste?
lista_nodos_cerrada.append(lista_nodos_abierta[0]) # coloco el primer nodo a expandir en la lista cerrada

nodo_hijo = FindBest(primer_ciudad,matriz_costos,matriz_heur,lista_nodos_previos)
lista_nodos_cerrada.append(nodo_hijo)
lista_nodos_previos.append(nodo_hijo.index_name)
print("El hijo de menor coste es:"+str(nodo_hijo.index_name)+"\n con costo:"+str(nodo_hijo.g) )
	
for i in range(n-1):
	nodo_hijo = FindBest(nodo_hijo, matriz_costos,matriz_heur,lista_nodos_previos)
	if nodo_hijo == False:
		# llego al final de la rama
		break
	lista_nodos_cerrada.append(nodo_hijo)
	lista_nodos_previos.append(nodo_hijo.index_name)
	print("El hijo de menor coste es:"+str(nodo_hijo.index_name)+"\n con costo:"+str(nodo_hijo.g) )

for i in lista_nodos_cerrada:
	costo_total = i.g + costo_total 	

print("el camino encontrado es: " + str(lista_nodos_previos))
print("con coste total = ",costo_total)
print("cant de nodos desarrollados = ",len(lista_nodos_previos) ) 


