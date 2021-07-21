import Funciones as f
suma= f.sumar(10,5)
print(suma)

lista1=[10,10,10]
lista2=[5,10,7]
f.promedio(lista2)
f.promedio(lista1)
nombres=["One Piece","Death Note","Pokemon", "Dragon Ball", "Inuyasha","Tokyo Ghoul","Naruto"]
calificaciones=[4,9,11,9,10,7,5]
#10,9,9,8,7,5,4
tipos=["Shonen","Gore","Shonen", "Aventura","Shonen", "Shonen","Aventura" ]
#Shonen, Gore, Aventura 
comunidades=["Gamers","otakus","Gamers","otakus","Gamers","otakus","PK"]

f.animeMayorCalificacion(nombres,calificaciones)
print(f.tiposUnicos(tipos))
