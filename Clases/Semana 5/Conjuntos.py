conjuntos= set() 
conjuntoA= { 1,2,3,4,5,6,7   }
conjuntoB= {  2,4,6,8,10 }
# Conjunto --> se escribe con llaves, no tiene elementos repetidos y puedo realizar
#operacion como los conjuntos matematicos 
union_conjuntos= conjuntoA.union(conjuntoB) # retorne o imprima todos los elmentos de las listas
# todos*<<--- union 
interseccion_conjuntos= conjuntoA.intersection(conjuntoB)
#los que se repetien en uno y otro*<-- los que estan en a y los que estan en b
restaA= conjuntoA - conjuntoB  #los que estan en el conjunto a pero no estan en b
restaB= conjuntoB-conjuntoA

diferencia_simetrica= conjuntoA.symmetric_difference(conjuntoB) #todos los elementos, menos los que se repiten

print(union_conjuntos)
print(interseccion_conjuntos)

print(diferencia_simetrica)


conjuntoC= {"papa","cebolla"}
conjuntoTienda= {"limon","papa","arroz","tomate"}
estanEnTienda = conjuntoC.issubset(conjuntoTienda)
print(estanEnTienda)
# lista, tupla, conjunto -->

