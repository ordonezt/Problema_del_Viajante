from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from nodos_lib import Nodo, crear_nodos
from copy import copy
import numpy as np

def puntoArranque(size):
  #  return starting points list
	np.random.seed(1)
	a = round(size)
	mi = 1
	mx = 10
	if a>mx:
		l = np.random.choice(size, mx, replace=False)
		return(l)
	elif a<=10:
		l = np.random.choice(size, mi, replace=False)
		return(l)
	else:
		l = np.random.choice(size, a, replace=False)
		return(l)

def nearest_neighbour(startPoint,dist_mat,size):
		"""
		Nearest Neighbour algorithm
		"""    
		Tour = [startPoint]
		for _ in  range(size-1):
			min_index = np.argmin(dist_mat[Tour[-1]])
			#print("Para el punto de arranque "+str(startPoint)+" se tuvo el índice mínimo "+str(min_index)+" con valor "+str(dist_mat[Tour[-1]][min_index]))
			for t in Tour:
				dist_mat[min_index][t] = np.inf
				dist_mat[t][min_index] = np.inf
			Tour.append(min_index)
		return np.array(Tour)

def get_tour_distance(T,dist_mat):
	s = 0
	for i,t in enumerate(T):
		try:
			s+=dist_mat[t][T[i+1]]
		except IndexError:
			s+=dist_mat[t][T[0]]
	return s    

indice = "05"
archivo = "TSP_IN_"+indice+".txt"
archivo_path = "Recursos_de_la_catedra/Datos_no_euclidianos/"+archivo
lineas = leer_lineas_archivo(archivo_path)
n = calc_dim(lineas[0])
matriz_costos = matrix_TSP(n, lineas)
for i in range(n):
	matriz_costos[i][i] = np.inf
#print(matriz_costos)
matriz_costos_temp = np.copy(matriz_costos)
tours_dist = []
tours = []
#startPoints = puntoArranque(n)
startPoints = range(n)
print(startPoints)
for s in startPoints:
	t = nearest_neighbour(s,matriz_costos_temp,n)
	d = get_tour_distance(t,matriz_costos)
	tours.append(t+1)
	tours_dist.append(d)
	matriz_costos_temp = matriz_costos.copy()

min_dist_index = np.min(tours_dist)
print("El mínimo costo para los puntos de arranque fue: "+str(min_dist_index))