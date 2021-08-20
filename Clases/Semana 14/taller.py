import numpy as np

productos=["carne","queso","leche","detergente","pollo","pescado","cebolla","tomate","pimiento","naranja","sandia","papaya","pimienta"]

fechas = ["2020-03-20","2020-05-04","2020-05-31","2020-07-28","2020-08-09","2020-06-09","2020-03-22","2020-04-16","2020-07-31","2020-07-29","2020-06-18"]
compras= ["2020-07-31,tomate|14;pollo|13;pimiento|4","2020-07-29,naranja|15;pimienta|3","2020-06-18,carne|1;papaya|2;pescado|22","2020-07-28,pimiento|1"]
"fecha(aaaa-mm-dd),leche|4;...."
n_filas=len(fechas)
n_colum=len(productos)
M=np.zeros((n_filas,n_colum))
print(M)
#nombre,id,apellido
for compra in compras: 
    fecha,info_productos=compra.split(",")
    lista_productos=info_productos.split(";")
    posicionFila= fechas.index(fecha)
    #fecha 2020-07-31
    # print(lista_productos)
    for producto in lista_productos: 
        p,c=producto.split("|")
        c=int(c)
        posicon_columna= productos.index(p)
        M[posicionFila,posicon_columna]+=c
print(M)
print(fechas)
def mas_comprado_mes(M,mesUser,fechas,productos):
    meses=[]
    for fecha in fechas: 
        year,mes,dia= fecha.split("-")
        meses.append(int(mes))
    print(meses)
    meses=np.array(meses)
    condicion= meses==mesUser
    submatriz_mes=M[condicion,:]
    condicion_aparecido= submatriz_mes>=1
    suma_productos= np.sum(condicion_aparecido,axis=0)
    indice_mayor= np.argmax(suma_productos)
    producto_mayor= productos[indice_mayor]
    return producto_mayor
producto_masC=mas_comprado_mes(M,7,fechas,productos)

print(producto_masC)

def top_5_articulos(M, fechas, productos): 
    total_productos=np.sum(M,axis=0)
    indices_ordenados=np.argsort(total_productos)[::-1]
    array_productos=np.array(productos)
    productos_ordenados= array_productos[indices_ordenados]
    productos_top5= productos_ordenados[:5]
    return productos_top5
    
top5=top_5_articulos(M,fechas,productos)
print(top5)