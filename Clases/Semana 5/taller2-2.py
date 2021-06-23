vidas=3
import random as rd 
palos=["CORAZON","DIAMANTE","TREBOL","PICAS"]
color=["ROJO","ROJO","NEGRO","NEGRO"]
numR= rd.randint(2,6)
paloR= rd.choice(palos)
indicePalo= palos.index(paloR)
colorR= color[indicePalo]
#2, PICAS
#3 intentos 
while vidas>0  :
    usuario= input("Ingrese un numero:")  #3 CORAZON 
    numero, palo= usuario.split() #["3","CORAZON"]
    numero = int(numero) #3
    if numero!=numR or paloR!=palo: #SI  falla el jugador tiene una oportunidad menos
        vidas-=1
    if numero==numR and paloR==palo:
        vidas=-1 # una condición para salir del while sin necesidad de break 
        print("Has adivinado ")
    if numero>numR:
        print("El numero oculto es más bajo!")
    elif numero<numR:
        print("El numero oculto es más alto! ")
    if palo!=paloR:
        print("El color del palo es",colorR)
    else:
        print("El palo de la carta es Correcto!") 
    if vidas==0:
        print("PERDIO SE ACABARON LOS INTENTOS! ")
        print("La carta que escogió la pc es:",numR,paloR)