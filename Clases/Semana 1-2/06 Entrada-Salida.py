#Programa 006-EntradaSalida

print("************************")
print("* 006 - Entrada/Salida *")
print("************************")

#El sistema de identificación de aduanas requiere ciertos datos del pasajero:
#Nombres completos, número de cédula, edad, cantidad de dinero en efectivo, número de pasajeros que le acompaña

#Agrega las líneas de código para ingresar el nombre completo y la cédula.

nombresCompletos = input("INGRESE SU NOMBRE COMPLETO:")
cedula =input("INGRESE SU NUMERO DE CEDULA:")

#Muestra el contenido de las variables nombresCompletos y cedula
print("Nombres completos del viajero: ", nombresCompletos)
print("C.C.: ", cedula)

#Agrega las líneas de código para ingresar los datos que necesita el sistema de aduanas.


#Muestra el contenido de las variables edad, dineroEfectivo y pasajeros. Utiliza un mensaje adecuado.
print("Su edad es %d \nSu dinero en efectivo es %.2f \nSu dinero en efectivo es %d"%(edad,dineroEfectivo,pasajeros))

print("----" * 10)
print(" Sistema de Identificación de Aduanas")
print("----" * 10)

#¿La cantidad de dinero en efectivo supere los 5000.10 dólares? Utiliza la variable dineroEfectivo y el operador relacional adecuado para asignar el resultado en la variable declaracionPorEscrito.  
declaracionPorEscrito = dineroEfectivo>=5000.10

#Muestra por pantalla los siguientes mensajes. 
#Nota: El texto que encuentras entre los símbolos <> hacen referencia a las variables que ingresaste previamente por teclado.
print("¿numero es igual que total? {}".format(cedula) )
print("¡Bienvenid@ %s, C.C. %s, con %d años!"%(nombresCompletos,cedula,edad))
print("¿Debe hacer una declaración por escrito?", declaracionPorEscrito,"\n¡Ud y los %d tenga un buen viaje!"%(pasajeros))

