import numpy as np
jugadores= ["Rose","Banguera","La pulga","Ronaldo"]
goles=[10,30,20,5]
golesOrdenador= goles.copy()
golesOrdenador.sort()
for gol in golesOrdenador:
    indice= goles.index(gol)
    print(jugadores[indice])



#[5   10   20   30]
indicesGolces=goles.argsort() #vector de indices
#un vector con los indices en caso de que el vector esta ordenado
print(jugadores[indicesGolces])



#Indexar de menor a mayor un arreglo, segun otro
indices=goles.argsort() #vector de indices
ordenador= jugadores[indices]
def equiposUnicos(listaEquipos):
    equposArry=np.array(equipos)
    unicos=np.unique(equposArry)
    return unicos


estudiantes=np.array(["Juan","Alex","Victor","Maria"])
calificaciones=np.array([10,8,2,9])
#Muestre los nommbres segun quien obtuvo menor calificacion (menor a mayor  )
posiciones= calificaciones.argsort()
estudiantesOrdenador=estudiantes[posiciones]
print(estudiantesOrdenador)


#Mayor a menor 
mayorEst= estudiantesOrdenador[::-1]
print(mayorEst)

#presente el que obtuvo mayor calificacion
indice= calificaciones.argmax()  #MAXIMOS Y MINIMOS EN ARREGLOS CON DATOS 
masPilas= estudiantes[indice]
print(masPilas)
