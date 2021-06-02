nombre= "Johan"
 
print(range(5))


for i in range(5):  #(0,1,2,3,4)
    print(i)
    

for i in "Johan":
    print(i)

#2 tipos de for
print()
print()
lista=["Johan", "Melany","Katherine"]
#Por elemento
for i in lista:
    print(i)

#Por indice  #LISTAS PARALELAS 
for i in range(len(lista)):
    print(lista[i])

nombres=["Juan","Jose","Julio"]
calificaciones=[9,10,8.5]

for i in range(len(lista)):
    print("El nombre del alumno es {} y su califiacion es {}".format(nombres[i],calificaciones[i]))

# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# palabra= input("Ingrese una palabra")
# print(palabra)
# print()
# for i in range(10):
#     print(palabra)

for i,nombre in enumerate(nombres):
    print(i,nombre,calificaciones[i])










