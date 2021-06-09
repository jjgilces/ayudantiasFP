#par o impar
numero = 4
isPar = numero  % 2 ==0  #un numero es par
isImpar = numero % 2 !=0 #un numero es impart

#promedio en listas
calificaciones=[10,12,15,15]
promedio= sum(calificaciones)/len(calificaciones)

#recorrer 2 listas paralelas
nombres=["Juan","Jose","Pablo","Noelia"]
semestres=[1029,2019,1020,139]


print(promedio)
#solo los mayores al promedio
# 0  1  2  3 
#for por indice 
for i in range(len(nombres)):
    califacion= calificaciones[i]
    if califacion>=promedio:
        print(nombres[i])
#for elemento
# juan  jose pablo noelia 
for nombre in nombres:
    
    nombreAlReves= nombre[::-1]
    print(nombreAlReves)


paises=["Ecuador","Peru","Brasil","Ecuador","Peru","Brasil","Brasil"]
paisesUnicos=[]
for pais in paises:
    if pais not in paisesUnicos:
        paisesUnicos.append(pais)

print(paisesUnicos)


