#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:06:38 2021

@author: Grupo 1
"""
from numpy import arange, nonzero
from copy import copy

class Nodo:
    hijos = []
    padre = 0
    f = 0
    g = 0
    h = 0
    
    meta = False
    
    def __init__(self, ciudad_cabecera, heuristica=0, meta=False):
        self.ciudad_cabecera = ciudad_cabecera
        self.h = heuristica
        self.meta=meta
        
    def set_padre(self, padre):
        self.padre = padre
    
    def get_padre(self):
        return self.padre
    
    def get_herencia(self):
        herencia = []
        padre = self.padre
        while padre != 0:
            herencia.append(padre.ciudad_cabecera)
            padre = padre.get_padre()
        herencia.reverse()
        return herencia
    
    def set_hijo(self, hijo, mapa_costos, tipo_heuristica=3):    
        n = mapa_costos.shape[0]
        
        camino = self.get_herencia()
        camino.append(self.ciudad_cabecera)
        
        n_recorridas = len(camino) +1
        
        #Le cargo la heuristica
        if tipo_heuristica == 0:
            hijo.h = 0
            
        elif tipo_heuristica == 1:
            costo_minimo_global = min(mapa_costos[nonzero(mapa_costos)])
            hijo.h = costo_minimo_global * ((n + 1 - n_recorridas) ** 2) / (n+1)
       
        elif tipo_heuristica == 2:
            costo_minimo_global = min(mapa_costos[nonzero(mapa_costos)])
            hijo.h = costo_minimo_global * (n + 1 - n_recorridas) * n_recorridas / (n+1)
       
        elif tipo_heuristica == 3:
            costo_minimo_global = min(mapa_costos[nonzero(mapa_costos)])
            hijo.h = costo_minimo_global * (n + 1 - n_recorridas)
       
        elif tipo_heuristica == 4:
            costos_locales = copy(mapa_costos)
            if n_recorridas < (n):
                for ciudad in camino:
                    #Pongo la fila con costo cero para no considerarla despues
                    costos_locales[ciudad] = 0
                    #Pongo la columna con costo cero para no considerarla despues
                    costos_locales[:,ciudad] = 0
                costo_minimo_restante = min(costos_locales[nonzero(costos_locales)])
            else:
                costo_minimo_restante = mapa_costos[self.ciudad_cabecera, hijo.ciudad_cabecera]
            hijo.h = costo_minimo_restante * (n + 1 - n_recorridas)
       
        else:
            hijo.h = 0
            
        hijo.set_padre(self)
        hijo.g = self.g + mapa_costos[self.ciudad_cabecera, hijo.ciudad_cabecera]
        hijo.f = hijo.g + hijo.h
        self.hijos.append(hijo)
    
    def get_costo(self):
        self.f = self.g + self.h
        return self.f
    
    def is_meta(self):
        return self.meta
    

def crear_ciudades(cantidad):   
    return list(arange(cantidad))

def calcular_costo_camino(camino, matriz_costos):
    costo = 0
    for i, ciudad in enumerate(camino[0:-1]):
        costo += matriz_costos[ciudad, camino[i+1]]
    return costo
