frutas =    ["aguacate","cerezas","ciruelas","fresas","kiwi","limon","mandarina","manzana","melon"] 
aguas =      [79,82,84,88,83,87,86,85,88] 
hidratos =  [1.3,13.5,11.0,7.0,12.1,9.0,9.0,10.5,8.4] 
grasas =    [13.8,0.5,0.15,0.5,0.44,0.3,0.19,0.2,0.28] 
energias =  [134,58,45,34,53,39,39,41,37] 
fibras =    [2.4,1.5,2.1,2.2,1.5,1.0,1.9,2.3,0.8] 
proteinas = [1.3,0.8,0.6,0.7,1.0,0.7,0.8,0.3,0.9]  
valoresNutricional=[]
#El valor nutricional de una fruta se calcula energía + fibras + proteínas. 
#Seleccionar algunas frutas, tal que la suma del total de agua sea menor que 200. El criterio de selección es empezando a tomar las frutas que tengan mayor valor nutricional. 
#Presentar los nombres de las frutas seleccionadas con sus valores de agua.
for i in range(len(hidratos)):
    energia = energias[i]
    fibra = fibras[i]
    proteina = proteinas[i]
    valorNu= energia+fibra+proteina
    valoresNutricional.append(valorNu)
print(valoresNutricional)
valoresNuOrdenados = valoresNutricional.copy()
valoresNuOrdenados.sort(reverse=True)
print(valoresNuOrdenados)
sumaAgua=0
aguasSumadas=[]
for i in valoresNuOrdenados:
    indice = valoresNutricional.index(i)
    agua = aguas[indice]
    fruta= frutas[indice]
    sumaAgua+=agua
    if(sumaAgua<200):
        aguasSumadas.append(agua)
        print(fruta,agua)
print(sum(aguasSumadas))

