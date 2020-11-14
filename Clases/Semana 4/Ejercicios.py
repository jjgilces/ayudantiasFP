#¿Que imprime los siguientes codigos?

letras= ["a", "c", "z","m","k"]
numeros=[3,4,5,6,5,7]
t=''
print("a"*0)
for c in letras:  #"a"  "c"   "z"
    a= letras.index(c) #  0   1   2   3   4
    b= numeros[:a]
    d= c*len(b) # "c"*1 
    t= t + d  # ""+ 
# print(t) 


#1  c="a" a=0  b=[]    t = ""
#2 c="c" a=1  b=[3]   t = "c"
#3 c="z "  a=2  b=[3,4] t= "c" +zz
#4 c="m"                    c zzmmm
#5 c="k" a=4 b=[3,4,5,6]   czzmmmkkkk esta es la salida



lista=[89,45,23,17,55,95,13,41,28,11]
lista.sort()
#[11,13,17,23,28,41,45,55,89]

promedio = sum(lista)//len(lista) # DIVISION ENTERA 
#32.2 ---> 32
menores=[]
i=0
while lista[i]<promedio:  #FALSO
    menores.append(lista[i])
    i+=1

# print(menores)

#1     11     menores=[11]
#2     13     menores=[11,13]
#3            menores=[11,13,17]
#             menores=[11,13,17,23]
#             menores=[11,13,17,23,28]
#    41     menores=[11,13,17,23,28] solucion


pal= 'Se va en sus naves'
b = pal[::-1].replace(' ','').lower()   #'sevansusnaves'
pali= pal.lower().replace(' ','')     #sevaensusnaves
# if pali==b:
#     print('es palindromo')
# else:
#     print('no es palindromo')

# Escriba un programa en Python que pida por consola un número entero positivo, a partir del cual se
# mostrarán por pantalla los múltiplos de dicho número hasta el 100

# Solicite dos números.  El primer número entre 1 y 10 y el segundo entre 10 y 20. Genere una lista con los números en el rango ingresado.  Asuma que el usuario va a ingresar un número en el rango indicado.  Presente la lista



nombres = ["Camilo","Alberto","Miguel","Karla","Sonia","Margarita","Carlos"]
instrumentos = ["bateria","piano","guitarra","guitarra","trompeta","piano","bajo"]

# Dada las listas de nombres e instrumentos de los integrantes de una banda realice lo siguiente:
# Solicitar un nombre y mostrar el instrumento que toca
# Mostrar cuántos integrantes tocan el mismo instrumento

# Nota: Las listas son paralelas.  Asuma que el usuario va a ingresar un nombre que se encuentra en la lista





# Solicitar el ingreso de un numero entero y determinar si es par o no.
# En caso de que sea par imprimir "Es par", caso contrario, "Es impar". 



#EXAMEN   
#       pintar coser lavar
#        0     1     2
#        9    7   8 

#      7     8   9 
#   coser lavar pintar
tareas=['pintar', 'coser','lavar']
inicio=[2, 5,6]
duracion=[7,2,2]
finalizacion=[]

for i in range(len(inicio)):
    final = inicio[i]+duracion[i]
    finalizacion.append(final)

finalOrdenada= finalizacion.copy()
finalOrdenada.sort()
#COMO ORDENAR LISTAS
tareaOrdenas=[]

maximo = 14
horasTrabajadas= 0
i=0
while(horasTrabajadas<maximo):
    horasTrabajadas = horasTrabajadas+ finalOrdenada[i]
    print("{}. {} #{} horas".format(i+1, tareaOrdenas[i], finalOrdenada[i]))
    i+=1
print(horasTrabajadas)




# finalizacion.sort()
