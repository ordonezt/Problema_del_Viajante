#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:06:38 2021

@author: ord
"""

class Nodo:
    hijos = []
    
    def __init__(self, identificador):
        self.identificador = identificador
        
    def set_padre(self, padre):
        self.padre = padre
    
    def get_padre(self):
        return self.padre
    
    def set_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.set_padre(self)
    

def crear_nodos(cantidad):
    nodos = []
    
    for nodo_i in range(cantidad):
        nodos.append(Nodo(nodo_i))
    
    return nodos

