canciones=["YHLQMDLG","YOPERREOSOLA","DILES", "BYEMEFUI","DAKITI","SOYPEOR","BICHIYAL", "COMOANTES","0SENTIMIENTO"] 
votaciones=[0]*len(canciones)
print(votaciones)
#Social Media le ha solicitado a usted validar mensajes de twitter que representa votos para una determinada canción.  El programa debe permitir al usuario ingresar 3 votos, en caso de que el usuario ingrese un voto invalido el programa debe solicitar nuevamente su voto, tantas veces sea necesario hasta que complete sus 3votos válidos.





#Un mensaje valido es aquel que tenga el
# 1) tiene hashtag #badbunny 
# 2) continuación del hashtag está el nombre de la canción debe pertenecer a las canciones.
#3) 3 votos 
#4) en caso de que el usuario ingrese un voto invalido el programa debe solicitar nuevamente su voto

#HOLA COMO ESTAS 
#HOALD
#HOLS
#HOLA #bADBUNNY CANCION HOLA 

votosDisponible = 0
while votosDisponible!=3:
    tweet = input("Ingrese un mensaje de twitter:").lower() #MI VVOTO #BADBUNNY CANCION H
    if "#badbunny" in tweet:
        listaDelTweet=tweet.split("#badbunny") 
        parteDondeCancion =listaDelTweet[1]
        partesLaCancion =parteDondeCancion.split('')
        cancion=partesLaCancion[0].upper()
        if cancion in canciones:
            print("Su voto por la cancion {} es valido".format(cancion))
            votosDisponible+=1 
        else:
            print("Su voto no es valido")

    else:
        print("Su voto no es valido")
#EL PROGRAMA DEBE ACABARSE CUANDO LOS VOTOS SEAN IGUALES A 3
print("EL PROGRAMA SE ACABA")



        







def crear():
    dicc= {}
    salir= ""
    while salir!="fin": 
        nombre= input("ingrese su nombre...")
        materia=""
        #agrego al pana al diccionario 
        dicc.setdefault(nombre, {})
        while materia!="salir":
            materia=input(" ingrese materia y nota")
            #agregas la materia al diccionario
            dicc[nombre]=materia
       