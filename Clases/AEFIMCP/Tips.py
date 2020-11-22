import random as rd
#Par
numero = 8
isImpar = numero%2!=0 #true o false
edades =[19,24,46,78]

#Promedio Listas
promedio = sum(edades)/len(edades)


#Cuando usar for y cuando usar while
#while- cuando no se cuando se acabe, depende, no conozco el bucle


#Como recorro listas paralelas (tiene la misma cant de elemento y tienen relacion)
edades =[19,24,100,78]

nombres =["Johan", "Andrea","Josue","Pedro"]
for indice in range(len(nombres)):
    edad= edades[indice]
    nombre= nombres[indice]
    # print(nombre,edad)

#El maximo, el minimo de una lista indexar(buscar) en otra
#el nombre del que tiene menor de edad y el nombre del que tiene mayor edad
print(max(edades))
indiceMaximo = edades.index(max(edades))
nombreMaximo = nombres[indiceMaximo]
print(indiceMaximo)
# print(nombreMaximo)
indiceMinimo = edades.index(min(edades))
nombreMinimo = nombres[indiceMinimo]
#Muestre los nombres los mayores al promedio 
print(promedio)
for i in range(len(nombres)):
    edad = edades[i]
    if edad>promedio:
        nombre= nombres[i]
        # print(nombre)


#Elemento random de una lista
numeroAletario = rd.randint(0,len(edades)-1)
nombreRandom= nombres[numeroAletario]
nombreRandom2= rd.choice(nombres)
# print(nombreRandom)
print(nombreRandom2)
