junio=["Fb-10MB","Tw-5MB","Spotify-15MB","Tw-12MB","Spotify-1MB","FB-1234MB","ig-100mb"]
aplicaciones =[]
megabytes=[]
for i in junio:
    #FB-10MB
    listaAM=i.split("-")  
    #[fb, 10mb]
    aplicacion= listaAM[0].upper()
    aplicaciones.append(aplicacion)
    megas = listaAM[1] #10MB #100MB  #1000MB  
    megas = megas[:-2] #10 15 1998 str cadena plabrita
    megasEnteros= int(megas)
    megabytes.append(megasEnteros)
print(aplicaciones)
print(megabytes)

aplicacionesSinRepetir=[]
#CREAR LISTA SIN REPETIR 
for app in aplicaciones:
    if app.upper() not in aplicacionesSinRepetir:
        aplicacionesSinRepetir.append(app.upper())

for appSR in aplicacionesSinRepetir:
    numeroTotalDeMegasPorAPP=0
    for indice in range(len(aplicaciones)):
        app= aplicaciones[indice]
        mega= megabytes[indice]
        if app==appSR:
            numeroTotalDeMegasPorAPP+=mega
    print(appSR,numeroTotalDeMegasPorAPP)

#     print(aplicacion)

