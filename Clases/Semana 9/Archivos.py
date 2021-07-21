# archivo = open("prueba.txt",)
#Modo lectura
# archivo = open("prueba.txt","r")

#si un archivo esta en modo lectura y no existe, va a dar error 


#Modo escritura
# archivo = open("prueba.txt","w")
#si un archivo esta en modo esscritura y no existe, lo crea


#Modo de agregar
archivo = open("Clases\Semana 9\prueba2.csv","r")
archivo.readline()
nombres=[]
edades=[]  #"18", "19"
for linea in archivo:
    #Linea--> Johan,Gonzalez,18 
    nombre,apellido,edad= linea.split()
    nombres.append(nombre)
    edades.append(int(edad))

#si un archivo esta en modo esscritura y no existe, lo crea