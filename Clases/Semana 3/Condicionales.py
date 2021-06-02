# edad=18
# # Si es mayor de edad puede tomar, sino toma jugo 

# if edad>= 18:
#     print("es mayor de edad")
#     print("Toma alcohol")
#     #SE CUMPLE TODO LO VERDADERO
# else: #EN CASO contrario
#     print("No es mayor de edad")
#     #SE CUMPLE SI LA CONDICION ES FALSA
#     print("Toma jugo")



# #Quiero verificar si el numero es 2 o mayor o menor
# numero = 5 
# if numero==2:
#     print("Numero es igual a 2")
# elif numero<2:
#     print("El numero es menor a 2")
# else:#el numeor es mayor a 2  --->numero>2
#     print("El numero es mayor a 2")


print("************************")
print("* Condiciones *")
print("************************")

#El sistema de identificación de aduanas requiere ciertos datos del pasajero:
#Nombres completos, número de cédula, edad, cantidad de dinero en efectivo, número de pasajeros que le acompaña


#Agrega las líneas de código para ingresar el nombre completo y la cédula.
nombre = input("Escriba su nombre:")
cedula= input("cedula:")
edad = int(input("edad: "))  #string 18 
dinero = float( input("dinero en efectivo:"))
pasajeros= int(input("pasajeros: "))

#Muestra el contenido de las variables nombresCompletos y cedula
print("Nombres completos del viajero:", nombre)
print("C.C.: ", cedula)


#¿La cantidad de dinero en efectivo supere los 5000.10 dólares? Utiliza la variable dineroEfectivo y el operador relacional adecuado para asignar el resultado en la variable declaracionPorEscrito. 

#En caso de que supere el valor, se le debe cobrar iva  
# declaracionPorEscrito =

if  dinero>5000.10:  #if boolean
    iva= dinero*0.12
    dinero-=iva
    print("Se le esta cobrando iva...")

#Ademas muestre un mensaje que indique si el numero de pasajeros es par o impar 

if pasajeros%2==0:
    print("El numero de pasajeros es par")
else: #caso contrario
    print("El numero de pasajeros es impar")
    


#Muestra el contenido de las variables edad, dineroEfectivo y pasajeros. Utiliza un mensaje adecuado.
print("La edad del pasajero es {} \nSu dinero en efectivo es {} \nNumero de pasajeros {}".format(edad,dinero,pasajeros))

print("----" * 10)
print(" Sistema de Identificación de Aduanas")
print("----" * 10)

