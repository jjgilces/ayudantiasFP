"""
LISTAS 
Carateristicas:
1.   Mutables  --> cambian
2.   Permite cualquier tipo de dato --> 
3.   Son ordenadas
"""
## Creación de listas vacias
lista =[]
lista2= list()

##Crear una lista --> a partir de un string

nombres="Johan Jair Gilces Reyes" #identifico lo que me esta molestando 
lista3= nombres.split()  

ingredientes="tomate, cebolla ,pimiento,arroz" 

lista4= nombres.split(",")
fecha= "4/7/2022"

lista_fecha= fecha.split("/")

lista=[]


##Añadir elementos : append e insert 

"""Busqueda en listas"""
print(lista)
lista =[2,4,6]
indice= lista.index(4)   #1
print(indice)
elemento=lista[indice]
print(elemento)
#find --> -1 si no encuentra el elemento


"""Ordenamiento"""
lista =[2,4,10,1,4,6]

listaOrdenada=lista.sort()
#mayor a menor 
listaOrdenada= listaOrdenada[::-1]


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









