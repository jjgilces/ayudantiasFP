archivo_materias=open("colegio.txt")
print()
lineas_materias= archivo_materias.readlines()
print(lineas_materias)
materias_unicas=[]
for linea in lineas_materias:
    nombre,materias= linea.strip().split(",")
    materia,calificacion=materias.split("-")
    if materia not in materias_unicas:
        materias_unicas.append(materia)
print(materias_unicas)


for linea in lineas_materias:
    nombre,materias= linea.strip().split(",")
    materia,calificacion=materias.split("-")
    calificacion= int(calificacion)
    print(calificacion)