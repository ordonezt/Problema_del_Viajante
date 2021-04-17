# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:44:57 2021

@author: Usuario
"""

from TSP_lib import leer_lineas_archivo, calc_dim, matrix_TSP
from python_tsp.exact import solve_tsp_dynamic_programming


filename="TSP_IN_10.TXT"

lineas=leer_lineas_archivo(filename)


#print((lineas[0]))
#print((lineas[1]))
#print((lineas[2]))

n=calc_dim(lineas[0])

print(len(lineas))

print(lineas)
      
matrix=matrix_TSP(n,lineas)

print(matrix)


#permutation, distance = solve_tsp_dynamic_programming(matrix)

#print("Camino")
#print(permutation)

        
def tsp_resolver():
    pass
    # Pasos del algoritmo A*:
    #     Armar 2 listas, una vacia y una cerrada
    #     Asignarle todos los nodos como hijos al nodo de inicio
    #     Ponemos el nodo de inicio en la lista abierta
        
    #     Mientras que haya nodos en la lista abierta:
    #         Ordenar la lista abierta de menor (costo) a mayor
    #         Agarrar el de menor costo y pasarlo a la lista cerrada
            
    #         Era el nodo destino?
    #             No:
    #                 Pasar todos sus hijos a la lista abierta si es que no estan
    #             Si:
    #                 Terminar

        
