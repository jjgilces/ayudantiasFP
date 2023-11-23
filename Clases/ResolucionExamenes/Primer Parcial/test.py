def multiplicador (numero, lista):
    numero+= 2
    for pos in range (len (lista)):
        lista [pos] *= numero
lista = [1,2,3,4,5]
numero=2
multiplicador(numero, lista)
print(numero, lista, sep="\n")