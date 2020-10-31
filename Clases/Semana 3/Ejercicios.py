from random as rd
# Escriba un programa que lea por teclado un correo electrónico. Luego, deberá mostrar un mensaje indicando si es un correo comercial o no. Un correo comercial se identifica porque
# termina por “gmail.com”, “hotmail.com” o “live.com” 
correo= "johanjairgr@hotmail.com"
lista = correo.split("@")
dominio= lista[-1]
condicion = dominio =="gmail.com" or dominio =="hotmail.com" 
condicion2= correo.endswith("gmail.com") or correo.endswith("hotmail.com")
condicion3 = ("gmail.com" in lista) or ("hotmail.com" in lista)

print(condicion,condicion2,condicion3)





# dado1 = randint( 2, 15 )
# print(dado1)
# dado2 = randint( 3, 15 )
# nombre = input("Ingrese su nombre:" )
# adivinanza = input( "Ingrese el valor del dado:")
# puntaje = 0
# if dado1 == adivinanza:
#  print("Acabas de adivinar el primer dado")
#  puntaje = puntaje + 10
# if dado2 == adivinanza:
#  print("Acabas de adivinar el segundo dado")
#  puntaje = puntaje + 10
# print("{} tu puntaje {}".format( nombre, puntaje ))


# Escribir un programa que almacene en una lista los
# siguientes precios, 50, 75, 46, 22, 80, 65, 8, y
# muestre por pantalla el menor y el mayor de los
# precios, ademas eliminelos de la lista original.
lista=[50, 75, 46, 22, 80, 65, 8]
max= max(lista)
min = min(lista)
print(max,min)
print(lista)
lista.remove(max)
lista.remove(min)
print(lista)



# Se tiene la siguiente lista de calificaciones y nombres:
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
# Solicite dos números.  El primer número entre 1 y 10 y el segundo entre 10 y 20. Genere una lista con los números en el rango ingresado.  Asuma que el usuario va a ingresar un número en el rango indicado.  Presente la lista.
