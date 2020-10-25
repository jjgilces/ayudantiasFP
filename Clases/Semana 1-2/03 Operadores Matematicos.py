#Programa 003-OperadoresMatemáticos

print("********************************")
print("* 003 - Operadores Matemáticos *")
print("********************************")

#Nos vamos todos de viaje, encontrarás el número total de pasajeros en numeroPasajeros

numeroPasajeros= 5

#Calcula y asigna el subtotal a pagar en la variable subtotalAPagar. Para esto,  el valor de los pasajes es de $2.50.  
subtotalAPagar= numeroPasajeros*2.5

print ("Subtotal a pagar es:", subtotalAPagar)

#Calcula el ivaAPagar al multiplicar el subtotalAPagar por 12 y dividido para 100. 

ivaAPagar= (subtotalAPagar*12)/100


#Finalmente, obtén el total al pagar en totalAPagar con la suma del subtotalAPagar y el ivaAPagar.
totalAPagar=subtotalAPagar+ivaAPagar


#Muestra en orden el valor de cada una de las variables anteriores.

print("* Emisión de Boletos Aéreos *")
print('total a pagar', totalAPagar)


#Al parecer nos hemos ganado algunos boletos gratis según la promoción del mes
#  "Recibe 1 boleto gratis por cada 6 boletos comprados"

#Calcula y asigna el número de boletos gratis en la variable 
boletosPromocion= numeroPasajeros//6


print("Boletos por promoción:")
print(boletosPromocion)