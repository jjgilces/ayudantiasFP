menu = "1.Familia\n2. Ranas por familia\n3. Taxonomia\n4. Resultados\n5 Salir"
print(menu)
opcion= input("Ingrese una opción: ")
# 1. Familias. Muestra las familias de ranas que hay en el Ecuador.
# 2. Ranas por familia. Muestra las ranas por cada una de las familias.
# 3. Taxonomia 1. Muestra la taxonomía por las familias.
# 4. Resultados. Muestra las proporciones de cada una de las familias de ranas en el país.

#f:10  f:20   f:20  f:0

#total =50 
#la prop... f = 10/50 *100 =20%
def abrirArchivo(nombreArchivo):
    archivo = open(nombreArchivo,encoding= "utf-8") #utf perrmite tildes y ñ
    lista= [] 
    for linea in archivo: 
        datos= linea.strip().split(",")
        lista.append(datos)
    return lista


def familia(nombreArchivo):
    archivo = open(nombreArchivo)
    lista= [] 
    for linea in archivo: 
        familia= linea.split(",")[-2]   
        #nombre,clase,orden,familia,genero=linea.split(",")
        lista.append(familia)
    familias=set(lista)
    archivo.close()
    return familias

def ranaPorFamilia(nombreArchivo): 
    familias= familia(nombreArchivo)
    datos=abrirArchivo(nombreArchivo)
    dicTaxonomia={}
    for dato in datos: 
        rana= dato[0]
        family=dato[-2]
        dicTaxonomia.setdefault(family,[])  #{familia1:[]}
        dicTaxonomia[family].append(rana)
        #
    return dicTaxonomia


def ranaPorFamilia(nombreArchivo): 
    familias= familia(nombreArchivo)
    datos=abrirArchivo(nombreArchivo)
    dicTaxonomia={}
    for f in familias: 
        ranas=[]
        for dato in datos: 
            rana= dato[0]
            family=dato[-2]
            if f ==family:
                ranas.append(rana)
        dicTaxonomia[f]=ranas
    return dicTaxonomia

def taxonomia(nombreArchivo): 
    familias= familia(nombreArchivo)
    datos=abrirArchivo(nombreArchivo)
    dicTaxonomia={}
    for dato in datos: 
        taxo= dato[-1]
        family=dato[-2]
        dicTaxonomia.setdefault(family,set())  #{familia1:{}}
        dicTaxonomia[family].add(taxo)
        #
    return dicTaxonomia


def proporciones(): 
    familas_ranas= ranaPorFamilia(("ranas_ecuador.csv"))  #{fa1:[r1,r2]}
    total=0
    for f in familas_ranas.values(): 
        t=len(f)
        total+=t

    # familia 1      12%
    for familia, ranas in familas_ranas.items(): 
        cantRanas=len(ranas)
        porcentaje =cantRanas/total *100 
        print("La familia {} tiene una proporción de {:.2f}%".format(familia,porcentaje))


while opcion!="5":
    if opcion=="1": 
       familia("ranas_ecuador.csv")
    elif opcion =="2":
        ranaPorFamilia("ranas_ecuador.csv")
# print(ranaPorFamilia(("ranas_ecuador.csv")))
proporciones()
