# diccionarios, archivos y matrices --> medio/facil 
import numpy as np 


#vector --> lista 
ancho=[1,2,3,4]
vector = np.array(ancho)
print(vector)
# lista != vector --> no se puede modificar

alto= [2,2,2,2]
vector_alto= np.array(alto)
metrosCuadrados=  vector_alto * vector
print(metrosCuadrados)




#MATRIZ 

matriz = np.array([[1,2,3],[2,2,2],[0,0,0],[2,4,6]])
print(matriz)

print(matriz.shape) # fila, columnas



 # crea r matriz 
matrizCeros = np.zeros((4,3))
print(matrizCeros)

matrizCeros[1,2]= 10 
print(matrizCeros)

ESTUDIANTES = np.array([[2,10],[2,8],[6,6]])
print(ESTUDIANTES)
totalPorGenero = np.sum(ESTUDIANTES,axis=0) # vector 
print(totalPorGenero)

cantidadMujeres= totalPorGenero[0]
print(cantidadMujeres)




