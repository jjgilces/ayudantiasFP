import random as rd

# randrange, choice , randint
#1 2 3 4 10 
numero= rd.randrange(11)  #nunca incluye al numero del final

numero2=rd.randint(5,15)
# print(numero)
# print(numero2)


lista=[18,19,20,34,12]
#escoja aleatorio de la lista
edad=rd.choice(lista)  #super tatuarse 



print(edad)
#Revolver una lista
rd.shuffle(lista)
print(lista)


