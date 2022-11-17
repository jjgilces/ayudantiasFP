frutas =    ["aguacate","cerezas","ciruelas","fresas","kiwi","limon","mandarina","manzana","melon"] 
energias =  [134,58,45,34,53,39,39,41,37] 
agua =      [79,82,84,88,83,87,86,85,88] 
hidratos =  [1.3,13.5,11.0,7.0,12.1,9.0,9.0,10.5,8.4] 
fibras =    [2.4,1.5,2.1,2.2,1.5,1.0,1.9,2.3,0.8] 
grasas =    [13.8,0.5,0.15,0.5,0.44,0.3,0.19,0.2,0.28] 
proteinas = [1.3,0.8,0.6,0.7,1.0,0.7,0.8,0.3,0.9]  
#Seleccionar algunas frutas, tal que la suma del total de hidratos de las frutas seleccionadas sea menor que 30. El criterio de selección es empezando a tomar las frutas que tengan menor número de grasa. 
#Presentar los nombres de las frutas seleccionadas con sus valores de hidratos.
consumos=[]

for i in range(len(energias)):
    fruta= frutas[i]
    energia= energias[i]
    grasa= grasas[i]
    #consumo = energeia *grasa
    consumo = energia*grasa
    consumos.append(consumo)
print(consumos)













# grasasOrdenadas= grasas.copy()
# grasasOrdenadas.sort()
# sumaHidratos=[]
# sumaFrutas=[]
# contadorHidratos=0 #15
# for i in grasasOrdenadas:
#     indiceGrase = grasas.index(i) #2
#     hidrato = hidratos[indiceGrase]   
#     if(contadorHidratos+hidrato<30):
#         contadorHidratos=contadorHidratos+ hidrato
#         fruta = frutas[indiceGrase]
#         print(fruta, hidrato)



