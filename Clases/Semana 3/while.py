
"""

WHILE

- No se conoce cuando va a terminar el ciclo 
- Se usa para realizar validaciones, hacer videojuegos 
- Tener cuidado de no hacer un ciclo infinito 

"""
print("************************")
print("* WHILE *")
print("************************")



#Ademas el usuario posee una cuenta que se deberá incrementar siempre y cuando el cliente quiera seguir consumiendo productos en el local 

encebollado = 2.5 
gaseosa= 0.9

#realice un programa que aumente la cuenta cada vez que el cliente desee permanecer en el resturante 
# Pregunte si el usuario desea continuar en el restaurante

"""
# opcion=input("Desea continuar comprando(SI/NO):")
# total=0
total= encebollado+gaseosa
opcion= input("Desea continuar comiendo: ")#SI/NO  SI ---> DEBO SUMARLE MAS A LA CUENTA
while opcion=="SI": #False--> ya no entra al while
    total+=encebollado+gaseosa
    opcion= input("Desea continuar comiendo: ")  #NO 
    print(total)

opcion="SI"
while opcion=="SI": #False--> ya no entra al while
    total+=total
    opcion= input("Desea continuar comiendo: ")  #NO 
    print(total)
"""
#banderas---> dentro del while nosotros vamos a verificar si se cumple ---> True or False


#validar si es un digito y si es mayor a 2 
esValido=False

while not esValido: 
    numero = input("Ingrese un numero mayor a 2: ")  #jsjfkf
    if numero.isdigit(): 
        if int(numero)>2: 
            esValido=True

#SI mi bandera es true, el while va a terminar cuando esa variable sea false


"""






opcion="SI"
while opcion=="SI":
    total+= float(encebollado)+float(gaseosa)
    opcion=input("Desea continuar comprando(SI/NO):")
    print(total)

#1) YO tengo que hacer que entre 

#cree un menu, muestre el menu hasta que el usuario escoja la opcion salir 
print("1)Mostrar bienvenida\n2)Imprimir un numero\n3)Sumar l cuenta4)Salir")
print("1) mostr")
print("2)")
opcion=input("Ingrese una opcion: ")

while opcion!="4":
    if opcion=="1":
        print("\tHola, bienvenido al restaurante")
    elif opcion=="2":
        print(13)
    print("1)Mostrar bienvenida\n2)Imprimir un numero\n3)Salir")   
    opcion=input("Ingrese una nueva opcion: ")

nombre=input("Ingrese un nombre:")
#vuelva a pedir el nombre si no comienza con mayuscula
while not nombre.isupper():
    nombre=input("Ingrese un nombre con letra mayuscula :")

numero=input("Ingrese un numero"):


#valida si o 

# Escriba un programa en Python que pida por consola un número entero positivo, a partir del cual se mostrarán por pantalla los múltiplos de dicho número hasta el 100



# Solicitar el ingreso de un numero del 1 al 10 y permitirle al usuario ingresarle la 
# cantidad de veces necesarias para que adivine el numero que la computadora ha escogido.

"""