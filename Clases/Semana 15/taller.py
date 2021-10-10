# Cree una matriz cuyas filas sean los alumnos del colegio y cuyas columnas sean las materias, los valores son las notas que han obtenido.

import numpy as np
from numpy.core.numeric import indices 
archivo_estudiantes= open("alumnos.txt") #leer archivos y escribir ---> agregar datos a un archivo
lista_alumnos=[]
for linea in archivo_estudiantes:
    n,nombre= linea.strip().split("-")
    lista_alumnos.append(nombre)
numero_filas= len(lista_alumnos)



lista_materias=["Matematicas","Lenguaje","Estudios Sociales","Ingles","Quimica","Fisica","Computacion"]
archivo_materias=open("colegio.txt")

MATRIZ= np.zeros((numero_filas,len(lista_materias)))
for linea in archivo_materias:
    nombre,materias= linea.strip().split(",")
    materia,calificacion=materias.split("-")
    calificacion= int(calificacion)
    pos_fila= lista_alumnos.index(nombre)
    pos_columna= lista_materias.index(materia)
    MATRIZ[pos_fila,pos_columna]=calificacion

print(MATRIZ)

#ojo: crear matriz valores aletorios
total_materias=np.sum(MATRIZ,axis=0) #arreglo
total_estudiantes= len(lista_alumnos) #Int
promedio_materia= total_materias/total_estudiantes

dic_materias={}
for i in range(len(promedio_materia)):
    materia=lista_materias[i] #Mate  ingles
    promedio= promedio_materia[i]#56   68.7
    dic_materias.setdefault(materia,promedio)
    # dic_materias[materia]=promedio
print(dic_materias)

def generarArchivo(materia):
    nombre ="reprobados"+materia+".txt"
    archivo= open(nombre,"w")
    indice= lista_materias.index(materia)
    submatriz_materia= MATRIZ[:,indice]
    for i in range(len(lista_alumnos)):
        nombre= lista_alumnos[i]
        nota= submatriz_materia[i]
        if nota<60:
            linea= "{},{},{}\n".format(materia,nombre,nota)
            archivo.write(linea)

#fail   usar argsort los indices
promedio_alumno=np.sum(MATRIZ,axis=1)
indices_mayores= np.argsort(promedio_alumno)[::-1]
array_alumnos= np.array(lista_alumnos)
nombres_top= array_alumnos[indices_mayores][:]
# print(nombres_top)


#MAIN

for materia, promedio in dic_materias.items():
    print("Materia: {}  Promedio General:{}".format(materia,promedio))
    generarArchivo(materia)
    print("Se genero el archivo")
