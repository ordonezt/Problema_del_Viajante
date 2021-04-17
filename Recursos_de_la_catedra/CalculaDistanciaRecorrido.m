% Función que calcula la distancia de un recorrido (secuencia de ciudades) leyendo 
% el archivo de la matriz de distancias, tal como se especifica en el problema de 
% TP de IIA.
% Devuelve la distancia del recorrido
%
% Utiliza leeMatrizDistanciasIIA()
%
% JuanCa 05/05/2016
function [dist] = CalculaDistanciaRecorrido(recorrido, fileName) 
dist = 0;

% Obtiene la matriz desde el archivo.
matDist = leeMatrizDistanciasIIA(fileName);

% calcula la cantidad de ciudades
cantCiud = length(recorrido)-1;

% calcula el recorrido
for i=1:cantCiud 
    cAnt = recorrido(i);
    cPos = recorrido(i+1);
    dist = dist + matDist(cAnt,cPos);
end



return;


