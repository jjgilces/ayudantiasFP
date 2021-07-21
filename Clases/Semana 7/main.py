def comunes(lis1,lis2,lis3):
    compras1= set(lis1)
    compras2= set(lis2)
    compras3= set(lis3)
    return compras1 & compras2.intersection(compras3)


conjunto={4,2,3,6,5,10}
conjuntoVacio=set()
lista=[1,2,3,4,2,3,4]
conjuntoL= set(lista)
print(conjuntoL)
print(conjunto)

#LISTAS UNICAS 
elementoUnico= list(set(lista))
# print(elementoUnico)
print(conjunto.union(conjuntoL))
print(conjunto.intersection(conjuntoL))
print(conjunto & conjuntoL)



#Escribir una función que recibe la lista de todos los empleados de una empresa y la lista de solo
# los empleados que trabajaron el último viernes. Está función debe mostrar en pantalla los
# nombres de los empleados que no trabajaron el último viernes para multarlos. . Use operaciones
# de conjuntos.
# Pruebe la función, en el
def noTrabajaron(empleados,empleadosViernes):
    #{Johan, David}
    #[Andrea, Juan]
    todos= set(empleados)
    salvados= set(empleadosViernes)
    noSalvaron= todos-salvados
    print(noSalvaron)

datos="Ventas;Luis|Contabilidad;Pedro|Sistemas;Armando|Ventas;Juan|Marketing;Maria|Marketing;Luisa|Marketing;Rosa|Sistemas;Mariana|Contabilidad;Laura|Ventas;Melanie|Logística;Aura|Logística;Lady|Ventas;Alexa|Sistemas;Hugo|Recursos Humanos;Matías"


{'Ventas': ['Luis', 'Juan', 'Melanie', 'Alexa'], 'Contabilidad':['Pedro', 'Laura'], 'Sistemas': ['Armando', 'Mariana', 'Hugo'],'Marketing': ['Maria', 'Luisa', 'Rosa'], 'Logística': ['Aura','Lady'], 'Recursos Humanos': ['Matías']}
datosL=datos.split("|")
# Luis in dic
#Contabilidd in dic
dic={}
for dato in datosL:
    area,empleado=dato.split(";")

    
    if area not in dic:
        dic[area]=[empleado]  #{ventas:[empleado]}
    else:
        dic[area].append(empleado) #{ventas:[juan,jose]}

    #{}       []  +  [juan]
    actual= dic.get(area,[])+[empleado] #        [juan]+[jose]
    dic[area]= actual #{ventas: [juan,jose]}

    dic.setdefault(area,[])  #{ventas:[]}
    dic[area].append(empleado)

    
   
print(dic)