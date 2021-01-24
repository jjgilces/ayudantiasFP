def academico(narchivos):
    notas=dict()
    for archivo in narchivos:
        semestre=archivo[6:-4]
        archivo=open(archivo)
        for linea in archivo:
            matricula,materia,notaP,notaF,notaM,estado=linea.strip().split(",")
            d_semestres=notas.setdefault(matricula,dict())
            listaMaterias=d_semestres.setdefault(semestre,[])
            listaMaterias.append((materia,notaP,notaF,notaM,estado))
    return notas