# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:03:55 2021

@author: Usuario
"""
import numpy as np
import matplotlib.pyplot as plt


def save_cities(cities,archivo):
        name="cities"+"_"+archivo
        f = open (name,'w')
        for i in range(len(cities)):
    
                f.write((str(i)+" "+str(cities[i].x)+" "+str(cities[i].y)+"\n"))

        f.close()
        return(0)
    

def print_cost(archivo,T_init_round, T_round, val,x,costo,costo_optimo):

    plt.figure()
    ax = plt.axes()
    ax.grid()
    plt.xlabel("Iteraciones")
    plt.ylabel("Costo")
    
    titulo= archivo + " con T_inicial=" + str(T_init_round)+"ºC" + " y T_final=" + str(T_round)+"ºC"
    plt.title(titulo)
    ax.plot(x, val,label='costo (final= {0:.2f})'.format(costo));
    plt.axhline(costo_optimo, color='r', linestyle='--',label='costo optimo= {0:.2f}'.format(costo_optimo))
    plt.legend()
    return(0)
        
def print_temp(archivo,T_init_round, T_round, Temp,x):
    
    plt.figure()
    ax = plt.axes()
    ax.grid()
    plt.xlabel("Iteraciones")
    plt.ylabel("Temperatura [ºC]")
    
    titulo= archivo + " con T_inicial=" + str(T_init_round)+"ºC" + " y T_final=" + str(T_round)+"ºC"
    plt.title(titulo)
    ax.plot(x,Temp,label='temperatura (final= {0:.2f})'.format(T_round));
    plt.legend()
    return(0)


def Permutacion(cities):
    
    cities_new=cities.copy()
    i,l = np.random.randint(0,len(cities_new),size=2)
    temp=cities_new[i]
    cities_new[i]=cities_new[l]
    cities_new[l]=temp

    return(cities_new)
    
def Storung(cities):
    
    cities_new=cities.copy()
    i= np.random.randint(0,len(cities_new))
    l=i-1
    temp=cities_new[i]
    cities_new[i]=cities_new[l]
    cities_new[l]=temp

    return(cities_new)

def Inversion(cities):
    
    cities_new=cities.copy()
    i,l= np.random.randint(0,len(cities_new),2)
    cities_new[i : (i + l)] = reversed(cities_new[i : (i + l)])

    return(cities_new)
    

def Temperatura1(T,F):
    Temp=T
    Temp=Temp*F
    return(Temp)

def Temperatura2(T,F):
    Temp=T
    Temp=Temp/(1+Temp*F)
    return(Temp)

######## Funciones para leer el archivo 
    
def limpiar_encabezado(lineas):
    nueva_lineas = [""]
    for i in range(len(lineas)):
        linea = lineas[i].replace("  "," ")
        if(linea[0].isdigit()):
            nueva_lineas.append(linea)
    nueva_lineas.remove("")
    return nueva_lineas

def leer_lineas_archivo(filename):
    
        try:
            f = open (filename,'r')
            mensaje = f.readlines()
            f.close()
            
            return mensaje

        except:
            return -1

def get_costo_optimo(filename):
        if filename == "berlin52.tsp":
            costo_optimo=7542
        elif filename == "kroB100.tsp" :
            costo_optimo=22141
        elif filename == "kroB150.tsp" :
            costo_optimo=26130
        elif filename == "kroB200.tsp":
            costo_optimo=29437
        else:
            costo_optimo=-1
        return(costo_optimo)
        
#### Clase Coordinate, para sacar la distancia y armar el objeto ciudad
            
class Coordinate:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        
    def get_distance_euc(ca, cb):
        dif_x=ca.x-cb.x
        dif_y=ca.y-cb.y
        return( np.sqrt((dif_x**2)+(dif_y**2)))
    
    def get_total_distance(cities):
        dist=0
        for a,b, in zip(cities[:-1],cities[1:]):
            dist += Coordinate.get_distance_euc(a, b)
        dist += Coordinate.get_distance_euc(cities[0],cities[-1])
        return dist
    
    def get_distance_non_euc(ca,cb,matrix):
        
        return(matrix[ca][cb])
        
    def get_total_distance_non_euc(cities,matrix):
        dist=0
        for a,b, in zip(cities[:-1],cities[1:]):
            dist += Coordinate.get_distance_non_euc(a, b,matrix)
        dist += Coordinate.get_distance_non_euc(cities[0],cities[-1],matrix)
        return dist
    
