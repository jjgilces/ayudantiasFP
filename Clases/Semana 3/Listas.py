
"""
LISTAS 
Carateristicas:
1.   Mutables  --> cambian
2.   Permite cualquier tipo de dato --> 
"""


## Creación de listas vacias
lista=[]
lista2= list()

nombres="Johan Jair Gilces Reyes"
ingredientes="tomate,cebolla,pimiento,arroz"

lista3= nombres.split(" ")
lista4= nombres.split(",")

##Añadir elementos 
lista.append(1)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.insert(0,4)
lista.insert(-1,4)


"""Busqueda en listas"""
print(lista)
indice= lista.index(4)
print(indice)
elemento=lista[indice]
print(elemento)



"""Ordenamiento"""
lista.sort(reverse=True)
print(lista)
#de pequeño a más grande




"""Cambio de elementos"""
lista[0]=6
print(lista)
lista[-1]=10
print(lista)

'''Eliminar un elemento'''
lista.pop(2)  #elimina en esa posicion, si no recibe nada elimina el ultimo
print(lista)
lista.remove(4) #elemento 
print(lista)

## Operaciones de Listas

#1.   Suma  -->concatenacion
#2.   Multiplicacion

listaRandom=[1,2,3,4,5]
listaTota=lista+listaRandom
print(listaRandom)
print(lista*3)

lista=["hola",1,2,3,4,"carlos","Roberto",1.3,1.24]


"Recorre una lista "



