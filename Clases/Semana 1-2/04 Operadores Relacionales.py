#Programa 004-OperadoresRelacionales

print("*********************************")
print("* 004 - Operadores Relacionales *")
print("*********************************")

print(":::Precio de una botella con agua:::")

#En el aeropuerto nos dimos cuenta que los precios de  los productos que venden ahí dentro son un poco diferentes.  
#Dentro del aeropuerto, una botella con agua cuesta 0.99 centavos
#Fuera del aeropuerto, una botella con agua cuesta 0.75 centavos

#¿La botella con agua es más cara dentro del aeropuerto que fuera del aeropuerto? Si

#Utiliza el operador relacional correspondiente con botellaAguaFA y botellaAguaDA para almacenar el resultado en la variable botellaAguaCara.
botellaAguaFA= 0.99
botellaAguaDA=0.75
botellaAguaCara= botellaAguaDA> botellaAguaFA
print(botellaAguaCara)



#Muestra el resultado (True o False) por pantalla el resultado de la comparación.
print('¿La botella con agua es más cara dentro del aeropuerto que fuera del aeropuerto? ', botellaAguaCara)

print(":::Precio de artesanía:::")
#Fuera del aeropuerto, una artesanía cuesta 0.80 centavos. Asigna el valor a una variable.
artesaniaFA= 0.80
#Dentro del aeropuerto, una artesanía cuesta 0.75 centavos. Asigna el valor a una variable.
artesaniaDA= 0.75

#¿La artesanía cuesta menos o igual dentro del aeropuerto que fuera del aeropuerto?
#Utiliza el operador relacional correspondiente con las variables previamente asignadas
artesaniaMaCara= artesaniaDA <= artesaniaFA
#Muestra el resultado (True o False) por pantalla el resultado de la comparación.
print('¿La artesanía cuesta menos o igual dentro del aeropuerto que fuera del aeropuerto?', artesaniaMaCara)



