#del archivo google.py sed importan las funciones consultaPal y consultaOracion
from google1 import consultaPal,consultaOracion
#se imprime la bievenida al usuario
print("BIENVENIDO A GOOGLE TRANSLATE")
#se imprime al usuario la explicación del programa
print("El idioma de traducción por defecto es de eng-spa. Sin embargo,\nsi ud desea spa-eng debe enviar origen y destino.")
#se imprime al usuario la explicación del programa
print("Para validar su funcionamiento le brindamos los siguientes ejemplos:")
#se imprime el primer ejemplo que es la traducción de la palabra dog con la función consultaPal
print("dog:", consultaPal("dog"))
#se imprime el segundo ejemplo que es la traducción de la palabra sky con la función consultaPal
print("sky:",consultaPal("sky"))
#se imprime el tercer ejemplo que es la traducción de la palabra hombre con la función consultaPal, esta vez pasándole argumentos ya que ya no es eng-spa sino spa-eng
print("hombre:",consultaPal("hombre","spanish", "english"))
#se imprime el cuarto ejemplo que es la traducción de la palabra casa con la función consultaPal, esta vez pasándole argumentos ya que ya no es eng-spa sino spa-eng
print("casa:",consultaPal("casa","español", "english"))
#se imprime al usuario la explicación de que también se traducen oraciones, no sólo palabras, aunque la traducción no es perfecta (ya que retorna palabras aleotorias que pueden ser posible traducción pero no la exacta, así lo programamos con la primera función consultaPal)
print("\nTambién oraciones (no es una traducción perfecta)")
#se imprime el primer ejemplo de la traducción de una oracion con la función consultaOracion pasándole como argumentos, el string de la oracion, el idioma de origen y el de destino
print("Yo tengo 32: ",consultaOracion("Yo tengo 32", "spanish", "english").capitalize())
#se imprime el segundo ejemplo de la traducción de una oracion con la función consultaOracion pasándole como argumentos, el string de la oracion, el idioma de origen y el de destino
print("You are my sun:",consultaOracion("You are my sun", "english", "spanish").capitalize())
#se explica que en caso de existir la palabra en el diccionario, no se la traduce sino que se la muestra tal cual (así se configuró con la primera función, el else imaginario)
print("\nEn caso de no existir la palabra, no la traduce")

#se le pregunta al usuario si quiere traducir alguna palabra
opcion = input("Deseas traducir alguna palabra? Y/N").lower()
#si puso que sí (de cualquiera de las maneras expresadas en la lista ["y", "yes", "si", "sí"]), entonces...
if opcion.lower() in ["y", "yes", "si", "sí"]:
    #... entonces se le pide que ingrese cada palabra separada por coma
    #se eliminan los espacios vacíos con replace
    #se separan las palabras por sus comas con split
    palabras = input("Ingrese cada palabra separada por coma: ").replace(" ","").split(",")
    #se pide al usuario que ingrese el idioma de origen
    origen = input("Ingrese idioma origen:")
    #se pide al usuario que ingrese el idioma de destino
    destino = input("Ingrese idioma destino:")
    #se imprime de qué idioma a qué idioma se traducirá
    print(f"Traducciones {origen}:{destino}")
    #por cada palabra de la lista de palabras...
    for palabra in palabras:
      #... se imprimirá la palabra, dos puntos, su traducción usando la primera función
        print(palabra+":",consultaPal(palabra,origen, destino))
#se le pregunta al usuario si quiere traducir alguna oración
opcion = input("Deseas traducir alguna oración? Y/N").lower()
#si puso que sí (de cualquiera de las maneras expresadas en la lista ["y", "yes", "si", "sí"]), entonces...
if opcion.lower() in ["y", "yes", "si", "sí"]:
    #se pide que ingrese la oracion a traducir
    oracion = input("Ingrese la oración: ")
    #se pide que ingrese el idioma de origen
    origen = input("Ingrese idioma origen:")
    #se pide que ingrese el idioma de destino
    destino = input("Ingrese idioma destino:")
    #se imprime de qué idioma a cuál se traducirá
    print(f"Traducciones {origen}:{destino}")
    #se imprime la oración, dos puntos, la oración traducida usando la segunda función
    print(oracion+":",consultaOracion(oracion,origen, destino))
#si no indica querer una traducción de oración, entonces se le agradece
else:
    print("Gracias por usar Google Translate (pirata).")