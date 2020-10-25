#Escriba la salida por pantalla de cada resultado

a= '4'
b = 4
# c=a+b
# print(c)  #error


c =10

c +=10

# print(c)  #

# print(3*'perreo'+2*'gato')


# print(5!=5 or 7>=5) 
# True or True ==1
#False or True ==1
#False or False







a=5
b=2
c=4

c= c%(a+b)
# 4 % (7) 
# print(c)
#3 El siguiente programa sirve para convertir grados Farenheit a grados Centígrados 
# gradosFahrenheit = float(input("Ingrese en grados F: "))

#La fórmula de conversión a grados Centígrados es la siguiente https://goo.gl/ojmwyh  
# gradosCentigrados = (gradosFahrenheit-32)/1.80
# print(gradosCentigrados)

#4 El siguiente programa sirve para convertir los hora a minutos


#5 Escriba un programa que permita al usuario ingresar las medidas del cateto a y b de un triángulo rectángulo, su programa deberá calcular la hipotenusa c del triángulo a partir de la fórmula del teorema de Pitágoras. hi = 
# catetoA= int(input("Ingrese el cateto a:"))
# catetoB= int(input("Ingrese el cateto a:"))
# # hipotenusa= (catetoA**2 )+ (catetoB**2)
# # hipotenusa =  hipotenusa ** (1/2)
# hipotenusa = ((catetoA**2 )+ (catetoB**2)) ** (1/2)
# print("La hipotenusa del triangulo es: %.2f"%(hipotenusa))



#5 Un número narcicista es aquel que es igual a la suma de sus dígitos elevados a la potencia de su número de cifras. Su nombre se debe a lo mucho que parece "quererse a sí mismos". 
numero= 153
numero = str(numero)
firstD= numero[0]
middleD= numero[1]
lastD= numero[2]


#Utilice el número 153 
#Cambia el valor de la variable numero por 370,143, 321, 371, 389 y 407

#Separar el numero en unidades, decenas y centenas

#Elevar las uniddes, las decenas y las centenas al cubo
firstElevado = int(firstD)**3
middleElevado = int(middleD)**3
lastElevado = int(lastD)**3


#Asigna la suma de los valores unidadescubo, decenascubo y centenascubo a total
sumaTotal= firstElevado+middleElevado+lastElevado

#¿numero es igual que total? Asigna el resultado de la comparación en 
esNarcicista =sumaTotal==int(numero)


#Muestra el resultado
print("¿numero es igual que total? {}".format(esNarcicista) )



#6 Escribir un programa en Python que permita el ingreso de un número, asumir que el usuario siempre ingresará 3 cifras, deberá mostrar por pantalla True si cumple las siguientes condiciones:
#  El primer número es mayor que el último número, pero menor que el segundo
# Al menos un número es par
