conductores=["Juan", "Pedro","Jose"]
listaC=["01-01-2020,Urdesa,kennedy, comida,7,1.2","02-01-2020,Guayacanes,kennedy, ropa,6,2.2","01-02-2020,Los Ceibos,Ceibos Norte, comida,7,1.2","01-03-2020,Urdesa,kennedy, comida,5,1.2"]

def cargar_datos(lista): 
    meses=["Enero","Febrero","Marzo","Abril","Mayo"]
    diccionario={}
    for info in lista: 
        informacion=info.split(",")
        fecha,origen,destino,articulo,km,peso=info.split(",")
        dia,mes,anio= fecha.split("-") #"04"
        mes=int(mes) #4
        posicionMes=mes-1
        nombreMes= meses[posicionMes]  #enero, febrero 
        diccionarioMes={"KmTotales":0,"LbsTotales":0,"Barrios":set()}
        barrios=set([origen,destino])
        diccionario.setdefault(nombreMes,diccionarioMes)  #{ENERO:{"KmTotales":0,"LbsTotales":0,"Barrios":set()}}
        #CONFIGURA, AGREGA O CREA SI NO EXISTE 
        diccionario[nombreMes]["KmTotales"]+=int(km)
        diccionario[nombreMes]["LbsTotales"]+=float(peso)
        diccionario[nombreMes]["Barrios"]= diccionario[nombreMes]["Barrios"].union(barrios)
        # if nombreMes not in diccionario: 
        #     barrios=set([origen,destino]) 
        #     diccionarioP={"KmTotales":int(km),"LbsTotales":float(peso),"Barrios":barrios}
        #     diccionario[nombreMes]=diccionarioP  #{enero:{"KmTotales":7,"LbsTotales":1.2,"Barrios":{urdesa, kennedy}}
        # else:   
        #     barrios=set([origen,destino]) 
        #     diccionario[nombreMes]["KmTotales"]+=int(km)
        #     diccionario[nombreMes]["LbsTotales"]+=float(peso)
        #     diccionario[nombreMes]["Barrios"]= diccionario[nombreMes]["Barrios"].union(barrios)



    return diccionario

      
print(cargar_datos(listaC))
diccionario={}
diccionario.add("a")
        

