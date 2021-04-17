% Sript para probar el cálculo de la distancia de un recorrido.

 fileName = 'TSP_IN_01.txt';        % Archivo de entrada ...
 recorrido = [1 2 3 4 5 1];
% fileName = 'TSP_IN_02.txt';
fileName = 'TSP_IN_03.txt';
% fileName = 'TSP_IN_04.txt';
% fileName = 'TSP_IN_05.txt';
% fileName = 'TSP_IN_06.txt';
% fileName = 'TSP_IN_07.txt';
% fileName = 'TSP_IN_08.txt';
 fileName = 'TSP_IN_09.txt';
% fileName = 'TSP_IN_10.txt';
% fileName = 'TSP_IN_11.txt';
% fileName = 'TSP_IN_12.txt';

% pruebas...

recorrido = [1, 2, 3, 4, 6, 8, 10, 5, 7, 9, 1];
% recorrido = [1 14 9 13 8 4 12 7 3 11 6 2 15 10 5 1];
% recorrido = [1 2 4 6 8 5 7 9 10 3 1];
% recorrido = [ 1 3 5 7 9 10 8 6 4 2 1];
% recorrido = [1 6 5 4 3 2 1];
% 8
% recorrido = [1 2 3 9 7 5 6 8 4 10 1];
% recorrido = [1 3 9 7 5 6 8 4 10 2 1];
% recorrido = [1 2 10 9 3 4 8 6 5 7 1];
% recorrido = [1 2 9 3 5 6 8 4 10 7 1];
% 9
% recorrido = [1 10 9 8 7 6 5 4 3 2 1];
% recorrido = [1 2 3 4 5 6 7 8 9 10 1];
% recorrido = [1 10 9 8 7 6 5 4 3 2 1];
% recorrido = [1 10 9 8 7 6 5 4 3 2 1];


distancia = CalculaDistanciaRecorrido(recorrido, fileName);
disp(sprintf('\nDistancia = %d',distancia));
fin=0;

