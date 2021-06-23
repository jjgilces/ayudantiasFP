
import random as rd 
vidas=3
numR= rd.randint(2,6)
paloR= rd.choice(palos)
print(numR,paloR)
indicePalo= palos.index(paloR)
colorR= color[indicePalo]
usuario= input("Ingrese un numero:")  #10 CORAZON fjidj
numero, palo= usuario.split() #["3","Corazon "]
if numero>numR:
    print("El numero oculto es más bajo!")
elif numero<numR:
    print("El numero oculto es más alto! ")
if palo!=paloR:
    print("El color del palo es",colorR)
else:
    print("El palo de la carta es Correcto!")