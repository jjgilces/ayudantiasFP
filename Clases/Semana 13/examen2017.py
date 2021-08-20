import numpy as np 

#1989 
def juegosConsolas(nomArchivo, categoria, decada):
    archivo = open(nomArchivo)
    archivo.readline()
    juegosDecadas=[]
    consolasDecada=[]
    for linea in archivo: 
        nombre, anio, consola,calificacion, tags= linea.strip().split(",")
        #"RPG;SJ;LIZNK;ELDA;KSFJ"
        categoriaJuego=tags.split(";")[0]
        decadaJuego= anio[2:]
        if decadaJuego==decada:
            juegosDecadas.append(nombre)
        if decadaJuego==decada and categoriaJuego==categoria:
                consolasDecada.append(consola)
        
    juegosDecadas=list(set(juegosDecadas))
    consolasDecada=list(set(consolasDecada))
    return juegosDecadas,consolasDecada

def crearMatriz(nomArchivo,  categoria,decada):

    archivo = open(nomArchivo)
    MATRIZ= np.zeros((len(juegosDecadas),len(consolasDecada)))
    for linea in archivo: 
        nombre, anio, consola,calificacion, tags= linea.strip().split(",")
        #"RPG;SJ;LIZNK;ELDA;KSFJ"
        categoriaJuego=tags.split(";")[0]
        decadaJuego= anio[2:]
        if decadaJuego==decada and categoriaJuego==categoria:
            posicionFila= juegosDecadas.index(nombre)
            posicionColumna= consolasDecada.index(consola)
            MATRIZ[posicionFila,posicionColumna]=calificacion
    