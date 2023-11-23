"""
LISTAS 
Carateristicas:
1.   Mutables  --> cambian
2.   Permite cualquier tipo de dato --> 
3.   Son ordenadas
"""
## Creación de listas vacias


##Crear una lista --> a partir de un string

nombres="Johan Jair Gilces Reyes" #identifico lo que me esta molestando 
lista3= nombres.split()  

ingredientes="tomate, cebolla ,pimiento,arroz" 

lista4= nombres.split(",")
fecha= "4/7/2022"

lista_fecha= fecha.split()

lista=[]


##Añadir elementos : append e insert 

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









