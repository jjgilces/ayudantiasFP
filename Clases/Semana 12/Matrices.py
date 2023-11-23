#Importar Numpy 
import numpy as np

#Vector 
#Listas pero con un solo tipo (No tienen coma ) 
lista=[1,2,3,4]

vector2= np.array(["A","B", "C"])
vector1= np.array(lista)
print(vector1)
print(vector1.max())
print(vector2)
print()
vector3 = np.array(["A","1",2,2.0])  #Los convierte a string
print(vector3)
#Matriz
matriz= np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])
print(matriz)
#Ejercicio matematicos 

#CONOCER FILAS Y COLUMNAS 

print(matriz.shape) #es una tupla (fila, columna)
# FILAS PRIMERO Y LUEGO COLUMNAS
print(matriz[0])
print(matriz[1])
print(matriz[2,1])


# #DATOS NUMERICOS 
pesos=[40,60,70]
altura=[167,160,132]
# imc= #peso *2 /altura
imcs=[]
for i in range(len(pesos)):
    imc= pesos[i]*altura[i]
    imcs.append(imcs)
vectorPeso= np.array(pesos)
vectorAltura= np.array(altura)
vectorICM= vectorPeso* vectorAltura
print(vectorICM)
#suma de vectores
sumaVector= vectorPeso+vectorAltura

# COMO CREO UN VECTOR CON 5 CEROS 
vectorCeros= np.zeros(5)
print(vectorCeros)
matrizCeros= np.zeros((3,3))
print(matrizCeros)
# COMO CREO UN VECTOR CON 5 unos 
vectorUnos= np.ones(5)
print(vectorUnos)

# COMO CREO UN VECTOR/MATRIZ CON 5 NUMERO ALEATORIOS del 1 al 10
aleatorio= np.random.randint(1,10,5)
print(aleatorio)
maleatorio= np.random.randint(1,10,(3,3))
print(maleatorio)


#OPERACIONES DE FILAS Y COLUMNAS 

M= np.random.randint(8,100,(3,5))
print(M)
#calcular el total de ventas del dia lunes
sumaPorDia= np.sum(M,axis=0)
print(sumaPorDia)
print("El total del dia lunes es: ",sumaPorDia[0])

vectorLunes= M[:,0]
print(vectorLunes)
print("El total del dia lunes es: ",vectorLunes.sum())

#el total de ventas de la semana que obtuvo los electrodomesticos 

vectorCategoria=np.sum(M,axis=1)
totalElectro= vectorCategoria[1]
print("El total del electrodomesticos es: ",totalElectro)


# Vector Boolean
print()
print(sumaPorDia)# el total de ventas por cada dia 
dias=["Lunes","Martes","Miercoles","Jueves","Viernes"]

#cuantos dias de la semana han vendido mas de 125
booleano=sumaPorDia>125
print(booleano)
print(booleano.sum())

vectorDias= np.array(dias)
cumplen= vectorDias[booleano]
print(cumplen)






# Presente los numeros mayores a 10
print(sumaVector)
condicion= sumaVector>210
resultado= sumaVector[condicion]  #Matriz que cumple esa condición 
print(resultado)
condicion= sumaVector%2==0  #NUMEROS PARES
resultado= sumaVector[condicion]  #Matriz que cumple esa condición 
print(resultado)






#Operaciones con Matrices

# print(promedio)
