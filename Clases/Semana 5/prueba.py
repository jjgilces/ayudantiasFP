lista=[1,2,3,7,4,5]

nombres=["a","b","c","d","e","f"]

print(lista)
max1= max(lista)
indiceM= lista.index(max1)
lista.sort()
max2=max(lista)
indiceM2= lista.index(max1)
print(indiceM)
print(lista)
print(indiceM2)
print(nombres[indiceM])


