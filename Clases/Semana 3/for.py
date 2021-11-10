opcion=""
while opcion!="5": 
    print("Bienvenido a la tienda Konoha\n1)Comprar anime\n2)Agregar anime\n3)Generar catalogo según presupuesto\n4) Recomendar animes por genero\n5)Salir")
    opcion= input("Ingrese su opción: ")
    if not opcion.isdigit(): 
        print("\nIngresa un numero valido\n ")
    if opcion=="1": 
        print("Comprar anime")
    elif opcion=="2": 
        print("Agregar anime")
    elif opcion=="3": 
        print("Generar catalogo según presupuesto")
    elif opcion=="4": 
        print("Recomendar animes por genero")
    elif opcion=="5": 
        print("Esta saliendo de la tienda ")