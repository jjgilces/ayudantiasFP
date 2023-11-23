import random as rd
#si me preguntan si un numero 
n=19
esPar= n%2==0 #True si es par False si no es par 

#promedio de una lista 
lista=[10,10,30]



#si me piden buscar un elemento a partir de otro 
animes = [ "Jujutsu Kaisen", "Tokyo Revengers", "Haikyuu", "Kimetsu No yaiba", "Boku No Hero", "Naruto"]
precios = [15.5 , 20.80, 10.78, 17.90, 23.56, 24.62] 
#YO TENGO EL ANIME
anime= input("Ingrese el anime que desea comprar: ")#naruto --> Naruto

#deberia buscar el indice de ese anime en la lista DE ANIMES
indice= animes.index(anime)
#deberia indexar el precio de ese anime EN LA LISTA DE PRECIOS
precio= precios[indice]  #30
#deberia pedir al usuario cuanto efectivo tiene 


#Obtener un elemento aleatorio de la lista y obtener otro dato de uuna lista
anime_azar= rd.choice(animes)
indice_azar= animes.index(anime)
#deberia indexar el precio de ese anime EN LA LISTA DE PRECIOS
precio_del_anime_azar= precios[indice]  #30
#deberia pedir al usuario cuanto ef

#si me piden el que cuesta mas, el maximo, el mayor, pero ME PIDEN NOMBRE(no EL VALOR, SINO EL NOMRE)
mayor_precio= max(precios)
indice_mayor= precios.index(mayor_precio)
nombre_mayor = animes[indice_mayor]

#como obtener una lista a partir de un string
nombres="Johan,Jair,Gilces,Reyes" #identifico lo que me esta molestando, lo que separa a una 
#palabra de otra 
lista3= nombres.split(",")  # nombres.split(" ")  ---> ["Johan", "Jair","Gilces", "Reyes"]  



#creo una lista vacia 

paises_sin_repetir=[]
#recorro la repetida
for pais in paises: 
    if pais not in paises_sin_repetir:
        paises_sin_repetir.append(pais)

#solo agrego los elementos que no se encuentren en la lista
for pais in paises: 
    if pais  in paises_sin_repetir:
        paises_sin_repetir.remove(pais)
    paises_sin_repetir.append(pais)

