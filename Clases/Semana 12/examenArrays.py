import numpy as np 
import random as rd  
nombreArchivo="Clases/Semana 12/vacunacion.txt"
def cargarArchivo(nombreA,m):
    archivo = open(nombreA)
    #eliminar la cabecera
    archivo.readline()
    archivo.readline()
    lineaVacunas= archivo.readline().strip()
    lista= lineaVacunas.split(":") #separador
    stringVacuna= lista[1]#solo las vacunas
    listaVacunas= stringVacuna.split(",") #convierto en lista
    vectorVacunas= np.array(listaVacunas)
    lineaC= archivo.readline().strip()
    lista= lineaC.split(":") #separador
    stringC= lista[1]#solo las CIUDADES
    listaC= stringC.split(",") #convierto en lista
    vectorCiudades= np.array(listaC)
    #eliminar cabeceras de poblacion
    archivo.readline()
    archivo.readline()
    archivo.readline()

    lineaPoblaciones= archivo.readline().strip()
    poblaciones= lineaPoblaciones.split(",")
    totalPoblacion=[]
    for pobla in poblaciones:
        poblacion= pobla.split(":")[1]
        poblacion = int(poblacion)
        totalPoblacion.append(poblacion)

    vectorPoblacion = np.array(totalPoblacion)

    M= np.zeros((vectorCiudades.size,vectorVacunas.size))
    #eliminar cabeceras de VACUNACIONA
    archivo.readline()
    archivo.readline()
    archivo.readline()

    for linea in archivo: 
        lista= linea.strip().split(";")
        ciudad= lista[0]
        mes= int(lista[1].split("-")[1])
        strVacunas= lista[2]
        lstVacunas= strVacunas.split("|")
        if mes==m:
            for vacuna in lstVacunas:
                nombre, cantidad= vacuna.split(",")
                indiceF= listaC.index(ciudad)
                indiceC= listaVacunas.index(nombre)
                M[indiceF,indiceC]+= int(cantidad)
    return vectorCiudades, vectorVacunas,vectorPoblacion, M



# print(M)

def totalVacunados(nombreArchivo, mesInicio, mesFin):# mesInicio= 4 , mesFin= 6
    vVacunas, vCiudades,vPoblacion, T= cargarArchivo(nombreArchivo, mesInicio)
    for mes in  range(mesInicio+1,mesFin+1):
        vCiudades, vVacunas,vPoblacion, M=cargarArchivo(nombreArchivo, mes)
        T+=M
    return T
totalVacunados(nombreArchivo, 4, 6)


def masVacunados(nombreArchivo, mes,N):
    vCiudades, vVacunas,vPoblacion, M=cargarArchivo(nombreArchivo, mes)
    tops=[]
    for i in range(vVacunas.size):
        print(i)
        subMatriz= M[:,i]
        matrizOrdenada= np.argsort(subMatriz)[::-1]
        ciudadesOrdenadas= vCiudades[matrizOrdenada]
        topCiudades= ciudadesOrdenadas[:N]
        tops.append(topCiudades)
    return tuple(tops)
vCiudades, vVacunas,vPoblacion, M=cargarArchivo("Clases/Semana 12/vacunacion.txt", 5)
masVacunados(nombreArchivo, 5, 3)
vacun_ener_agosto=totalVacunados(nombreArchivo, 1, 8)
print(vacun_ener_agosto)
totalVacunadosV=np.sum(vacun_ener_agosto, axis=1)
porcentaje= totalVacunadosV/vPoblacion
print(porcentaje)
vbool=porcentaje>=25
cumpleC=vCiudades[vbool]
print(cumpleC)

total_mayo_junio=totalVacunados(nombreArchivo, 4, 6)
i_ciu_cumple=[]
v,c,p,abril= cargarArchivo(nombreArchivo, 4)
v,c,p,agosto= cargarArchivo(nombreArchivo, 6)

for ciudad in cumpleC:
    # i_ciu_cumple.append(vCiudades.index(ciudad))
    indiceC= list(vCiudades).index(ciudad)
    print(indiceC)
    totalA= abril[indiceC,:].sum()
    totalAg= agosto[indiceC,:].sum()
    print(totalA-totalAg)





