# Escribir un programa en Python que solicite un número por teclado y muestre True sí el número se encuentra bajo las siguientes condiciones: 
# El número debe estar entre 25 y 60 sin incluir el 40 ó entre -20 y -40 sin incluir el -30; además el número debe ser divisible para 2 y elevado al cuadrado debe ser menor que 1000.

# num = int(input("Ingrese un numero: "))
# El número debe estar entre 25 y 60 sin incluir el 40
#
condicion1= (25<num<60) and num !=40
#  entre -20 y -40 sin incluir el -30
condicion2 =num>-20 and num<-40 and num !=-30
#numero divisible para 2 //numero es par
condicion3= (num % 2==0)
#
condicion4= (num**2)<1000

condicionTotal =(condicion1 or condicion2 ) and (condicion3 and condicion4)
print("El numero es par",condicionTotal)



# Escriba un programa que reciba una dirección web y verifique si es de dominio educativo o no.
# Para que una dirección web sea de dominio educativo y correcta debe de comenzar con “www” y tener “.edu” en la dirección al final o previo al dominio del país. 
direccion= "www.espol.fiec.edu"  # www  espol  fiec  edu   ec
lista= direccion.split(".")
# print(lista)
condicion1= lista[0]=="www"
condicion2= "edu" in lista
condicionT= condicion1 and condicion2
# print(condicionT)
 

#Elabore un programa que reciba los nombres y las edades de 3 estudiantes por teclado (Se recomienda usar una lista para las edades y otra para los nombres). En su programa las listas empiezan vacías y se van llenando con lo que el usuario ingresa por teclado. Muestre por pantalla lo siguiente:
# •	Cuál es el estudiante con mayor edad.
# •	Cuál es el estudiante con menor edad.
# •	Cuál es el promedio de edad de todos los estudiantes.
nombres=[]
edades=[]
# nombre1 = input("Ingrese un nombre:")
# nombre2 = input("Ingrese un nombre:")
# nombre3 = input("Ingrese un nombre:")
# nombres.append(nombre1)
# nombres.append(nombre2)
# nombres.append(nombre3)

# edad1 = int(input("Ingrese un edad:"))
# edad2 = int(input("Ingrese un edad:"))
# edad3 = int(input("Ingrese un edad:"))
# edades.append(edad1)
# edades.append(edad2)
# edades.append(edad3)

# nombresE= input("Ingrese los nombres separados por coma: ")
# edadesE= input("Ingrese las edades separadas por coma:")
#edades= edadesE.split(",")
nombres= ["Johan","Gabriel", "Melany"]
edades= [18,20,25]
edadMax= max(edades)
edadMin= min(edades)
indiceMax= edades.index(edadMax)
nombreMayor = nombres[indiceMax]
sumaTotal= sum(edades)
cantidad= len(edades)
promedio = sumaTotal/cantidad
print(promedio)



# Elabore un programa que reciba por teclado una hora en formato hh:mm:ss. El programa procede a presentar por teclado el total de segundos que contiene la hora. 
hora = "1:20:5"
tiempo = hora.split(":")
segundos= int(tiempo[-1])
minutos = int(tiempo[1])*60
horas= int(tiempo[0])*3600
seguntosTotales= segundos+minutos+horas
print(segun)
print(seguntosTotales)