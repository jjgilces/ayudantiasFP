info=["201908076-5","202020304-7","201567475-3","201907076-6"]
matriculas=[]
materias=[]

#el usario ingresa una oracion, cuenta las palabras
oracion=input("ingrese: ") #hola como estas 
palabras=oracion.split("")




print(matriculas)
for informacion in info: 
    # matri_can= informacion.split("-")#
    matricula,materia= informacion.split("-") #[394, 3]
    matriculas.append(matricula)
    materias.append(materia)
    # matriculas.append(matri_can[0])
    # materias.append(matri_can[1])
print(matriculas)
print(materias)








opcion=""
# while opcion!="N":
# ingreso= input("Ingrese un numero de matricula: ")#404044
# while ingreso not in matriculas:
#     print("Matricula invalida ")
#     ingreso= input("Ingrese un numero de matricula: ")#f,4,5,krf
# indice= matriculas.index(ingreso)#[20293,2094,20494]  [1,2,3] -->2
# numero_materias=materias[indice]  #2
# print("Cantidad de materias:",numero_materias)
# opcion=input("Desea continuar:")
while opcion!="N": 
    ingreso= input("Ingrese un numero de matricula: ")#404044
    while ingreso not in matriculas:
        print("Matricula invalida ")
        ingreso= input("Ingrese un numero de matricula: ")#f,4,5,krf
    indice= matriculas.index(ingreso)#[20293,2094,20494]  [1,2,3] -->2
    numero_materias=materias[indice]  #2
    print("Cantidad de materias:",numero_materias)
    opcion=input("Desea continuar:")
    