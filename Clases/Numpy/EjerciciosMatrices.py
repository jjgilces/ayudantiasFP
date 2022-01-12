import numpy as np
costa =  ['Guayaquil', "Machala", 'Manta'] 
sierra = ['Pichincha','Quito', 'Latacunga', 'Cuenca', 'Loja']  
oriente = ['Macas', 'Nueva Loja', 'El Puyo']  
anios = [1998, 2003,  2017, 2019] 
todas= costa+sierra+oriente
MATRIZ= np.random.randint(100,500,(len(todas),8))
print(MATRIZ)

#Cantidad total de turistas que ingresaron a las ciudades del país en el año 2017. 
indice2017= anios.index(2017)
posicionColumna= indice2017 *2
sumaPorAnios= np.sum(MATRIZ,axis=0) #vector suma
totalTurista=sumaPorAnios[posicionColumna]


matriz2017= MATRIZ[:,posicionColumna]
totalTurista2= np.sum(matriz2017)

#La  capacidad  hotelera  promedio  para  cada  una  de  las  ciudades  de  la  sierra  considerando  todos  los  años.
matrizCH=MATRIZ[:,1::2]
print(matrizCH)
promedioCiudades= np.mean(matrizCH, axis=1)
print(promedioCiudades)

print(todas)
for ciudadS in sierra: 
    indiceC= todas.index(ciudadS)
    promedioC= promedioCiudades[indiceC]
    print("La ciudad {} tiene un promedio de {}".format(ciudadS,promedioC))

matrizSierra= MATRIZ[len(costa):len(costa)+len(sierra),:]
print(matrizSierra)
matrizSierraCH= matrizSierra[:,1::2]
print(matrizSierraCH)
promedioSierraCH= np.mean(matrizSierraCH,axis=1)
print(promedioSierraCH)
for i in range(len(sierra)):
    ciudadS= sierra[i]
    promedioS= promedioSierraCH[i]
    print("La ciudad {} tiene un promedio de {}".format(ciudadS,promedioS))



#Los años en la que la capacidad hotelera del país fue superior a 5000. 
capacidadPorPais= np.sum(matrizCH,axis=0)
print(capacidadPorPais)
condicion= capacidadPorPais>3000
print(condicion)
aniosCumplen= np.array(anios)[condicion]
print(aniosCumplen)


matrizTurista= MATRIZ[:,::2]
matrizTotalTurista= np.sum(matrizTurista,axis=1)
print(matrizTotalTurista)
indicesOrdenados= np.argsort(matrizTotalTurista)
vectorCiudades= np.array(todas)
print(vectorCiudades)
ciudadesOrdenadas= vectorCiudades[indicesOrdenados]#ordena de menor a mayor 
ciudadeOrdenadasDesc= ciudadesOrdenadas[::-1]
top3= ciudadeOrdenadasDesc[:3]
print(ciudadesOrdenadas)
print(top3)


indiceMachala= costa.index("Machala")
capacidadMachala=matrizCH[indiceMachala,:]
turistasMachala= matrizTurista[indiceMachala,:]
print(capacidadMachala,turistasMachala)
condicion=turistasMachala>capacidadMachala
print(condicion)











#TEMA 3
def crearMatriz(nomArchivo): 
    archivo= open(nomArchivo)
    filas=archivo.readline()
    columnas=archivo.readline()
    filas= int(filas)
    columnas= int(columnas)
    MHielo2019= np.zeros((filas,columnas))
    MHielo2009= np.zeros((filas,columnas))
    MEspecie2009= np.zeros((filas,columnas))
    MEspecie2019= np.zeros((filas,columnas))
    archivo.readline()
    for linea in archivo: 
        anio, fila, columna, hielo, especie= linea.strip().split(",")
        f= int(fila)
        c= int(columna)
        hielo= int(hielo)
        especie= int(especie)
        if anio =="2009": 
            MHielo2009[f,c]=hielo
            MEspecie2009[f,c]=especie
        else: 
            MHielo2019[f,c]=hielo
            MEspecie2019[f,c]=especie
    return MHielo2009,MHielo2019,MEspecie2009,MEspecie2019

matrices= crearMatriz('Clases/Numpy/WWF2020.txt')
print(matrices)