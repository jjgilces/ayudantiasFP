menu = "1.Familia\n2. Ranas por familia\n3. Taxonomia\n4. Resultados\n5 Salir"
print(menu)
opcion= input("Ingrese una opción: ")

def familia(nombreArchivo):
    archivo = open(nombreArchivo)
    lista= [] 
    for linea in archivo: 
        nombre,clase,orden,familia,genero=linea.split(",")
        lista.append(familia)
    familias= list(set(lista))
    return familias
print(familia("Clases\Semana 11\ranas_ecuador.csv"))