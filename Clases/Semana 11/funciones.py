print("\n\n\n\n")
def cargarDatos(nombFile):
    file=open(nombFile)
    dicc=dict()
    for linea in file:
        ciudad,metrica,valor=linea.strip().split(",")
        if ciudad not in dicc:
            dicc[ciudad]={}
            if metrica =="precioCasas":
                dicc[ciudad][metrica]=int(valor)
            elif metrica=="temperatura":
                dicc[ciudad][metrica]=int(valor)
        else:
            if metrica =="precioCasas":
                dicc[ciudad][metrica]=int(valor)
            elif metrica=="temperatura":
                dicc[ciudad][metrica]=int(valor)

    file.close()
    return dicc
def cargarDatos(nomFile):
    dic ={}
    f = open(nomFile)
    for i in f:
        i = i.strip("\n")
        partes = i.split(",")
        dic[partes[0]] = dic.get(partes[0],{})
        dic[partes[0]][partes[1]]= dic[partes[0]].get(partes[1],partes[2])
    f.close()
    return dic
diccionario = cargarDatos("Clases\Semana 11\datos.txt")
print(diccionario)

def cargarDatos(nomFile):
    fichero=open(nomFile)
    diccionario=dict()
    for linea in fichero:
        ciudad,metrica,valor=linea.strip().split(",")
        metricas =diccionario.setdefault(ciudad,dict())
        metricas[metrica]=float(valor)
        metricas =diccionario.setdefault(ciudad,dict())
        metricas[metrica]=float(valor)
    fichero.close()
    return diccionario
diccionario =cargarDatos("Clases\Semana 11\datos.txt")
print(diccionario)



def metricaPais(datos, paises):
    dic = {}
    for pais, ciudades in paises.items():
        for ciudad in ciudades:
            if ciudad in datos:
                dic2 = {"precioCasas": [], "temperatura": []}
                dic[pais] = dic.get(pais,dic2)
                dic[pais]["precioCasas"].append(int(datos[ciudad].get("precioCasas")))
                dic[pais]["temperatura"].append(int(datos[ciudad].get("temperatura")))
        dic[pais]["precioCasas"] = sum(dic[pais]["precioCasas"])/len(dic[pais]["precioCasas"])
        dic[pais]["temperatura"] = sum(dic[pais]["temperatura"])/len(dic[pais]["temperatura"])
    return dic

def generaPaises(promedios,metrica,minimo,maximo):
    f = open("{}.csv".format(metrica), "w")
    for i in promedios:
        if minimo<=promedios[i][metrica] and promedios[i][metrica]<=maximo:
            f.write("{},{},{}".format(i,metrica,promedios[i][metrica]))
            f.write("\n")
    f.close()





