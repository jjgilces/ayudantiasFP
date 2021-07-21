def ingresoCanciones():
    cancion1= input("Ingrese una letra de una canción: ").split()
    cancion2= input("Ingrese una letra de una canción: ").split()
    cancion3= input("Ingrese una letra de una canción: ").split()
    while len(cancion1)<=20 or len(cancion2)<=20 or len(cancion3)<=20:
        cancion1= input("Ingrese una letra de una canción: ").split()
        cancion2= input("Ingrese una letra de una canción: ").split()
        cancion3= input("Ingrese una letra de una canción: ").split()
    cancion1= tuple(cancion1)
    cancion2= tuple(cancion2)
    cancion3= tuple(cancion3)
    return cancion1,cancion2,cancion3

def comunes(t1,t2,t3):
    return t1 & t2 &t3

def cuenta(palabras):
    palabrasUnicas=tuple(set(palabras))
    veces=[]
    
    diccionario={}
    for pala in palabrasUnicas: 
        for p in pala: 
            if p=="a" or p == "e" or p=="i" or p == "o": 
                diccionario.setdefault(p,0)
    return diccionario

can1,can2,can3=ingresoCanciones()
comun= comunes(can1,can2,can3)
diccionario=cuenta(comun)