
correo = input("Ingrese correo ESPOL: ") #reyjcast@espol.edu.ec
condicion1 = correo[0].isalpha() 
usuario = correo.find("@")==1 
condicion3 = correo.isalnum()
condicion2 = correo.endswith("espol.edu.ec")
CondicionFinal = condicion1 and condicion3 and usuario and condicion2
print("¿ Es valido el correo ESPOL? ", CondicionFinal)
print(usuario)
correo = input("Ingrese correo ESPOL: ")
condicion1 = correo[0].isalpha() 
condicion2 = correo.isalnum()
condicion3 = correo.count("@")==1
condicion4 = correo.endswith("espol.edu.ec")
CondicionFinal = condicion1 and condicion2 and condicion3 and condicion4 
if CondicionFinal:
    print("Es un correo de ESPOL valido")
else: 
    print("No es un correo valido")

