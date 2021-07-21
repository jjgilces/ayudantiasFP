
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
diccionario["matriculas"]="2020"
print(calificacion)
print(diccionarioP)
print(diccionario)
print()



claves= diccionario.keys()
valores= diccionario.values()
items= diccionario.items()
print(claves)
print(valores)
print(items)
[('nombre', 'Johan'), ('edad', 21), ('hobbies', ['leer', 'deporte']), ('calificacion', 7), ('matricula', '2019'), ('matriculas', '2020')]
