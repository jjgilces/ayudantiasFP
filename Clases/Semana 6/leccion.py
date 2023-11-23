#EJERCICIO1 
# lea un archivo y cuente las palabras repetidas

archivo= open('Semana 6/palabras.txt')
dicc={}
for linea in archivo:
    lista= linea.strip().split(" ")
    for palabra in lista:
        # if palabra not in dicc: otra manera de hacerlo 
        #     dicc[palabra]=1
        # else:
        #     dicc[palabra]+=1
        dicc.setdefault(palabra,0)
        dicc[palabra]+=1
palabras= list(dicc.keys())
veces= list(dicc.values())
palabrasC= palabras.copy()
print(palabras)
print(veces)
palabrasC.sort()
print(palabras)
#EJERCICIO 2
archivo2= open('Semana 6/repetidos.csv','w')
for palabra in palabrasC:
    indice= palabras.index(palabra) #busca la posicion en la original
    vez= veces[indice] #Obtiene el # de repeticiones
    archivo2.write(palabra)
    archivo2.write(" ")
    archivo2.write(str(vez))
    archivo2.write("\n")#salto de linea
archivo2.close()


#ejercicio 3 
dicEst={'0912877940':['jjuan','perez','201908086','FIEC']}
cedula='0912877940'
print(dicEst.get(cedula,'dato no existe'))
dicMat={'M001':'fundamentos de programacion'}
codigo='M001'
print(dicMat.get(codigo,'dato no existe'))

dicTipo= {"Leccion": 0.20, "Tarea":0.10}
dicNotas= {"0912877940:M001:Leccion": "10.0#7.8#6.9",
"0912877940:M001:Tarea": "9#7.8#8.9"}
promedioGeneral=0
for clave, valor in dicTipo.items(): 
    matricula= cedula+":"+codigo+":"+clave
    notas= dicNotas.get(matricula,"no hay nota")
    notas1= notas.split("#")
    total=0
    for n in notas1:
        n= float(n)
        total+=n
    promedio=total/len(notas1)
    ponderado= promedio*valor
    promedioGeneral+=ponderado
    print(promedio)
print(promedioGeneral)