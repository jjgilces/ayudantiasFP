#se crea un diccionario con las palabras y sus traducciones
#las claves con las palabras en inglés y los valores son listas con palabras en español que son traducción de las claves
palabrasIng={
  "the":["el","la","los","las"],
  "a": ["un","una"],
  "i":["yo"],
  "she":["ella"],
  "he": ["el"],
  "you":["tu","ustedes"],
  "your":["su","tu"],
  "it":["eso","su"],
  "we":["nosotros"],
  "they":["ellos"],
  "dog":["perro","perra"],
  "cat":["gato","gata"],
  "car": ["carro","auto","coche"],
  "boy":["chico"],
  "girl":["chica"],
  "men":["hombres"],
  "man":["hombre"],
  "women":["mujeres"],
  "woman":["mujer"],
  "school":["escuela","colegio"],
  "house":["casa","vivienda"],
  "sun":["sol"],
  "moon":["luna"],
  "my":["mi"],
  "am":["soy","estoy","tengo"],
  "are":["eres","son","estás","están"],
  "is":["es","esta"],
  "in":["en"],
  "like":["gusta"],
  "air":["aire"],
  "water":["agua"],
  "fire":["fuego"],
  "sky":["cielo"],
  "star":["estrella"],
  "hi":["hola","que tal"]
  }

#se importa la librería random con el nombre de rd para que sea más rápido llamar la librería
import random as rd

#se define la función llamada consultaPal que tiene como parámetros:
#pal: un string que es la palabra a traducir
#origen: que es el idioma de origen y tiene como argumento default "english"
#destino: que es el idioma de destino y  tiene como argumento default "spanish"
#diccionario: es el diccionario del cual se obtendran las palabras para traducir y tiene com valor default el nombre del diccionario palabrasIng
def consultaPal(pal, origen="english", destino="spanish", diccionario=palabrasIng):
    #traduccion es pal, la palabra a traducir
    traduccion = pal
    #por cada pareja palEng,listaEsp (que es la palabra en inglés y la lista de palabras en español que correspondan), se recorre el diccionario:
    for palEng, listaEsp in diccionario.items():
        #si origen y destino sí son de los idiomas para los cuales funciona el diccionario, entonces:
        if origen in ["inglés", "english"] and destino in ["español", "spanish"]:
            #si la clave del diccionario es igual a la palabra que vamos a traducir, entonces...
            if palEng == pal.lower():
              #...entonces la traducción será una palabra aleatoria en español de la lista que corresponde
                traduccion = rd.choice(listaEsp)
        #si origen y destino NO son de los idiomas para los cuales funciona el diccionario, entonces:
        elif destino in ["inglés", "english"] and origen in ["español", "spanish"]:
          #si la palabra a traducir está en la lista de palabras en español, entonces...
            if pal.lower() in listaEsp:
              #la traducción será la palabra en inglés
                traduccion = palEng
            #existe el "else" imaginario en el que entonces la traduccion será igual a la misma palabra
    #se retorna una string con la traduccion de la palabra
    return traduccion

#se define la función llamada consultaOracion que tiene como parámetros:
#oracion: un string que es la oracion a traducir
#origen: que es el idioma de origen
#destino: que es el idioma de destino
def consultaOracion(oracion, origen, destino):
    #se crea un string vacío donde se agregará palabra por palabra traducida (con la función creada anteriormente)
    traduccion = ""
    #se separa la oracion en palabras
    palabras = oracion.split()
    #por cada palabra en la lista palabras:
    #(se recorre la lista palabras)
    for palabra in palabras:
        #se va concatenando al string traducción, palabra por palabra con la función creada anteriormente
        traduccion+= consultaPal(palabra, origen, destino)+" "
    #se retorna una string con la traduccion de la oración
    return traduccion