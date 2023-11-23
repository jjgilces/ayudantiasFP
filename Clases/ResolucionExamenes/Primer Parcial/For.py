# 2 tipos de for 

precios = [2,3,4,5,76,2]
nombre= ["ARROZ","LECHE","HUEVOS","PAN","AJO"]
for elemento in lista:
    print(elemento)

#listas paralelas
#IMPRIMA LOS PRODUCTOS QUE TENGAN UN COSTO MAYOR A $4
for i in range(len(lista)):
    precio = precios[i]
    nombre = nombres[i]
    if precio>4:
        print(nombre)



#primer elemento 
lista[0]


#ultimo elemento 
lista[-1]