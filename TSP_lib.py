# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:36:06 2021

@author: Grupo 1
"""
import numpy as np
from datetime import timedelta
import matplotlib.pyplot as plt
import time
import simulated_annealing_lib as sa

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

def imprimir_camino(nodo, mensaje=None):
    # camino_str = []
    camino = nodo.get_herencia()
    camino.append(nodo.ciudad_cabecera)
    # for ciudad_i in camino:
    #     camino_str.append(ciudad_i.identificador)
    # camino_str.reverse()
    # camino_str.append(nodo.ciudad_cabecera)
    print(mensaje, camino, " costo de {}".format(nodo.get_costo()))
    return

def guardar_resultados(path_archivo, meta, nodos_abiertos, tiempo, aproximacion, heuristica=None):
    # La información que contendrá el archivo de salida es la siguiente:

    # TSP_OUT_xx_XXX.txt:
    
    # strCamino;<CR>
    # CT;<CR>
    # NA;<CR>
    # strTiempoEj;<CR>
    # EOF
    
    # Donde:   
    # strCamino es un string con el camino encontrado, de la forma "1;2;3;4;5;1;"
    # CT es el costo total del camino encontrado.
    # NA es la cantidad de nodos abiertos durante el proceso.
    # strTiempoEj es un string con el tiempo de ejecución.
    if heuristica != None:
        heuristica_str = str(heuristica)
    else:
        heuristica_str = ''
    
    if aproximacion == 'si':
        msg_aprox = '_mejorado'
    else:
        msg_aprox = ''
        
    id_archivo = path_archivo[-6:-4]
    extension = '.txt'
    path = 'Resultados/TSP_OUT_' + id_archivo + '_BBMO' + heuristica_str + msg_aprox + extension
    
    with open(path, 'w+') as archivo:
        
        #formo la string del camino
        camino = meta.get_herencia()
        camino.append(meta.ciudad_cabecera)
        archivo.write(str(camino) + ';\n')
        
        #Escribo el costo
        archivo.write(str(meta.get_costo()) + ';\n')
        
        #Escribo la cantidad de nodos abiertos
        archivo.write(str(nodos_abiertos) + ';\n')
        
        #Escribo el tiempo de ejecucion
        tiempo_str = str(timedelta(seconds=tiempo))
        archivo.write(tiempo_str + ';\n')
    
    return

def mapa_calor(archivo):
    archivo_path = 'Entradas/' + archivo
    
    #Leemos el archivo
    lineas = leer_lineas_archivo(archivo_path)
    n = calc_dim(lineas[0])
    
    #Creamos la matriz de costos
    matriz_costos = matrix_TSP(n, lineas)
    
    plt.imshow(matriz_costos)
    plt.title(archivo + ' Mapa')
    plt.show()

def SA_res(index):
    #### Variables
    cities_min=[]
    val=[]
    deltaE=[]
    Temp=[]
    delta_costo=0
    Intentos=0
    Iteraciones=0
    
    ## Tiempo de ejecución inicial
    inicio = time.time()
    
    list_archivo=['TSP_IN_01.txt','TSP_IN_02.txt','TSP_IN_03.txt','TSP_IN_04.txt','TSP_IN_05.txt','TSP_IN_06.txt','TSP_IN_07.txt','TSP_IN_08.txt','TSP_IN_09.txt',\
                  'TSP_IN_10.txt','TSP_IN_11.txt','TSP_IN_12.txt']
    
    archivo='Entradas/'+list_archivo[index-1]


    lineas=leer_lineas_archivo(archivo)
    #print(lineas)
    dim=calc_dim(lineas[0])
    #print(dim)
    matrix=matrix_TSP(dim,lineas)
   # print(matrix)
    #print((matrix[0][5]))
    cities= [x for x in range(dim)]
   # print(cities)
    costo=sa.Coordinate.get_total_distance_non_euc(cities,matrix)
    #print(costo)
    
    
    list_archivo=['TSP_IN_01.txt','TSP_IN_02.txt','TSP_IN_03.txt','TSP_IN_04.txt','TSP_IN_05.txt','TSP_IN_06.txt','TSP_IN_07.txt','TSP_IN_08.txt','TSP_IN_09.txt',\
                  'TSP_IN_10.txt','TSP_IN_11.txt','TSP_IN_12.txt']
    list_costo_optimo=[30,35,31,30,83,76,10,143,10,17,15,15]
    list_T=[100,100,100,300,500,500,500,500,500,500,500,300]
    F=0.995
    list_NI=[1000,1000,1000,1000,2000,1500,1500,1500,2500,2000,2000,2000]
    list_NC=[150,150,150,150,500,500,500,500,500,500,500,500]
    list_IIT=[100,100,100,100,100,100,100,100,100,300,300,400]
    
    costo_optimo=list_costo_optimo[index-1]
    T=list_T[index-1]
    NI=list_NI[index-1]
    NC=list_NC[index-1]
    IIT=list_IIT[index-1]
    
    ###################################################### SEGMENTO 2
    # En cities tengo las ciudades con sus coordenadas
    
    #costo=sa.Coordinate.get_total_distance_non_euc(cities,matrix) # calculo el costo inicial
    costo_min=costo
    print("Costo Inicial: ",costo)
    print("Costo Optimo: ",costo_optimo)
    #print(cities)
    
    
    T_init=T #guardo la temperatura inicial
    
    while Iteraciones < NI :        
    
        # Armo vectores para graficar después
       val.append(costo)
       deltaE.append(delta_costo)
       Temp.append(T)
               
       for j in range(IIT):
                
                cities_new=sa.Inversion(cities) #Perturbación
                #cities_new=sa.Permutacion(cities) #Perturbación
                
                costo_new = sa.Coordinate.get_total_distance_non_euc(cities_new,matrix)#Calculo el nuevo costo
                
                # Hago este IF para quedarme con el camino mínimo, no es parte del SA
                if costo_new < costo_min:               #el costo nuevo el menor
                    costo_min=costo_new                 # me quedo con el menor
                    cities_min=cities_new.copy()        
                
                #Si el costo nuevo es menor al costo anterior, LO ACEPTO
                if costo_new < costo:               #el costo nuevo es menor
                    costo=costo_new                 # me quedo con el menor
                    cities=cities_new.copy()
                    Intentos=0  
                    
                #Si el costo nuevo es MAYOR al costo anterior, LO ACEPTO CON CIERTA PROBABILIDAD
                else:                               #si es mayor
                    x=np.random.uniform()           #probabilidad random entre 0 y 1
                    delta_costo=costo_min-costo_new     #Calculo el delta CON EL COSTO MINIMO HISTORICO!!!
                    
                    if x < np.exp(delta_costo/T):   #es menor a la probabilidad
                        costo=costo_new             #me quedo con el calculado
                        cities=cities_new.copy()    #y las ciudades
                        Intentos=0                 
                        
                    else:
                        Intentos=Intentos+1
    
       Iteraciones=Iteraciones +1
       
        #Condicion de Salida
       if Intentos > NC:
           #print(Intentos)
           break;
    
    
       #Cambio de la Temperatura
       T=sa.Temperatura1(T,F) # F= 0.995
       #T=sa.Temperatura2(T,F) # F=0.001
       #print(costo)
       
    ################################ FIN DEL WHILE 
       
    
           
    ################################ SEGMENTO 3
    '''       
    # Datos para graficar
    T_round=np.around(T, 2)
    T_init_round=np.around(T_init, 2)
    eje_x = np.linspace(0, Iteraciones, Iteraciones)
    
    #Grafico Costo y Temperatura en función de las Iteraciones
    sa.print_cost(archivo,T_init_round, T_round, val,eje_x,costo,costo_optimo)
    sa.print_temp(archivo,T_init_round, T_round, Temp,eje_x)
    
    #Costo mínimo encontrado
    print("El costo mínimo fue de: ",costo_min)
    print("El costo final fue de: ",costo)
    #Archivo con el último camino
    #sa.save_cities(cities,archivo)
    
    #Ploteo los valores de temperatura incial estimados (promedio de los delta energía/ln(pInicial))
    #print("Para un 50% de probabilidad inicial de aceptación: ",np.mean(deltaE)/0.69,"°C")
    #print("Para un 80% de probabilidad inicial de aceptación: ",np.mean(deltaE)/1.6,"°C")
    #print("Para un 20% de probabilidad inicial de aceptación: ",np.mean(deltaE)/0.223,"°C")
    
    #Calculo el tiempo de ejecución final y hago la diferencia
    fin = time.time() 
    print("Tiempo de Ejecución :",fin-inicio,"s") # 1.5099220275878906
    '''
    ############ 
    return(costo_min)