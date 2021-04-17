% PruLeeTSPLIB
% Archivo de prueba de lectura de los archivos TSPLIB.
% El formato de los archivos de entrada está especificado en TSPLIBdoc.pdf
% Ver también el sitio:
% http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/
%
% JuanCa 24/06/2012

clc; close all; clear all;

[xy name nC] = LeeTSPLIB('att48.tsp');

[xy name nC] = LeeTSPLIB('kroB200.tsp');

fin = 1;
