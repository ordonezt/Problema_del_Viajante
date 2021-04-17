% Lee matriz de coordenadas de un archivo TSPLIB.
% El formato de los archivos de entrada está especificado en TSPLIBdoc.pdf
% No está completo!!! Entre otras cosas no considera 3D.
% Ver también el sitio:
% http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/
% Devuelve la matriz xy con las coordenadas xy de cada ciudad en el plano,
% el string con el nombre indicado en el archivo y la cantidad de ciudades.
% 
% JuanCa 24/06/2012
%

% fileName = 'att48.tsp';        % 


[fileName,PathName,FilterIndex] = uigetfile('*.tsp', 'Seleccione archivo .tsp');


% Lee el archivo seleccionado y obtiene la matriz de coordenadas, el nombre
% y la cantidad de ciudades.
[xy name n] = LeeTSPLIB(strcat(PathName,fileName));

% Prueba...
% xy = [100 , 100; 200, 200; 300,300];
% n=3;

a = meshgrid(1:n);
% Calcula la matríz de distancias entre ciudades. para TSPLIB deben ser
% enteros. por eso round()
dmat = reshape(round(sqrt(sum((xy(a,:)-xy(a',:)).^2,2))),n,n);

[strPath, strName, strExt] = fileparts(fileName);
outFileName = strcat(strName,'_O','.txt');

fH = fopen(strcat(PathName,outFileName),'w+');
fprintf( fH, '%0.0d;\n',n);
for i=1:(n-1)
    fprintf( fH, '%0.0f;',dmat(i,(i+1):end));        
    fprintf( fH, '\n');
end
fclose(fH);

fin = 1;
