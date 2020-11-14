prodL=["Carne","Leche","Huevos"]
costos=[2,5,1]
#[1,2,5]
encarecimiento=[-0.1,1,-2]
print("1)Consulta productos\n2)Encarecimiento\n3)Compra\n4)Salir")
opcion = input("Ingrese una opcion: ")
while(not opcion.isdigit()):
    opcion= input("Ingrese una opcion del menú valida")
opcion= int(opcion)

while(opcion!=4):
    if opcion==1:
        valor= float(input("Ingrese un valor:"))
        for i in range(len(prodL)):
            if costos[i]>= valor:
                print(prodL[i],costos[i])
    elif opcion==2:
        enca= input("Igrese el encarecimiento:").lower()
        if enca=="positivo":
            for i in encarecimiento:
                if i>0:
                    print(i)
        elif enca=="negativo":
            for i in encarecimiento:
                if i<=0:
                    print(i)
    elif opcion ==3:
        dinero= int(input("ingrese su dinero: "))
        costoOrdenas= costos.copy()
        costoOrdenas.sort()
        print(costoOrdenas)
        i=0
        while(dinero>=0):
            pos= costos.index(costoOrdenas[i])
            nom= prodL[pos]
            print(nom)
            i+=1
            dinero-=costoOrdenas[i] 
        # for i in costoOrdenas:
        #     dinero-=i
        #     pos= costos.index(i)
        #     nom= prodL[pos]
        #     print(nom)
    print("1)Consulta productos\n2)Encarecimiento\n3)Compra\n4)Salir")   
    opcion = input("Ingrese una opcion: ")
    while(not opcion.isdigit()):
        opcion= input("Ingrese una opcion del menú valida")
    opcion= int(opcion)
print("Gracias por usar el programa")
