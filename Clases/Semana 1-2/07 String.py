# Escriba un programa que pida ingresar una contraseña para su sitio web.

password = input("Ingrese su contraseña: ")  # hola   Hola como estas

# El programa deberá presentar y realizar las siguientes operaciones:
# Para validacines futuras, el programador necesita conocer el numero total de caracteres
numCaracteres = len(password)
print("El numero de caracteres es", numCaracteres)


# En caso de que se olvide su contraseña el usuario podrá visualizar el primer caracter y el ultimo caracter de su contraseña
firstC = password[0]
lastC = password[-1]
num= numCaracteres-2
print(firstC, lastC)
passwordVisible = firstC+("*"*num)+lastC
print(passwordVisible)

# La base de datos almacenará la cadena al revez, cree una variable que almacene esta nueva variable
passwordAlReves= password[::-1]
print(passwordAlReves)
# El sistema no permite ingresar cadenas que contengan la letra "a". Cambie La cadena con cada letra “a” remplazada por una “e” o alguna otra letra
passwordOK= password.replace("a","e")
print(passwordOK)
# Debido a una cuestion de seguroidad debe proteger su contraseña de la interfaz de usuario.    Ej: Chao ---> * * * *
print("*"*numCaracteres)

