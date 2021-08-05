#Importar Numpy 

import numpy as np
#Vector 
#[ 10   20    30   ]
#Listas pero con un solo tipo (No tienen coma ) 
lista=[1,2,3,4]

vector2= np.array(["A","B", "C"])

print(vector2)

vector3 = np.array(["A","1",2,2.0])  #Los convierte a string
print(vector3)
#Matriz
matriz= np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])
print(matriz)
#Ejercicio matematicos 
print(matriz.shape)

#CONOCER FILAS Y COLUMNAS 
dimension =matriz.shape

# FILAS PRIMERO Y LUEGO COLUMNAS
filas=dimension[0]  #Filas 
columna= dimension[1]

print(matriz.size)

# vector  = np.array(lista)
# vector4 = np.array([7,7,7,7])

# #DATOS NUMERICOS 
# print(vector)
# print(vector4)
# sumaVector= vector+vector4
#  #Matriz Boolean
# print(sumaVector)
# print(sumaVector>9)
# #Indexación Boolean 
# #Matriz[condicion]
# #Presente los numeros mayores a 10
# condicion= sumaVector>10
# resultado= sumaVector[condicion]  #Matriz que cumple esa condición 
# print(resultado)
# #Presente los numeros mayores a 10
# condicion= sumaVector%2==0  #NUMEROS PARES
# resultado= sumaVector[condicion]  #Matriz que cumple esa condición 
# print(resultado)


# #COMO CREO UN VECTOR CON 5 CEROS 
# ceros=np.zeros(5)
# print(ceros) 

# #COMO CREO UN VECTOR CON 5 unos 
# ceros=np.ones(5)
# print(ceros) 

# #COMO CREO UN VECTOR CON 5 NUMERO ALEATORIOS del 1 al 10
# aleatorio= np.random.randint(1,10,5)#inicion, fin, shapw
# print(aleatorio)

# matrizCeros=np.random.randint(1,10,(3,3))
# print(matrizCeros)



#Operaciones con Matrices
print(matriz)
sumaColumnas= np.sum(matriz,axis=0)
print(sumaColumnas)

sumaFilas= np.sum(matriz,axis=1)
print(sumaFilas)

promedio=np.mean(matriz)
# print(promedio)

print()
print(matriz[1])  #INDEXA POR FILAAAA
print()
print(matriz[1,1])
print(matriz[1:3,1:3])
print(matriz[1:3,0:2])
print()
print(matriz[1::2,0])