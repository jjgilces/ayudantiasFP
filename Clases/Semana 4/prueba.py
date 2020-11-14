prodsL=[]
costosL=[]
eL=[]
print("1)Consulta de productos\n2)Encarecimiento de productos\n3)Compra productos\n4)Salir")

opc = int(input("Ingrese una opcion del menú"))
while(opc!=4):
    if(opc==1):
        valor = float(input("Ingrese un valor de referencia"))
        for i in range(len(costosL)):
            if(costosL[i]>=valor):
                print(prodsL[i], costosL[i])
    if(opc==2):
        enc = input("Ingrese el encarecimiento\n1)Positivo\n2) Negativo").lower()
        while(enc!="positivo" or ec!="negativo"):
              enc = input("Ingrese un encarecimiento correcto\n1)Positivo\n2) Negativo").lower()
        lista=[]
        if(enc=="positivo"):
            for i in eL:
                if(i>0):
                    lista.append(i)
        elif(enc=="negativo"):
            for i in eL:
                if(i<0):
                    lista.append(i)
        print("La cantidad de productos con encarecimiento",enc,"es",len(lista))
        print("El promedio es", sum(lista)/len(lista))
    if (opc==3):
        dinero = int(input("Ingrese su dinero:"))
        costoO = costosL.copy()
        costoO.sort
        print(costoO)
        print("Su dinero le alcanza a comprar:")
        while(dinero>0):
            for i in costoO:
                ind= costosL.index(i)
                dinero-=i
                print(prodsL[ind])
    


