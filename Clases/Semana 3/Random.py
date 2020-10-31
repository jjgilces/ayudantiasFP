import random as rd


calificaciones=[7,5,3,10]
nombres=["Carlos Loja","Javier Guevara","Robert Ruiz","Camila Ramirez"]
# Se pide mostrar por pantalla si el estudiante aprobo o no(Aprueba si su calificacion es mayor a 6), de la siguiente 
# forma:
# "El estudiante Carlos Loja ha aprobado"
# "El estudiante Javier Guevara ha reprobado"
#Escoga un estudiante al azar 
cantidad= len(nombres)
numAl= rd.randint(0,cantidad-1)

calificacion= calificaciones[numAl]
nombre= nombres[numAl]
if calificacion >6:
    print("El estudiante {} ha aprobado".format(nombre))
else:
    print("El estudiante {} NO  ha aprobado".format(nombre))
