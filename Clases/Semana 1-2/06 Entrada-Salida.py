#Programa 006-EntradaSalida

print("************************")
print("* 006 - Entrada/Salida *")
print("************************")

#El sistema de identificación de aduanas requiere ciertos datos del pasajero:
#Nombres completos, número de cédula, edad, cantidad de dinero en efectivo, número de pasajeros que le acompaña

#Agrega las líneas de código para ingresar el nombre completo y la cédula.
#el usuario ingrese, ingrese por pantalla, o pida 
nombresCompletos =  input("Ingrese su nombre completo: ") #STRING 
cedula = input("Ingrese su cedula: ") #STRING 
#Los enteros NO comienzan con 0 




#Agrega las líneas de código para ingresar los datos que necesita el sistema de aduanas(edad, dinero en efectivo y el numero de pasajeros).
edad= input("Ingrese su edad: ")#STRING
dineroEfectivo= input("Ingrese su dinero en efectivo: ")
numeroPasajero = input("Ingrese el numero de pasajeros: ")
#Muestra el contenido de las variables edad, dineroEfectivo y pasajeros. Utiliza un mensaje adecuado.




#SIEMPRE CAMBIAR EL TIPO DE DATO QUE SEA LA VARIABLES
edad=int(edad)
dineroEfectivo= float(dineroEfectivo)
numeroPasajero=int(numeroPasajero)



print("El nombre completo es: %s y su cedula es %s, La edad del pasajero es %s, su dinero en efectivo %f"%(nombresCompletos,cedula,edad,dineroEfectivo))


print("El nombre completo es: {} y su cedula es {}, \n\tLa edad del pasajero es {}, \n\tsu dinero en efectivo {}".format(nombresCompletos,cedula,edad,dineroEfectivo))

