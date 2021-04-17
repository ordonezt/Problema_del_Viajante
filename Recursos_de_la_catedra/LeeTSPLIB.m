function [xy name nCiud]= LeeTSPLIB(fileName)
% Lee matriz de coordenadas de un archivo TSPLIB.
% El formato de los archivos de entrada est� especificado en TSPLIBdoc.pdf
% No est� completo!!! Entre otras cosas no considera 3D.
% Ver tambi�n el sitio:
% http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/
% Devuelve la matriz xy con las coordenadas xy de cada ciudad en el plano,
% el string con el nombre indicado en el archivo y la cantidad de ciudades.
% 
% JuanCa 24/06/2012
%

% Abre el archivo solicitado
fH = fopen(fileName);
while (1)
    line = fgetl(fH);   % Lee una nueva l�nea.
    if(feof(fH))
        disp('error al leer el archivo');
    end
    [token, remainder] = strtok(line, ' :');
    remainder = QuitaEspY2Puntos(remainder);               
    switch upper(token)
        case 'NAME' 
            name = remainder;
        case 'COMMENT'
            comment = remainder;               
        case 'TYPE'
            type  = remainder;
        case 'DIMENSION'
            nCiud = sscanf(remainder,'%d');
        case 'EDGE_WEIGHT_TYPE'
            edgeWeightType  = remainder;
        case 'NODE_COORD_SECTION'   % Comienza con las coordenadas
            break;                  % Sale del while y contin�a
        otherwise 
            disp('l�nea desconocida o no considerada');
    end
end
if isempty(nCiud)
    error('mal el n�mero de ciudades');
end
% Lee los valores y completa la matriz de coordenadas
xy = zeros(nCiud,2);
i=1;

line = fgetl(fH);   % Lee una nueva l�nea.
while ~feof(fH)
    [token, remainder] = strtok(line);
    xy(i,:)= sscanf(remainder,'%d');    % Deben ser enteros    
    i = i+1;
    line = fgetl(fH);   % Lee una nueva l�nea.
end

    
fclose(fH);

% -------------------------------------------------------------------------
function s = QuitaEspY2Puntos(s)
% Funci�n auxiliar que quita los espacios y ':' iniciales del string s
% Si llegan a ser todos espacios lo deja vac�o.

    if isempty(s)
        return;
    end
    lStr = length(s); % longitud del string

    for j=1:lStr
        if( (s(j) ~= ' ') && (s(j) ~= ':'))
            break;
        end
    end

    s = s(j:lStr);
end




end
