#par o impar
numero = 4
isPar = numero  % 2 ==0  #un numero es par
isImpar = numero % 2 !=0 #un numero es impart

#yo quiero saber si un numero si un numro es divisible para 5
numero=13
divisible5= numero%5==0

#promedio en listas
lista=(1,2,3,4)
#sum -len
promedio= sum(lista)/len(lista)

#recorrer 2 listas paralelas

#quieor obtener EL NOMBRE de quien obtuvo la QUIENES TIENEN MAYOR A 6 (promedio)
nombres=["Johan","PEPE"]
cantidades=[10,100]
pesos=[65,72.5]
nombresSOBREPES=[]
for i in range(len(nombres)):  #
    #0
    nombre = nombres[i]
    cantidad = cantidades[i]
    peso= pesos[i]
    if cantidad<0 and peso>60: 
        nombresSOBREPES.append(nombre)

nombresSOBREPES= tuple(nombresSOBREPES)
conjuntoSobrepeso= set(nombresSOBREPES)

numeros=[10,12,13]
print(numeros[2])
#elementos unicos en una lista
paises=["Ecuador", "Peru","Colombia", "Peru", "Argentina","Colombia"]
# paisesSinR=[]
# for i in paises:
#     if i not in paisesSinR:
#         paisesSinR.append(i)

#elemento UNICOS, SIN REPETIR, 
print(paises)
listaUnicosPaises= list(set(paises))
print(listaUnicosPaises)
# print(paisesSinR)



#recorrer cuando se cuantas veces debo hacer algo 



    # print(i)
    #0,1,2



#recorrer cuando no se cuantas
#pida numeros hasta que el numero sea o el numero sea negativo 



#validar --> if ---> WHILE 
#VIDEOJUEGO --> WHILE 
# solicite un numero mayor a 3 
isValido= False
while not isValido: 
    edad= input("Ingrese su edad: ")
    if edad.isdigit(): 
        if int(edad)>30: 
            edad= int(edad)
            print("su numero es correcto")
            isValido=True
        else: 
            print("Su numero es menor que 30")
    else: 
        print("Ingrese un digito CORRECTO!")



#siempre en el while voy a poner la condicion que me saque ddel while 
opcion=""
while opcion!="5": 
    opcion=input("1)PRESENTAR\n2)Jugar\n5)Salir\nIngrese una opcion:")
    if opcion=="1": 
        print("Hola")
    elif opcion=="2": 
        print("Opcion 2")
    elif opcion=="5": 
        print("Saliendo del menu...") 
    else: 
        print("INGRESA UNA OPCION CORRECTA, POR FAVOR uwu")


nombres=[]
videojuegos=[]

maximo= max(videojuegos)
indice_max= videojuegos.index(maximo)
nombre_max= nombres[indice_max]