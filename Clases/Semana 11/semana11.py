tendencias = {
    '08-22-2016': {'#Rio2016', '#BSC', '#ECU'},
    '08-25-2016': {'#GYE', '#BRA','#BSC'}, 
    '08-27-2016': {'#YoSoyEspol', '#GYE', '#BSC'}, 
    '04-07-2020':{"#USA", "FIFA","COVID"}
    }

def cuentaEtiquetas (tendencias, listaFechas): 
    dicc={}
    #{#jaj:1,#bsc:4}
    #Creo una lista con todos los hastag y luego creo el diccionario contando cuentan
    #ir iterando el diccionario e ir creando, sumando las veces que se repitan
    for fecha in listaFechas: 
        etiquetas= tendencias.get(fecha,set()) #{'#Rio2016', '#BSC', '#ECU'}
        for tag in etiquetas: 
            # dicc.setdefault(tag,0)  
            # dicc[tag]+=1     
            if tag not in dicc: 
                dicc[tag]=1#{#BSC:1}
            else:
                dicc[tag]+=1 #BSC:2
    return dicc

def reportaTendencias(tendencias, listaFechas):
    numeroTendencias= cuentaEtiquetas(tendencias,listaFechas)
    numeroFechas=len(listaFechas)
    print("Literal A")
    for tag, veces in numeroTendencias.items(): 
        if veces==numeroFechas:
            print(tag)
    print("Literal B")
    print(list(numeroTendencias.keys()))
def tendenciasExcluyentes(tendencias, fecha1, fecha2): 
    etiquetas1= tendencias[fecha1] #{'#Rio2016', '#BSC', '#ECU'}
    etiquetas2= tendencias[fecha2] # {'#GYE', '#BRA','#BSC'}
    final= etiquetas1.symmetric_difference(etiquetas2)
    print(final)


reportaTendencias(tendencias, ['08-22-2016','08-25-2016','08-27-2016'])
tendenciasExcluyentes(tendencias,'08-22-2016','08-25-2016')