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
    
    tipo = ''
    
    def __init__(self, identificador):
        self.identificador = identificador
        
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
    
    def set_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.set_padre(self)
    
    def get_costo(self):
        self.f = self.g + self.h
        return self.f
    
    def is_meta(self):
        return self.tipo == 'Meta'

def crear_nodos(cantidad):
    nodos = []
    
    for nodo_i in range(cantidad):
        nodos.append(Nodo(nodo_i))
    
    return nodos

