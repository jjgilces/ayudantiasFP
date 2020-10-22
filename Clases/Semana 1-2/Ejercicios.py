#Escriba la salida por pantalla de cada resultado

a= '4'
b = 4
c=a+b
#print(c)



c =3
c+= 10
# print(c)

print(3*'perreo'+2*'gato')

print(5==5 or 7>=5)

a=5
b=2
c=4
c %=a+b
print(c)

#2 Escriba un programa que permita al usuario ingresar las medidas del cateto a y b de un triángulo rectángulo, suprograma deberá calcular la hipotenusa c del triángulo a partir de la fórmula del teorema de Pitágoras.


#3 El siguiente programa sirve para convertir grados Farenheit a grados Centígrados 
gradosFahrenheit = 30
#La fórmula de conversión a grados Centígrados es la siguiente https://goo.gl/ojmwyh
gradosCentigrados = (gradosFahrenheit-32)/1.80


#4 El siguiente programa sirve para convertir los minutos en horas


#5 Un número narcicista es aquel que es igual a la suma de sus dígitos elevados a la potencia de su número de cifras. Su nombre se debe a lo mucho que parece "quererse a sí mismos". 

#Utilice el número 153 
#Cambia el valor de la variable numero por 370,143, 321, 371, 389 y 407
numero = 370
numeros= str(numero)
#Separar el numero en unidades, decenas y centenas
unidades = numeros[-1]
decenas = numeros[-2]
centenas = numeros[-3]
#Elevar las uniddes, las decenas y las centenas al cubo
unidadescubo = int(unidades)**3
decenascubo = int(decenas)**3
centenascubo = int(centenas)**3

#Asigna la suma de los valores unidadescubo, decenascubo y centenascubo a total
total= unidadescubo+decenascubo+centenascubo

#¿numero es igual que total? Asigna el resultado de la comparación en esNarcicista
esNarcicista = numero==total

#Muestra el resultado
print("¿numero es igual que total? {}".format(esNarcicista) )



#6 Escribir un programa en Python que permita el ingreso de un número, asumir que el usuario siempre ingresará 3 cifras, deberá mostrar por pantalla True si cumple las siguientes condiciones:
#  El primer número es mayor que el último número, pero menor que el segundo
# Al menos un número es par
