#par o impar
numero = 4
isPar = numero  % 2 ==0  #un numero es par
isImpar = numero % 2 !=0 #un numero es impart

#promedio en listas
#sum -len

#recorrer 2 listas paralelas
nombres=[]
cantidad=[]
for i in range(len(cantidad)):
    #0
    nombre = nombres[i]
    cantidad1 = cantidad[i]
numeros=[10,12,13]
print(numeros[2])
#elementos unicos en una lista
paises=["Ecuador", "Peru","Colombia", "Peru", "Argentina","Colombia"]
paisesSinR=[]
for i in paises:
    if i not in paisesSinR:
        paisesSinR.append(i)
# print(paisesSinR)

#recorrer cuando se cuantas veces debo recorrer

    # print(i)
    #0,1,2
#recorrer cuando no se cuantas
#pida numeros hasta que el numero sea 4

num = int(input("Ingrese un numero: ")) 
#1 #5 #6
#4
# 3 3 3 8 6 5 4
while(num!=4):
    num= int(input("vuelva a ingresar un numero: ")) 
print(num)
facultades = ["fcnm","fiec","fimcp","fcv","fadcom","fcsh","fimcm"]
estudiantes = [600,1200,900,50,100,1250,80]
pagina = input("Ingrese una pagina web: ") #www.espol.edu.ec www.fiec.espol.edu.ec  
partes =pagina.split(".") #[www", "fiec" , "edu"]
condicion1= partes[0] == "www"
condicion2= pagina.endswith(".espol.edu.ec")
condicion3 = partes[1] in facultades
condicion4= len(partes) == 5
condicionT= condicion1 and condicion2 and condicion3 and condicion4
print( "Es una pagina valida", condicionT)

maximo = max(estudiantes)
indiceMax = estudiantes.index(maximo) #5
facultadMax = facultades[indiceMax]

promedio = sum(estudiantes)/len(estudiantes)



import Funciones as f
promedio(f.listaC)