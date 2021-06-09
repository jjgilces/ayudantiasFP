#Programa 002-Tipos de datos

print("************************")
print("* WHILE *")
print("************************")


#Se desea crear un sistema de facturación en un restaurante por cliente

#Solicite el nombre del cliente y el numero de tarjeta de credito/debito
#Adicional el cliente debe ingresar la fecha de caducidad de su tarjeta de credito/debito mientras el usuario no ingrese una fecha correcta deberá solicitar otra tarjeta 
# #Nota: una tarjeta es valida si no ha caducado y contiene un mes valido 
# nombre= input("Ingrese un nombre: ")
# tarjeta= input("Ingrese una tarjeta:")
fechaTarjeta= input("Ingrese la fecha de caducidad: ") # 01/2020
#13/2021 #1/2021 #10/2021 ES LA VALIDO
#02/2019 no valido
#13/2021 no valido
fecha= fechaTarjeta.split("/") #["02","2020"]
mes=int(fecha[0])
anio=int(fecha[1])
mes_valido= mes>=1 and mes<=12  # 1<= mes<=12
no_caducado= anio>2021
condicion= mes_valido and no_caducado #boolea true or false

while not condicion:
    fechaTarjeta= input("Ingresaste una fecha incorrecta\nIngrese de nuevo la fecha de caducidad: ") # 01/2020
    fecha= fechaTarjeta.split("/") #["01","2020"]
    mes=int(fecha[0])
    anio=int(fecha[1])
    mes_valido= mes>=1 and mes<=12  # 1<= mes<=12
    no_caducado= anio>2021
    condicion= mes_valido and no_caducado


#Ademas el usuario posee una cuenta que se deberá incrementar siempre y cuando el cliente quiera seguir consumiendo productos en el local 

encebollado = 2.5 
gaseosa= 0.9

#realice un programa que aumente la cuenta cada vez que el cliente desee permanecer en el resturante 
# Pregunte si el usuario desea continuar en el restaurante


# opcion=input("Desea continuar comprando(SI/NO):")
# total=0
while opcion=="SI":
    total+= float(encebollado)+float(gaseosa)
    opcion=input("Desea continuar comprando(SI/NO):")
    print(total)


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