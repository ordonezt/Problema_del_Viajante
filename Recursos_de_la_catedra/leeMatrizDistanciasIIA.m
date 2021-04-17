% Funci�n que lee media matriz de distancias, tal como se especifica en el
% problema de TSP de IIA.
% Devuelve la matriz de distancias sim�trica.
%
% JuanCa 05/05/2016
function [matDist] = leeMatrizDistanciasIIA(fileName) 

matDist = [];
% fileName = 'TSP_IN_01.txt';        % Archivo de entrada ...
% fileName = 'TSP_IN_02.txt';
% fileName = 'TSP_IN_03.txt';
% fileName = 'TSP_IN_04.txt';
% fileName = 'TSP_IN_05.txt';
% fileName = 'TSP_IN_06.txt';
% fileName = 'TSP_IN_07.txt';
% fileName = 'TSP_IN_08.txt';
% fileName = 'TSP_IN_09.txt';
% fileName = 'TSP_IN_10.txt';
% fileName = 'TSP_IN_11.txt';
% fileName = 'TSP_IN_12.txt';

fH = fopen(fileName);           % Handler al archivo
line = fgetl(fH);   % Lee una nueva l�nea.
if(feof(fH))
    disp('error al leer el archivo');   
    return;                     % Termina con error
end
% Primera l�nea es la cantidad de ciudades
nCiud = sscanf(line,'%d');
if( ~(nCiud > 0))
    disp('error al leer la cantidad de ciudades');
    return;                     % Termina con error
end

    
matDist = zeros(nCiud,nCiud);
% Pr�ximas l�neas, filas y columnas de la matriz, pero s�lo mitad pues es sim�trica.
% Lee todas las l�neas hasta completar el archivo
line = [];
while( ~feof(fH) )
    line = [line, fgetl(fH)];   % Lee una nueva l�nea.
end
if( isempty (line))
    disp('error al leer la distancias de ciudades');
    return;
end
datos = sscanf(line,'%d;');
i=1;
for f=1:nCiud
    for (c = (f+1:nCiud))
        matDist(f,c) = datos(i);
        matDist(c,f) = datos(i);
        i=i+1;
    end
end


fclose(fH);

return






