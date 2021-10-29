"""
FOR 

-Iteraciones, conocemos el numero de veces que se repite 
- Repetir proceso n veces 
- Recorrer listas (Estructuras de datos)

"""



nombre= "Johan"
 
print(range(5)) #rango ---> (5)--> (0,1,2,3,4)

for i in range(3):  #(3)
    nombre=input("Ingrese un nombre: ")
    print(i)  # te da el indice segun el rango
    

for i in "Johan":
    print(i)

#3 tipos de for
print()
print()
lista=["Johan", "Melany","Katherine"]
#Por elemento  for variale in LISTA:   --> TENGO QUE IMPRIMIR, CUANDO TENGO UNA SOLA LISTA 
for i in lista:
    print(i)

#Por indice  #LISTAS PARALELAS ---> 2 o mas listas que tienen la misma longitud y tienen relacion 
# y me pidan buscar un elemento de una lista segun la otra lista

for i in range(len(lista)):  #for i  in range(len(LISTA))
    print(lista[i])




nombres=["Juan","Jose","Julio"]
calificaciones=[9,10,8.5]

for i in range(len(lista)):
    nombre=nombres[i]
    calificacion= calificaciones[i]
    print("El nombre del alumno es {} y su califiacion es {}".format(nombre,calificacione))

# EL NOMBRE DEL ALUMNO ES JUAN Y SU CALIFICACION ES 9 
# EL NOMBRE DEL ALUMNO ES JOSE Y SU CALIFICACION ES 10 

#cuando el profesor lo pida explicitamente 
for i,nombre in enumerate(nombres):
    print(i+1,nombre,calificaciones[i])
    #1 Juan 
    #2 Jose 
    #3 Julio








