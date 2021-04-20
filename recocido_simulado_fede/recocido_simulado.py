from readData import ReadData
from SA import SimAnneal
##################################################################
archivo = "berlin52.tsp"
archivo_path = "../Recursos_de_la_catedra/Datos/"+archivo
#print (archivo_path)
D = ReadData(archivo_path)
print(D.GetDistanceMat())
sa = SimAnneal(D.GetDistanceMat(),archivo_path)#, stopping_iter=2)
sa.anneal()

#berlin52.tsp se obtuvo 8363,8646,8586 y por ahí... y en la mejor corrida de la página es de 7542