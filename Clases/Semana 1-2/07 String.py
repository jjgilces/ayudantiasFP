# Escriba un programa que pida ingresar una contraseña para su sitio web.

password = input("Ingrese su contraseña: ")  # hola   Hola como estas

# El programa deberá presentar y realizar las siguientes operaciones:
# Para validacines futuras, el programador necesita conocer el numero total de caracteres

numCaracteres = len(password) #numero de caracteristico >8 
print("El numero de caracteres es", numCaracteres)


# En caso de que se olvide su contraseña el usuario podrá visualizar el primer caracter y el ultimo caracter de su contraseña

#Espol1990
#HOLAMUNDO12903477 
#01234567

firstC= password[0]
lastC= password[-1]
# ultimo -->-1 

#E  0


print(firstC, lastC)


# La base de datos almacenará la cadena al revez, cree una variable que almacene esta nueva variable
#Johan  nahoJ 
passwordAlReves= password[::-1]  
#[inicio: final-1:-1]


print(passwordAlReves)
# El sistema no permite ingresar cadenas que contengan la letra "a". Cambie La cadena con cada letra “a” remplazada por una “e” o alguna otra letra

passwordOK= password.replace("a","e")

#holamimama
#amamimaloh
#ememimeloh
#holemimeme

print(passwordOK)
# Debido a una cuestion de seguroidad debe proteger su contraseña de la interfaz de usuario.    Ej: Chao ---> * * * *
print("*"*numCaracteres)



#ENCONTRAR UN CARACTER 
posicionA= password.find("e")
print(posicionA)

