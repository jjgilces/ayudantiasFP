#sume 2 numeros 
def sumar(a,b):
    return a+b

#Retornan
#Muestran 

#Cree una funcion que reciba una lista de numeros y muestre el promedio

def promedio(lista):
    print(sum(lista)/len(lista))

#FUNCIONES ANIME 
def animeMayorCalificacion( nombres, calificaciones ) :
    mayorCalificacion=max(calificaciones)#10 
    indiceMayor=calificaciones.index(mayorCalificacion)#4
    nombreMayor=nombres[indiceMayor]
    print(nombreMayor)


def listaSinRepetir(tipos):
    tiposUnicos=[]
    for tipo in tipos: 
        if tipo not in tiposUnicos: 
            tiposUnicos.append(tipo)
            #[]--> [shonen ]
    return tiposUnicos


def string_a_diccionario(texto): #"Hola como estas hola querida estas estas estas"
    texto=texto.lower()
    palabras=texto.split()   #["hola","como","como","querida",querida]
    palabrasSinRepetir=listaSinRepetir(palabras)
    diccionario={}
    for palabra in palabrasSinRepetir:
        veces= palabras.count(palabra)
        diccionario[palabra]=veces

    return diccionario


print(string_a_diccionario("Hola como estas hola querida estas estas estas"))

lista=[["nom","juan"],["celular","09304"],["nom","jose"],["nom","pedro"]]
#{nom:[juan,jose], celular:[0873]}

def lista_a_diccionario(lista): 
    diccionario={}
    for elemento in lista:
        clave,valor=elemento
        valor=[valor]
        diccionario[clave]=diccionario.get(clave,[])+valor
        #[]+[juan]-->[juan]
        #[juan]+[jose]-->[juan,jose]
        #[juan,jose]+[pedro]-->[juan,jose, pedro ]
    return diccionario
print(lista_a_diccionario(lista))
#JOhan
#jOHAN 
#andrea
#andrea
#jose 


#johan,andrea, jose 