
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

def FindMinCostLevel(matriz_costos,nodo_padre,lista_nodos_previos,lista_nodos_abierta):
	######### FUNCION ENCARGADA DE BUSCAR EL MINIMO COSTO ENTRE LOS NODOS DE UN NIVEL DADO
	######### NO CUENTA LOS NODOS QUE SE ENCUENTRES YA EXPLORADOS (EN LA LISTA CERRADA)
	vector_costos = []
	min_cost = 0
	for i in lista_nodos_abierta:
		## recorro N-cant nodos explorados
		if (i.index_name not in lista_nodos_previos):
			# si el indice no esta en la lista de explorados tomo en cuenta su costo
			vector_costos.append(matriz_costos[nodo_padre.index_name][i.index_name]) 

	min_cost = np.min(vector_costos)
	#print("El costo minimo encontrado es : " +str(min_cost) )
	return min_cost

def FindBest(ciudad,matriz_costos,lista_nodos_previos,lista_nodos_cerrada):
	##########	FUNCION ENCARGADA DE ENCONTRAR EL HIJO CON EL MENOR COSTO #######

	costo_previo = 100000 ## costo para la primer comparacion
	costo_act = 0	
	
	if len(lista_nodos_previos) < n: #chequeo si no recorri toda la rama
			
		for i in range(n):

			# para que no se compare consigo misma
			if i not in lista_nodos_previos:
				
				#costo_act = matriz_costos[ciudad.index_name][i] + (n-i) * int(FindMinCostLevel(matriz_costos,ciudad,lista_nodos_previos,lista_nodos_abierta) )
				costo_act = matriz_costos[ciudad.index_name][i] + (n-i)*minimo_costo
				#costo_act = ciudad.f # evaluo el costo total f = g + h 
				if costo_act < costo_previo:
					#print(costo_act)
					# si el costo actual es menor al anterior, me quedo con ese nodo
					# print(i)
					nodo_hijo = lista_nodos_abierta[i]
					## cargo los costos de ese nodo hijo
					nodo_hijo.g =  matriz_costos[ciudad.index_name][i]

					#nodo_hijo.h = (n-i) * int(FindMinCostLevel(matriz_costos,ciudad,lista_nodos_previos,lista_nodos_abierta) )
					nodo_hijo.h = (n-i)*minimo_costo
					print("El costo h del nodo "+str(nodo_hijo.index_name)+" es "+str(nodo_hijo.h) )
					## cargo el indice del padre
					nodo_hijo.set_parent(ciudad.index_name)
					# ahora el costo siguiente debe ser mas bajo
					costo_previo = costo_act 	

			
		
		return nodo_hijo
# #Para correr el algoritmo como script descomentar
archivo_path = 'Recursos_de_la_catedra/Datos_no_euclidianos/TSP_IN_12.txt'

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
costo_total = 0
### creo la lista abierta ###
    
for i, nodo_i in enumerate(range(n)):
    lista_nodos_abierta.append(Nodo(0,0,nodo_i))
lista_nodos_abierta_sorted =copy(lista_nodos_abierta)
### TOMO UN NODO DE INICIO AL AZAR ###	

#random.shuffle(lista_nodos_abierta_sorted)
primer_ciudad = lista_nodos_abierta_sorted[0]
print("La ciudad de inicio es: "+str(primer_ciudad.index_name) )

lista_nodos_previos.append(primer_ciudad.index_name) # en esta lista guardo los nodos leidos

### empiezo a expandir por el metodo de expandir el primero el mejor ###
## cual es el hijo de menor coste?
lista_nodos_cerrada.append(lista_nodos_abierta[0]) # coloco el primer nodo a expandir en la lista cerrada

nodo_hijo = FindBest(primer_ciudad,matriz_costos,lista_nodos_previos,lista_nodos_cerrada)
nodo_hijo.set_parent(primer_ciudad.index_name)
lista_nodos_cerrada.append(nodo_hijo)
lista_nodos_previos.append(nodo_hijo.index_name)

#print("El hijo de menor coste es:"+str(nodo_hijo.index_name)+"\n con costo:"+str(nodo_hijo.g) )

parent_index = nodo_hijo.index_name

for i in range(n-2):
	#print(i)
	#recorro los nodos hasta el ultimo nodo	
	nodo_hijo = FindBest(nodo_hijo, matriz_costos,lista_nodos_previos,lista_nodos_cerrada)
	### VOY GUARDANDO LOS PADRES
	
	parent_index = nodo_hijo.index_name # el padre del proximo nodo es este
	### AGREGO EL NODO A LA LISTA CERRADA
	lista_nodos_cerrada.append(nodo_hijo)
	lista_nodos_previos.append(nodo_hijo.index_name)


lista_nodos_abierta[0].g = matriz_costos[nodo_hijo.index_name][primer_ciudad.index_name]

lista_nodos_cerrada.append(lista_nodos_abierta[0])
lista_nodos_previos.append(lista_nodos_abierta[0].index_name)

j=0
for i in lista_nodos_cerrada:
	#print(costo_total)
	if(j < n):
		costo_total = i.g + costo_total 	
	j = j+1	

print("el camino encontrado es: " + str(lista_nodos_previos))
print("con coste total = ",costo_total)
print("cant de nodos desarrollados = ",len(lista_nodos_previos) ) 


