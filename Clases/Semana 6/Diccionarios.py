
diccionario={"nombre":"Johan", "cedula":"0990520134","edad":19,"hobbies":["leer","deporte"]}
#cualquier tipo de dato 
#DESODERNADO 
lista=[[1,2,3],[2,4,6]]
print("Johan" in diccionario)
#clave, la varible que esta del lado izquierdo de los : 
#Valor
cedula= diccionario["cedula"]
diccionarioP={}
diccionarioP=dict()
diccionarioP["matricula"]="201908075"
diccionario["edad"]=21
diccionario.pop("cedula")
calificacion = diccionario.get("calificacion",0)



















diccionario.setdefault("matricula","2019")
diccionario["matricula"]="2020"
print(calificacion)
print(diccionarioP)
print(diccionario)
print()



#csv 
#1,Juan,Arroz 
#2,Pepe,Cebolla
#3,Juan,Tomate

#{juan: [arroz,tomate],pepe:[cebollla]}
dicc={}
archivo = open("Semana 6/compras.csv")
for linea in archivo:
    id,nombre,producto= linea.strip().split(",")
    # lista= linea.split(",")
    # id=lista[0]
    # nombre=lista[1]
    # compra=lista[2]
    # if nombre not in dicc:
    #     dicc[nombre]=[producto]
    # else: 
    #     dicc[nombre].append(producto)
    lista= dicc.setdefault(nombre,[])
    lista.append(producto)
print(dicc)


dicc.keys()
dicc.values()

for clave,valor in dicc.items():
    print(clave)
    print(valor)
    print()



