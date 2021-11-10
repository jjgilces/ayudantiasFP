#EJERCICIO 3 

#todas tienen edu
lista	=	["www.espol.edu.ec",	
		"www.google.com",	
		"www.sri.gob.ec",	
		"www.fiec.espol.edu.ec",	
		"www.uess.edu.ec",	
		"www.FIEC.espol.edu.ec",	
		"www.fict.espol.edu.ec",	
		"www.fcnm.Espol.edu.ec",	
		"www.ucsg.edu.ec",	
		"www.Stanford.edu",	
		"www.harvard.edu",	
		"www.stanford.edu",	
		"www.UCSG.edu.ec",	
		"www.google.com.ec",	
		"www.facebookedu.com",	
		"www.education.eduplatzi.com",	
		"www.educacionbc.edu.mx"]

#todas las universidad tienen edu 
universidades=[]
for url in lista: 
    informacion= url.split(".")
    if informacion[0]=="www" and (informacion[-1]=="edu" or informacion[-2]=="edu"): 
        indice = informacion.index("edu")
        universidad=informacion[indice-1].upper()
        universidades.append(universidad)
print(universidades)

universidadSR=list(set(universidades))
for i in range(len(universidadSR)): 
    uni= universidadSR[i]
    print(i+1,uni)

for i, uni in enumerate(universidadSR,1): 
    print(i,uni)

i=1
for uni in universidadSR: 
    print(i,uni)
    i+=1


veces= lista.count("www.jf.dk..e")



lista=[1,2,3]
tupla=2,4,6,4,6,6,5,3,2,24,5
conjunto={6,8,10}

conjuntoATupla= tuple(conjunto)
tuplaSR= list(set(tupla))
tuplSR= tuple(tuplSR)
listaAPRTTUPLA= list(tupla)