


 # RIO2016  BSC  ECU
 #GYE BRA BSC
 # YOSOYESPOL GYE BSC
 #RIO2016:1 BC:2

listaFechas=['08-22-2016', '08-25-2016', '08-27-2016']



diccionario={"A":2,"B":3,"C":5}
print(diccionario["A"]) 
diccionario["A"]=6
print(diccionario)  
diccionario["D"]=7
print(diccionario)
#{"A":6,"B":3,"C":5, "D":7}
# print(diccionario["E"]) #ERROR 

#ANTES

#GET 
numero = diccionario.get("A") #2
numero2 = diccionario.get("D",0)
print(numero2)

#SET
diccionarioVacio={}
diccionarioVacio.setdefault("A",0)
diccionarioVacio["A"]=0
print(diccionarioVacio)

print()
print()
print()
print()
print()
print()
tendencias = {
    '08-22-2016': {'#Rio2016', '#BSC', '#ECU'},
    '08-25-2016': {'#GYE', '#BRA','#BSC'}, 
    '08-27-2016': {'#YoSoyEspol', '#GYE', '#BSC'}
    }


tendencias['08-22-2016']
# def cuentaEtiquetas(tendencias, listaFechas):
#     diccionario={}
#     for fecha in listaFechas:
#         etiquetas= tendencias[fecha] #{#Rio, #Bsc,#ecu}
#         for tag in etiquetas:
#             if tag not in diccionario:
#                 diccionario[tag]=1
#             else:
#                 diccionario[tag]+=1
#     return diccionario

def cuentaEtiquetas(tendencias, listaFechas):
    diccionario={}
    for fecha in listaFechas:
        etiquetas= tendencias[fecha] #{#Rio, #Bsc,#ecu}
        for tag in etiquetas:
           diccionario.setdefault(tag,0) #{BSC:0} "" 
           diccionario[tag]+=1
    return diccionario

def reporteTendencias(tendencias, listaFechas):
    diccionarioVeces= cuentaEtiquetas(tendencias,listaFechas)
    todas= len(listaFechas)
    print("literal A")
    for etiqueta,nVces in diccionarioVeces.items():
        if nVces==todas:
            print(etiqueta)
    print("literal B") 
    print(list(diccionarioVeces.keys()))     
print(cuentaEtiquetas(tendencias, listaFechas))
reporteTendencias(tendencias,listaFechas)



#cree uuna funcion que retorne las etiquetas en un fecha indicada
def etiqueta(tendencias,fecha):
    return tendencias[fecha]#{#BSC, #CSE, #DTP}


def tendenciasE(tendencias,fecha1,fecha2):
    conjunto1= tendencias[fecha1] #{#BSC, #CSE, #DTP}
    print("conjunto 1",conjunto1)
    conjunto2= tendencias[fecha2]
    print("conjunto 2",conjunto2)
    conjuntoF= conjunto1.symmetric_difference(conjunto2)
    return conjuntoF

print(tendenciasE(tendencias,'08-22-2016', '08-25-2016'))



