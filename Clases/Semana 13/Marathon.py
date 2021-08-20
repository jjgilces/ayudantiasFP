from typing import List, SupportsRound
import numpy as np

sur = ['LosEsteros','Pradera' , 'RiocentroSur']
centro = ['Bahia', 'Malecon2000' , 'MaleconSalado']
norte = ['MallDelSol', 'CityMall' , 'RiocentroNorte']
futbol = ['zapatos-Adidas', 'zapatos-Nike', 'rodilleras-Reebok']
natacion = ['short-Nike', 'gafasPiscina-Swingo' , 'aletas-Speedo']

tiendas=sur+centro+norte
categorias= futbol+natacion

M= np.ones((len(tiendas),len(categorias)))

#EJERCICIO1
#A 
sumaColumnas= np.sum(M,axis=0)
futbolSuma= sumaColumnas[:len(futbol)]
natacionSuma= sumaColumnas[len(futbol):]
totalFutbol = sum(futbolSuma)
totalNatacion=sum(natacionSuma)
print(M)
print(sumaColumnas)
print(futbolSuma)



if totalFutbol>totalNatacion: 
    print("FUTBOL TIENE MAS VENTAS ",totalFutbol)
elif totalFutbol<totalNatacion:
    print("NATACION TIENE MAS VENTAS ",totalNatacion)
else: 
    print("Iguales",totalNatacion)

#Ejercicio 2
sumaTiendas= np.sum(M,axis=1)
indice= np.argmax(sumaTiendas)
tiendasMas= tiendas[indice]
print(sumaTiendas)

#Ejercicio 3
indiceNorte=len(sur)+len(centro)
sumaTiendasNorte=sumaTiendas[indiceNorte:]
indiceNorteMayor= np.argmax(sumaTiendasNorte)
tiendaMayorNorte= norte[indiceNorteMayor]


#Ejercicio 4
matrizSur= M[:len(sur),:]
matrizPSur= np.sum(matrizSur,axis=0)
indiceProductoSur= np.argmax(matrizPSur)
productoSurMayor= categorias[indiceProductoSur]
print(productoSurMayor)
