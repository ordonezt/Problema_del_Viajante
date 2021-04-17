# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:36:06 2021

@author: Usuario
"""
import numpy as np


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