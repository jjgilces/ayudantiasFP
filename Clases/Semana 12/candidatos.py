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

                
#Cree una funcion que cuente los votos POR CANDIDATO en TOTAL(hombres y mujeres)
def contarVotos(jrv_h,jrv_M):
    votosHombres=np.sum(jrv_h,axis=0)
    votosMujeres=np.sum(jrv_M,axis=0)
    total=votosHombres+votosMujeres
    return total

#Funcion que retorna true si hay segunda vuelta
#Hay segunda vuelta si el primer candidato tiene mas de 40%
#y si ademas supera por el segundo candidato con mas votos  10%  

def segundaVuelta(jrv_h,jrv_m):
    total=contarVotos(jrv_h,jrv_m)
    totalO= np.sort(total)
    primerCandidato= totalO[-1]#50
    segundoCandidato=totalO[-2]
    condicion=(primerCandidato/total)*100<40
    condicon2= (segundoCandidato/total)*100+10 >=((primerCandidato/total)*100)
    return condicion and condicon2

#FUNCION QUE RETORNA EL PORCENTAJE DE MUJERES, HOMBRES Y TOTAL QUE OBTUVO
#UN CANDIDATO 

def estadistica(JRV_H, JRV_M, candidatos, nombreCandidato):
    #find e index       find-->-1   index se care el 
    posicion= candidatos.index(nombreCandidato)
    votosHombres=np.sum(JRV_H,axis=0)
    votosMujeres=np.sum(JRV_M,axis=0)
    total=votosHombres+votosMujeres
    votosHC= votosHombres[posicion]
    votosMC= votosMujeres[posicion]
    votosTC=total[posicion]
    ph= (votosHC/sum(votosHombres))*100
    pm= (votosMC/sum(votosMujeres))*100
    pt= (votosTC/sum(total))*100
    return ph,pm,pt

#FUNCION QUE CREA UN ARCHIVO DE TEXTO CON LA INFO ANTERIOR POR CADA CANDIDATO
def crearArchivo(jrvH, jrvM, candidatos):
    for candidato in candidatos: 
        archivo=open("Clases\Semana 12\\"+candidato+".txt","w")
        ph,pm,pt= estadistica(jrv_h,jrv_m,candidatos,candidato)
        archivo.write("Candiado: "+candidato+"\n")
        archivo.write("PORCENTAJE HOMBRES: "+str(ph)+"\n")
        archivo.write("PORCENTAJE MUJERES: "+str(pm)+"\n")
        archivo.write("PORCENTAJE TOTAL: "+str(pt)+"\n")
        archivo.close()

crearArchivo(jrv_h,jrv_m,candidatos)


#DADAS LAS FUNCIONES CREAR UN PROGRAMA QUE RECIBA UNA LISTA DE CANDIDATOS
# Y LAS MATRICES Y CREE UN ARCHIVO CON LOS PORCENTAJES DE LO CANDIDATOS 


