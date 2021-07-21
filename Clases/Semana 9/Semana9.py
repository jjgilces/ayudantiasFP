# Escriba la función cargarDatos(nomFile)que recibe el nombre de un archivo que en cada línea contiene los siguientes campos "ciudad,metrica,valorDeMetrica" (ver ejemplo). La función retorna un diccionario con la estructura descrita a continuación#
#{"precioCasas":0,"temperatura":0}
#{}
#{"Guayaquil":{"precioCasas":200, "temperatura":20}}

def cargarDatos(nomFile): 
    archivo = open(nomFile) #modo lectura
    diccionario={}
    for linea in archivo: 
        ciudad,tipo,valor = linea.split(",")
        diccionario.setdefault(ciudad,dict())
        diccionarioTipos= diccionario.get(ciudad)
        diccionarioTipos[tipo]=int(valor)
    archivo.close()
    return diccionario


datos=cargarDatos("Clases\Semana 9\datos.txt")

diccionarioPaises={"Ecuador":["Guayaquil","Cuenca"],"Colombia":["Bogota","Cali"]}
print(datos)
def metricaPais(datos, paises): 
    dicc={}
    for pais, ciudades in paises.items(): 
        dicc.setdefault(pais,dict())
        tempP=0
        precioP=0
        for ciudad in ciudades: 
            tempP+= datos.get(ciudad).get("temperatura",0)
            precioP+= datos.get(ciudad).get("precioCasas",0)
        tempP=tempP/len(ciudades)
        precioP=precioP/len(ciudades)
        dicc[pais]["temperatura"]=tempP
        dicc[pais]["precioCasas"]=precioP
    return dicc

promedios=metricaPais(datos,diccionarioPaises)

def  generaPaises(promedios,metrica,minimo,maximo): 
    archivo = open(metrica+".csv","w")
    for pais, metricas in promedios.items():
        valor = metricas.get(metrica)
        if minimo<=valor<=maximo:
            archivo.write("{},{},{}".format(pais,metrica,valor))
            archivo.write("\n")
            archivo.writelines()
    archivo.close()

generaPaises(promedios,"precioCasas",100,1000000000)
#{guayaquil:preciocasas:150, temperatura }