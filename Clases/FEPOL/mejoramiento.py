import numpy as np 

def crearMatriz(nombreArchivo): 
    archivo = open(nombreArchivo)
    codigos= archivo.readline().strip().split(",") #obtener la primera linea --> una lista de los codigos 
    #"100034,100312,100021,201245,432198"
    vector_codigos= np.array(codigos)
    archivo.readline()# para eliminar la cabecera
    M = np.zeros((len(codigos),12))
    meses =["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC""]
    for linea in archivo: 
        codigo, fecha, cant = linea.strip().split(",")
        fila = codigos.index(codigo) # el indice del codigo en la lista de codigos
        dato = fecha.split("-") # lista de la fecha
        mes=dato[1] # el mes --"ENE"
        columna= meses.index(mes) 
        #02-ENE-2018  -> ["02","ENE","2018"]
        M[fila,columna]+= int(cant)
    return vector_codigos,M  
#ojo
def mesMasRentable(M):
    totalMes = np.sum(M,axis=0) #vertical --[ 10, 12,11]
    meses =["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
    cantidadMax= totalMes.max() #el maximo --> 12
    indiceMax= totalMes.argmax() #el indice del maximo --> 1
    mesMaximo = meses[indiceMax] # el mes --> "FEB"
    return mesMaximo, cantidadMax #retorna una tupla

def altosBajos(M,k): 
    mes,maximo= mesMasRentable(M)# maximo del año
    meses =["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
    vector_meses= np.array(meses)
    totalMes = np.sum(M,axis=0) #vertical --[ 10, 12,11]
    indicador= maximo-k # al menos deberia llegar
    condicion = totalMes>=indicador
    cumplen= vetor_meses[condicion]
    return cumplen

#ojo
def mejoresNProductos(M,cod,n):
    totalProducto = np.sum(M,axis=1) #horizontal 
    indicesOrdenados = totalProducto.argsort()  #indices ordenados
    codigoOrdenadosAsc= cod[indicesOrdenados] #codigos ordenados ascendentemente
    codigosOrdenaDesc= codigoOrdenadosAsc[::-1] #codigos ordenados descendentemente
    #me piden los n mejores
    return codigosOrdenaDesc[:n]

def porCategoria(M,cod,categorias): 
    codigos=list(cod)
    for categoria, lstCod in categorias.items():
        archivo = open(categoria+".txt","w")#crea el archivo w
        archivo.write("codigo,ENE,FEB,MAR,ABR,MAY,JUN,JUL,AGO,SEP,OCT,NOV,DIC\n")#escribe la cabecera
        for codigo in lstCod: 
            indice = codigos.index(codigo)
            fila = M[indice]#vector
            archivo.write(codigo+","+",".join(fila.astype(str))+"\n")
        archivo.close()