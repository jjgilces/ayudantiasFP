"""
LISTAS 
Carateristicas:
1.   Mutables  --> cambian
2.   Permite cualquier tipo de dato --> 
"""
## Creación de listas vacias

lista2= list()

##Crear una lista --> a partir de un string

nombres="Johan Jair Gilces Reyes" #identifico lo que me esta molestando 
lista3= nombres.split()  # nombres.split(" ")  ---> ["Johan", "Jair","Gilces", "Reyes"]  en string pero separados por comas
ingredientes="tomate, cebolla ,pimiento,arroz" 
#cuando yo quiero convertir un string a lista (uso split)
lista4= nombres.split(",")
fecha= "4/7/2022"
lista_fecha= fecha.split("/")

lista=[]


##Añadir elementos 
lista.append(1)  #[1]  append--> siempre agrega al final
lista.append(1)  #[1,1]
lista.append(2)  #[1,1,2]
lista.insert(0,4)  #[4,1,1,2,4]
lista.insert(-1,4)

 #[4,1,1,2,4]
"""Busqueda en listas"""
print(lista)
indice= lista.index(4)   #0
print(indice)
elemento=lista[indice]
print(elemento)



"""Ordenamiento"""
lista.sort()
print(lista)#[1,1,2,4,4]
#de pequeño a más grande
#top 3 
lista.sort(reverse=True) #[4,4,2,1,1]


"""Invertir una lista"""
lista=lista[::-1]  #[4,4,2,1,1]  de mayor a menor 

#si me piden ordenar de manera ascendente --> menor a mayor 
lista.sort()
#si me piden ordenar de manera descendente --> mayor a menor
lista.sort()
lista=lista[::-1] 

"""Cambio de elementos"""
lista[0]=6
print(lista)
lista[-1]=10
print(lista)

'''Eliminar un elemento'''
lista.pop(2)  #elimina segun el indice   
print(lista)
lista.remove(4) # elimina por elemento 
print(lista)

## Operaciones de Listas

#1.   Suma  -->concatenacion
#2.   Multiplicacion

listaRandom=[1,2,3,4,5]
listaTota=lista+listaRandom#[4,4,2,1,1,1,2,3,4,5]
print(listaRandom)
print(lista*3)#[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

lista=["hola",1,2,3,4,"carlos","Roberto",1.3,1.24]








