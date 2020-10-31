import random as rd
# 5 numeros aleatorios del 1 al 5, sumaT divisible al mayor
#al menor
lista=[]
num1 = rd.randint(1,5)
num2 = rd.randint(1,5)
num3 = rd.randint(1,5)

lista.append(num1)
lista.append(num2)
lista.append(num3)

sumaTotal = sum(lista) #suma total
mayor= max(lista)
menor= min(lista)
cond1= sumaTotal % mayor ==0
cond2 =  sumaTotal % menor ==0
conT= cond1 or cond2
print(lista)
print(conT)
