paises=["EC","CH","EC","PE","VN","BR","VN"]

#creo una lista vacia 

paises_sin_repetir=[]
#recorro la repetida
for pais in paises: 
    if pais not in paises_sin_repetir:
        paises_sin_repetir.append(pais)

#solo agrego los elementos que no se encuentren en la lista
for pais in paises: 
    if pais  in paises_sin_repetir:
        paises_sin_repetir.remove(pais)
    paises_sin_repetir.append(pais)
