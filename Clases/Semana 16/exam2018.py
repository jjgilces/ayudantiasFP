
import numpy as np
from numpy.lib.function_base import append
def cuadrantes(matriz):
    f,c=matriz.shape
    M1=matriz[:f//2,:c//2]
    M2= matriz[:f//2,c//2:]
    M3=matriz[f//2: ,:f//2]
    M4=matriz[f//2: ,f//2:]
    return M1,M2,M3,M4
def poblacionEspecie(mAnimales,especie):
    matrices=cuadrantes(mAnimales)
    lista=[]
    for m in matrices:
        mismaEspecia= m==especie
        lista.append(np.sum(mismaEspecia))
    return tuple(lista)
dicEspecies={0:"No hay animal",1:"Lobo ártico",2:"Oso Polar", 3:"Reno",
4:"Foca", 5:"Pinguino",
6:"NARVAL", 7:"ZORRO ÁRTICO",
8:"Ballena", 9:"Morsa",
10:"Beluga"}










def crearMatriz(nomArchivo):
    archivo=open(nomArchivo)
    nfilas=archivo.readline()
    ncolumnas= archivo.readline()
    nfilas= int(nfilas)
    ncolumnas= int(ncolumnas)
    archivo.readline()
    hielo2009= np.zeros((nfilas,ncolumnas))
    hielo2019= np.zeros((nfilas,ncolumnas))
    especies2009= np.zeros((nfilas,ncolumnas))
    especies2019= np.zeros((nfilas,ncolumnas))
    for linea in archivo:
        year,fila,columna,hielo,especie=linea.strip().split(",")
        columna=int(columna)
        fila=int(fila)
        hielo=int(hielo)
        especie=int(especie)
        if year=="2009": 
            hielo2009[fila,columna]=hielo
            especies2009[fila,columna]=especie
        else: 
            hielo2019[fila,columna]=hielo
            especies2019[fila,columna]=especie
    return hielo2009,hielo2019,especies2009,especies2019 #retorna una tupla 
hielo2009,hielo2019,especies2009,especies2019= crearMatriz("artico2009-2019.txt")


def densidadHielo(mHielo): 
    matrices= cuadrantes(mHielo) #(H1,H2,H3,H4)
    lista_densidades=[]
    for matrizH in matrices: 
        suma= np.sum(matrizH)
        total_celdas= matrizH.size
        densidad=suma/total_celdas
        lista_densidades.append(densidad)
    return tuple(lista_densidades)

def especieDominante(nAnimales):
    matrices= cuadrantes(nAnimales) #(H1,H2,H3,H4)
    lista_dominantes=[]

    for matrizH in matrices:
        especies_unicas,veces=np.unique(matrizH)
        #return_counts=True
        veces=[]
        for especie in especies_unicas:
            condicion= matrizH==especie
            veces_especie= np.sum(condicion)#los que cumple solucion
            veces.append(veces_especie)
        veces= np.array(veces)
        indice_mayor= np.argmax(veces)#1   2
        especie_mayor=especies_unicas[indice_mayor]
        lista_dominantes.append(especie_mayor)
    return tuple(lista_dominantes)

def migracionEspecie(mAnimales2009,mAnimales2019,especie):
    matrices2009= cuadrantes(mAnimales2009)
    nombres_cuadrante= ["Q1","Q2","Q3","Q4"]
    total_2009=[]
    for Q2009 in matrices2009: 
        existe_animal= Q2009==especie
        total_cuadrante_2009= np.sum(existe_animal)
        total_2009.append(total_cuadrante_2009)
    mayor2009= nombres_cuadrante[np.argmax(np.array(total_2009))] #Q1

    matrices2019= cuadrantes(mAnimales2019)
    total_2019=[]
    for Q2019 in matrices2019: 
        existe_animal= Q2019==especie
        total_cuadrante_2019= np.sum(existe_animal)
        total_2019.append(total_cuadrante_2019)
    mayor2019= nombres_cuadrante[np.argmax(np.array(total_2019))] #Q1
    return mayor2009,mayor2019


def crearDiccionario(mHielo, mAnimales,dicEspecies):
    dicc={}
    d1,d2,d3,d4= densidadHielo(mHielo)
    dicc["densidad hielo"]={"Q1":d1,"Q2":d2,"Q3":d3,"Q4":d4}
    dic_contar_especies= {} 
    for especie in dicEspecies.keys(): #0 1 2 3 
        #{0:12}
        condicion= mAnimales==especie
        veces= np.sum(condicion)
        dic_contar_especies[especie]=veces
    dicc["Especies"]=dic_contar_especies
    return dicc
    