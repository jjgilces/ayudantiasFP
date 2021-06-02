#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in [1,2,3]:
    print(i)


# # Ciclos

# ```
# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla un triángulo rectángulo como el de más abajo, de altura el número 
# introducido.
# ejem:
# >Ingrese un numero: 4
# *
# **
# ***
# ****
# ```
# 

# In[5]:


a=input("Ingrese un numero entero")
for i in range(1,int(a)+1):
    print("*"*i)


# ## Recorrido de Listas Paralelas
# 
# 
# *   zip
# *   Enumerate
# 

# In[13]:


n=["carlos", "Roberto"]
a=[16,19]
for nombre,anios in zip(n,a):
    print(nombre," ",anios)


# In[14]:


for indice,nu in enumerate(n):
    print(indice," ",nu)


# ### Ejercicio
# 
# ```
# Se tiene la siguiente lista de calificaciones y nombres:
# calificaciones=[7,5,3,4]
# nombres=["Carlos Loja","Javier Guevara","Robert Ruiz","Camila Ramirez"]
# Se pide mostrar por pantalla si el estudiante aprobo o no(Aprueba si su calificacion es mayor a 6), de la siguiente 
# forma:
# "El estudiante Carlos Loja ha aprobado"
# "El estudiante Javier Guevara ha reprobado"
# ...
# ```
# 

# In[15]:


calificaciones=[7,5,3,4]
nombres=["Carlos Loja","Javier Guevara","Robert Ruiz","Camila Ramirez"]
for nota,persona in zip(calificaciones,nombres):
    if nota>6:
        print ("El estudiante ",persona,"aprobo")
    else:
        print ("El estudiante ",persona,"reprobo")


# In[17]:


for nombre, dato in zip(nombres, calificaciones):
    if dato>6:
        print("EL ESTUDIANTE", nombre, "HA APROBADO")
    else:
        print("EL ESTUDIANTE", nombre, "HA REPROBADO")


# ### Ejercicio
# 
# Realizar un programa que verifique que los numeros igresados por el usuario son simetricos y luego de ello
# Mostrarle los numeros que no son simetricos.
# Para ello:
# Solicite al un usario que ingrese una cantidad cualquiera de numeros, separados por "," y
# trabajar con ello.
# 
# Ejem:
# 
# ```
# Ingrese los numeros: 2019, 1991, 1900, ..., 2000
# Los siguientes numero no son simetricos: 2019, 1900, ...., 2000
# ```

# In[19]:


anios=input("Ingreseme anios: ")
lista_anios=anios.split(",")
lista_ns=[]

for anio in lista_anios:
    a=anio.strip()
    reves=a[::-1]
    if a!=reves:
        lista_ns.append(a)

salida=", ".join(lista_ns)
print(salida)


# In[40]:


a=[1,2,3,4,5]
ab=a[1:4:-1]
print(ab)


# ### Ejercicio
# 
# El número EAN-13 (European Article Number) usado comercialmente en Europa en la identificación de productos, está constituido por 13 dígitos y con una estructura dividida en cuatro partes :
# 
# * 3 dígitos para el país,
# * 4 dígitos para la empresa,
# * 5 dígitos para el producto, y
# * Un dígito de control.
# 
# El dígito de control permite detectar errores de lectura del código, calculado como:
# 
# * Comenzando por la derecha, se multiplican los dígitos del código por 1 si su posición es par y por 3 si es impar
# * Se suman los valores de los productos obtenidos,
# * Se resta a la decena superior el resultado de la suma, siendo el resultado el dígito de control.
# 
# ![image.png](attachment:image.png)
# 
# ```
# Suma = 52
# decena superior = 60
# verificador calculado 60-52 = 8
# ```

# In[60]:


ingreso=input("Ingrese codigo: ")
digito_ver=int(ingreso[-1])
subs=ingreso[:-1]
suma=0
for indice,digito in enumerate(subs):
    digito=int(digito)
    if (indice+1)%2 ==0:
        suma=suma+(digito*3)
    else:
        suma+=digito
sig=suma//10
ds=(sig+1)*10
resta=ds-suma
if resta==digito_ver:
    print("Digito valido")
else:
    print("Digito invalido")


# In[ ]:





# ### Ejercicio
# Las aplicaciones para análisis de texto en internet (robots) siempre están trabajando para mejorar la eficacia del reconocimiento lingüístico. Para esta misión, los robots investigan el alfabeto teniendo como referencia:
# 
# ```
# vocales = 'AEIOU'
# consonantes = 'BCDFGHJKLMNPQRSTVWXYZ'
# ```
# Escriba un programa que dado un bloque de texto con palabras separadas por un espacio (‘ ‘) o un punto (‘.’), encuentre el número de palabras que tienen la misma cantidad de vocales y consonantes.
# 
# Ejemplo:
# 
# ![image.png](attachment:image.png)
# 
# Considere que el texto:
# * No contiene vocales con tildes.
# * NO se encuentran dos o más espacios seguidos o combinaciones de espacios y puntos.
# * Las mayúsculas y minúsculas no afectarán el resultado
# * Una palabra que contenga números no se la analiza.
# 

# In[ ]:





# En su programa usted ya tiene definida una lista con las **transacciones** de las tiendas de Marathon
# Sports en Guayaquil. Cada elemento de la lista es un string con los siguientes campos:
# sector```|tienda|categoria|producto|totalVentas|dia-mes-año``` que contiene el **total de ventas** en un **día**
# para un **producto** de una cierta **categoría** en una **tienda** ubicada en un determinado sector.
# 
# ![image.png](attachment:image.png)
# 
# Escriba sentencias un programa en Python que, usando la información dada, genere la siguiente
# información:
# 
# 1. Tres listas (sur,centro,norte) cuyos elementos son los nombres únicos de las tiendas: una lista por cada sector.
# 2. El total de ventas de los productos Adidas en el mes de mayo del año ingresado por teclado.

# In[ ]:





# 

# ## WHILE
# ```
# while condicion:
#     #haz algo
#     
# ```

# ### Ejercicio
# Solicitar el ingreso de un numero del 1 al 10 y permitirle al usuario ingresarle la 
# cantidad de veces necesarias para que adivine el numero que la computadora ha escogido.

# In[ ]:





# ### Ejercicio
# 
# La persistencia aditiva de un número entero se calcula sumando sus dígitos y en caso que esta sumatoria
# tenga más de un dígito, se repetirá el proceso sobre esta, hasta alcanzar un único dígito. La cantidad de
# veces que se requiera realizar la sumatoria hasta obtener un único dígito se denomina persistencia aditiva. 
# 
# * El número 1234 tiene una persistencia aditiva de 2 (la primera suma de dígitos es 10, luego la segunda suma es 1).
# * El número 5978 tiene una persistencia aditiva de 3 (5978→29→11→2).
# * El número 9 tiene una persistencia aditiva de 0.

# In[ ]:





# ### Ejercicio
# 
# ![image.png](attachment:image.png)
# ![image-2.png](attachment:image-2.png)

# In[ ]:





# ### Ejercicio
# 
# Como asistente de médico, usted tiene la tarea de generar un informe de indicadores a partir de un examen
# de sangre. El resultado del examen se lo entregan como una cadena de texto. Los indicadores los puede
# identificar porque estos siempre estarán en **mayúsculas**, por ejemplo INR, WBC, RBC, TA, etc. Todo
# indicador va seguido de un espacio, luego un número con decimales, seguido de otro espacio en blanco y
# finalmente las unidades. Al final del resultado se encuentra el nombre del médico. Ejemplos de resultados:
# 
# ```
# resultado = “Resultado de Laboratorio ‘Su Salud’ Nombre del paciente: Jose Aimas E-mail
# del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT
# 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC
# 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firma
# médico responsable Dr. Juan Pozo”
# resultado = “Resultado de Laboratorio ‘Sana’ Nombre del paciente: Ginger Irene Cruz
# Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL
# Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth
# Plaza”
# ```
# **La cantidad de indicadores puede variar. Los puntos no solo aparecen en los decimales, sino
# también para separar párrafos o en otras ocasiones como las direcciones de e-mail.**
# 
# Escriba un programa que nos muestre la información desglosada, el nombre del médico y una
# recomendación de si el paciente debe ir al endocrinólogo. Un paciente debe ir al endocrinólogo si su nivel
# de azúcar (BGT), está por encima de los 150 mmol/dL. **En caso de dar la recomendación, mostrar doble
# asterisco en el indicador BGT y la recomendación al final**. Para el primer ejemplo de arriba el informe
# sería:
# ![image.png](attachment:image.png)
# **No es necesario presentar el informe en el formato arriba descrito pero si lo hace, obtendrá 2
# puntos extras en el examen.**
# 

# In[ ]:





# In[88]:


import random as rd
l=["ROJO","AZUL","VERDE","CAFE","LILA","NARANJA"]
cr=rd.sample(l,4)
lista=[]
for c in cr:
    lista.append(c[0])

lista=["R","A","V","C"]

ingreso_usu=input("Ingrese colores")
valor_usu=["o"]*4

while  ["*"]*4!=valor_usu:
    
    for indice,letra in enumerate(ingreso_usu):
        if lista[indice]==letra:
            valor_usu[indice]="*"
    print("".join(valor_usu))
    if ["*"]*4!=valor_usu:
        valor_usu=["o"]*4
        ingreso_usu=input("Ingrese colores")
    
       
    


# In[ ]:


valor_usu=["*"]*4
print(valor_usu==["*"]*4)


# In[79]:


termino =False
numero=3
ingreso=input("Ingresa algo: ")
while not(termino):
    if numero==int(ingreso):
        termino=True
    else:
        ingreso=input("Ingresa algo: ")


# In[78]:


ingreso=input("Ingresa algo: ")
while numero!=int(ingreso):
    ingreso=input("Ingresa algo: ")
    


# In[ ]:




