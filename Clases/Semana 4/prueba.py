datos="<detalles><canton>Guayaquil,450000,2000000</canton><canton>Duran,56000,1000000</canton><canton>Daule,1000,500000</canton><canton>Samborondon,2000,8000</canton></detalles>"
canton= datos.split("<detalles>")[1].split("</detalles>")[0]
canton= canton.split("<canton>")[1:]
cantones=[]
dato=[]
dato2=[]
for c in canton:
    ct=c.split("<")[0]
    can,dat,dat2=ct.split(",")
    cantones.append(can)
    dato.append(dat)
    dato2.append(dat2)
print(cantones)