#La FEF le ha solicitado a usted validar mensajes de twitter que representa votos para un determinado goleador. Un mensaje valido es aquel que tenga el hashtag #goleador y a continuación del hashtag está el apellido del goleador. El programa debe permitir al usuario ingresar dos votos, en caso de que el usuario ingrese un voto invalido el programa debe solicitar nuevamente su voto, tantas veces sea necesario hasta que complete sus dos votos válidos. Ejemplo: 
votosValidos=2
while votosValidos>0:
    mensaje = input("Ingrese un mensaje de twitter: ")
    hastag = mensaje.split("#")
    voto = hastag[1]  #"goleador Ordoñez es el mejor"
    palabras = voto.split() # ["goleador", "ordoñez", "es","el"]
    goleador= palabras[0]
    futbolista = palabras[1]
    if goleador.lower() == "goleador":
        print("Su voto por el jugador {} es valido".format(futbolista))       
        votosValidos -= 1
    else:
        print("Su voto no fue valido")
       
    # else:
    #     print("Ingrese un mensaje que tenga hastag")
# cifuentes, jose, jose
# 1,1 ,1
# cifuente, jose
# 1         1
# 1          2
print(jugadores)
print(votosJugador)


    


