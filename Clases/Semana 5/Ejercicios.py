import random as rd
patos=[]
municion =10
for i in range(5):
    num = rd.randint(1,6)
    patos.append(num)
while(municion>0  and sum(patos)!=0):
    print("Patos:")
    print(patos)
    indice= input("Ingrese una posicion: ") #"string"
    while(not indice.isdigit()):
        indice= input("Ingrese un numero CORRECTO:") #nunca entra
    indice=int(indice)
    while(not (indice >= 0 and indice<len(patos))):
        indice= int(input("Ingrese un numero dentro del rango:"))#nunca entra   
    # patos[indice] = patos[indice]-1
    if(patos[indice]>0):
        patos[indice]-=1
    else:
        print("YA HAS ASESINADO A ESTE PATO")
    municion-=1
    print("Tiros restantes",municion)
    #el usuario NO debe ingresar una letra
    #el indice debe mayor o igual a cero y menor al len
if(sum(patos)>0):
    print("perdiste") 

