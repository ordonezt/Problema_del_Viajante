#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:06:38 2021

@author: ord
"""

class Nodo:
    hijos = []
    padre = 0
    f = 0
    g = 0
    h = 0
    
    meta = False
    
    def __init__(self, identificador, heuristica=0, meta=False):
        self.identificador = identificador
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
            herencia.append(padre)
            padre = padre.get_padre()
        return herencia
    
    def set_hijo(self, hijo, mapa_costos):            
        hijo.set_padre(self)
        hijo.g = self.g + mapa_costos[self.identificador, hijo.identificador]
        self.hijos.append(hijo)
    
    def get_costo(self):
        self.f = self.g + self.h
        return self.f
    
    def is_meta(self):
        return self.meta
    

def crear_nodos(cantidad, heuristicas):
    nodos = []
    
    for i, nodo_i in enumerate(range(cantidad)):
        nodos.append(Nodo(nodo_i, heuristicas[i]))
    
    return nodos

