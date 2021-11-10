tupla1=tuple()
#No se puede modificar una tupla (aumentar su tamaño, no se pueden eliminar)


#tupla---> lista, PERO no tengo que modificar NO VOY PODER 
informacion=("092848466","04/07/2021")
#EXPLICITAMENTE --> retorne una tupla, 
planetas= ("Tierra","Marte")
mesesDelAnip=("Enero","Marzo")
numeroCedula= informacion[0]  #--> 09389446










print(tupla1)
tupla2=()
print(tupla2)
numeros=1,2,3
print(numeros)
dias_semana=("Lunes","Martes","Miercoles","Jueves","Viernes")
fines_semana=("Sabado", "Domingo")
print(dias_semana*3)
print(type( dias_semana + fines_semana))
# print(dias_semana)
print( "Sabado" in dias_semana)

#La mayoria de ejercicios piden, retornar, imprimer, usar tuplas
califaciones=[0,9,8,7.5]
nombres=["Johan","Alan","Fausto","Domenica"]
califaciones=tuple(califaciones)
#(10,9,8,7.5)
print(califaciones)
#Imprima el nombre del estudiante que obtuvo la MAYOR calificacion <----tatuarse
#obtengo cual fue la calificacion mayor
maximo=max(califaciones)  #10
indice_maximo= califaciones.index(maximo)
nombre_maximo= nombres[indice_maximo]

print(nombre_maximo)
