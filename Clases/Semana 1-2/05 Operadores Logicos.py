#Programa 005-OperadoresLógicos

print("****************************")
print("* 005 - Operadores Lógicos *")
print("****************************")

#Situación 1: Para tomar el vuelo necesitas dos requisitos obligatorios: la visa en tu pasaporte y el boleto aéreo. Si te falta uno de los requisitos obligatorios no podrás tomar el vuelo.

tengoVisa = True
tengoBoleto =   True

#Utiliza las dos variables anteriores para comparar si puedes tomar el vuelo o no. Para esto, utiliza el operador lógico adecuado.

puedoTomarElVuelo =  tengoBoleto and tengoVisa

#Muestra el resultado, ¿Puedes tomar el vuelo?
print('¿Puedes tomar el vuelo? ', puedoTomarElVuelo)

#Cambia los valores tengoVisa y tengoBoleto para ver cómo cambia el resultado en puedoTomarElVuelo.



#Situación 2: Es hora de comer y hay dos opciones de menú. Al menos debes escoger una de las opciones de menú para comer. 

seleccionarMenuContinental = True
seleccionarmenuAmericano = False

#Utiliza las dos variables anteriores para verificar si seleccionaste una de las opciones del menú. Para esto, utiliza el operador lógico adecuado.

menuSeleccionado = seleccionarmenuAmericano or seleccionarMenuContinental

#Muestra el resultado, ¿Ya tengo un menú seleccionado?
print('¿Ya tengo un menú seleccionado? ', menuSeleccionado)

#Cambia los valores seleccionarMenuContinental y seleccionarmenuAmericano para ver cómo cambia el resultado en menuSeleccionado.

#Situación 3: Ahora, debes seleccionar un asiento cerca de la ventana o cerca del pasillo. Si escoges un tipo de asiento ya no puedes escoger el otro tipo.

asientoPasillo = True
asientoVentana = False

#Muestra el resultado, ¿Tomaré el asiento de pasillo?
print('¿Tomaré el asiento de pasillo? ', asientoPasillo)
print('¿Tomaré el asiento de ventana? ', asientoVentana)

#Cambia solo el valor de asientoPasillo para ver cómo cambia el valor de asientoVentana.

#Situación 4: De acuerdo a tus facturas has hecho estos gastos

almuerzo = 3.2
dulces = 0.5
agua = 0.9

#Calcula el gasto total sumando los valores de las facturas.

gastoTotal = almuerzo+dulces+agua

#De acuerdo a tu presupuesto, podías gastar entre 0.01 y 5 dólares

limiteMinimo = 0.01
limiteMaximo = 5#Utiliza el gastoTotal para verificar si aún estás dentro del limiteMinimo y el limiteMaximo



puedoComprarChucherias = limiteMinimo<=gastoTotal<=limiteMaximo#Muestra el resultado, ¿Tus gastos aún están dentro de los límites? 

print("¿Tus gastos aún están dentro de los límites? ", puedoComprarChucherias)#Cambia el valor de limiteMaximo para ver cómo cambia el resultado de puedoComprarChucherias


#Situación 5: La aerolínea tiene nueva restricciones respecto a las dimensiones de la maleta de mano. Las maletas de mano deben tener una dimensión menor o igual que las restricciones 

restriccionLargo = 23
restriccionAncho = 15
restriccionProfundidad = 18

#Tu maleta de mano tiene las siguientes dimensiones

largo = 20.1
ancho = 14.5
profundidad = 20

#Utiliza las dimensiones de tu maleta y las restricciones de la aerolínea para verificar si cumple o no con todas las restricciones
#cumpleConTodas = 

#Utiliza las dimensiones de tu maleta y las restricciones de la aerolínea para verificar si falla con al menos una de las restricciones
#fallaAlMenosUna = 

#Muestra los resultados de las variables cumpleConTodas y fallaAlMenosUna, con el mensaje adecuado.

#Cambia el valor de las dimensiones de la maleta para ver cómo cambia el resultado de cumpleConTodas y fallaAlMenosUna