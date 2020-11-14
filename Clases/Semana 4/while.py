#Programa 002-Tipos de datos

print("************************")
print("* WHILE *")
print("************************")


#Se desea crear un sistema de facturación en un restaurante por cliente

#Solicite el nombre del cliente y el numero de tarjeta de credito/debito
#Adicional el cliente debe ingresar la fecha de caducidad de su tarjeta de credito/debito mientras el usuario no ingrese una fecha correcta deberá solicitar otra tarjeta 
#Nota: una tarjeta es valida si no ha caducado y contiene un mes valido 
nombre= input("Ingrese un nombre: ")
tarjeta= input("Ingrese una tarjeta:")
fechaTarjeta= input("Ingrese la fecha de caducidad: ") # 01/2020
#13/2020 #1/2019 #10/2020N ES LA VALIDO
fecha= fechaTarjeta.split("/") # ["01","2020" ]
mes= int(fecha[0])  #01
year= int(fecha[1])# 2021
esValido = 1<=mes<=12 and year>2020 #TRUE O FALSE

while not esValido: #es verdadero 
    fechaTarjeta= input("Ingrese una fecha correcta: ") #1/2022
    fecha= fechaTarjeta.split("/") # ["01","2020" ]
    mes= int(fecha[0])  #01
    year= int(fecha[1])# 2020
    esValido = 1<=mes<=12 and year>2020 #TRUE O FALSE



#Ademas el usuario posee una cuenta que se deberá incrementar siempre y cuando el cliente quiera seguir consumiendo productos en el local 

encebollado = 2,5 
gaseosa= 0,9

#realice un programa que aumente la cuenta cada vez que el cliente desee permanecer en el resturante 
# Pregunte si el usuario desea continuar en el restaurante

