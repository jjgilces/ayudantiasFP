from io import open_code
import numpy as np

candidatos=("Almeida","Andrade","Arauz","Carrasco","Celi","Freile","Gutierrez","Hervas","Larrea","Lasso","Montufar","Pena","Perez","Romero","Sagnay","Velasco")
jrv_h=np.array([[15,145,1000,45,85,23,4,67,22,110,45,23,56,12,14,45],
                [18,187,2000,45,85,23,4,67,22,110,45,23,56,12,14,67],
                [109,12,3000,45,85,23,4,67,22,110,45,23,56,12,14,18],
                [18,187,89,45,85,23,4,67,22,110,45,23,56,12,14,67],
                [231,76,67,45,85,23,4,67,22,110,45,23,56,12,14,137]])

jrv_m=np.array([[100,240,1000,45,85,23,4,67,22,110,45,23,56,12,14,45],
                [50,38,242,45,85,23,4,67,22,110,45,23,56,12,14,67],
                [178,12,164,45,85,23,4,67,22,110,45,23,56,12,14,5],
                [18,187,89,45,85,23,4,67,22,110,45,23,56,12,14,67],
                [123,23,638,45,85,23,4,67,22,110,45,23,56,12,14,333]])

def contarVotos(jrv_h,jrv_M):
    hombres= np.sum(jrv_h, axis=0)
    mujeres = np.sum(jrv_M,axis=0)
    total=tuple(hombres+mujeres)
    return total

def segundaVuelta(jrv_h,jrv_m):
    votosTotales= np.array(contarVotos(jrv_h,jrv_m))
    print(votosTotales)
    total= np.sum(votosTotales)
    primerCandito= np.max(votosTotales)
    votosTotales[np.argmax(votosTotales)]=0
    segundoCandidato= np.max(votosTotales)
    condicion1= ((primerCandito/total)*100 ) >= 40
    condicion2= (((primerCandito/total)*100 )-10) >= ((segundoCandidato/total)*100 )
    return condicion1 and condicion2

def estadistica(JRV_H, JRV_M, candidatos, nombreCandidato):
    #find e index       find-->-1   index se care el 
    indice = candidatos.index( nombreCandidato )
    totalH= np.sum(JRV_H)
    totalM= np.sum(JRV_M)
    totalPorCandidatoHombres= np.sum(JRV_H, axis=0)[indice]
    totalPorCandidatoMujeres= np.sum(JRV_M, axis=0)[indice]
    totalT= totalH+totalM
    porH= (totalPorCandidatoHombres/totalH)*100
    porM= (totalPorCandidatoMujeres/totalM)*100
    totalCandidato= contarVotos(JRV_H,JRV_M)[indice]
    porT= (totalCandidato/totalT )*100
    return (porH,porM,porT)


def crearArchivo(jrvH, jrvM, candidatos):
    archivo= open("Candidatos.txt","w")
    archivo.write("Elecciones Presidenciales\n")
    for candidato in candidatos:
        tuplaE=estadistica(jrvH,jrvM,candidatos,candidato)
        porH,porM,porT= tuplaE
        archivo.write("Candidato: "+candidato+"\n")
        archivo.write("voto totales: "+str(porT)+"\n")
        archivo.write("voto mujeres: "+str(porM)+"\n")
        archivo.write("voto hombres: "+str(porH)+"\n")
        archivo.write("\n")
        archivo.write("\n")
    archivo.close()

crearArchivo(jrv_h,jrv_m,candidatos)


#DADAS LAS FUNCIONES CREAR UN PROGRAMA QUE RECIBA UNA LISTA DE CANDIDATOS
# Y LAS MATRICES Y CREE UN ARCHIVO CON LOS PORCENTAJES DE LO CANDIDATOS 


