molecula = ["A","C","G","T"] 
nombres = ["adenina","citosina","guanina","timina"]
numeroApariciones=[]
cadena= "ACGTSDFGHRTYSTSZXGSXQWERATZXC1T123454A3"
for i in molecula:
    veces = cadena.count(i)
    numeroApariciones.append(veces)
indiceMax= numeroApariciones.index(max(numeroApariciones))
moleculaMaxima = molecula[indiceMax]
nombreMaximo= nombres[indiceMax]

#presente los mayores al promedio o los menores 
# y presente su molecula y su nombre, el numero de veces que se repite
promedio= sum(numeroApariciones)/len(numeroApariciones)
print(promedio)
print(numeroApariciones)
for i in range(len(molecula)): #for por indice
    vecesPorMolecula= numeroApariciones[i]
    if vecesPorMolecula> promedio:
        mol= molecula[i]
        nom = nombres[i]
        print(vecesPorMolecula,mol,nom)
# print("La molecula que mas veces aparece es {} con su nombre {}".format(moleculaMaxima,nombreMaximo) )



