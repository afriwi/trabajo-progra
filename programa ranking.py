#calcular promedio de 3 calificaciones (1-10) "Flow"
#Jason Flatt 9/10
#Anonimo 8/10
#Enrique Colmena 10/10

lista=[]
x=0
while x<3:
    calificación=int(input("agregue su calificación del 1 al 10: "))
    while calificación <1 or calificación> 10:
        calificación=int(input("error, agregue su calificación del 1 al 10: "))
    lista.append(calificación)
    x=x+1
promedio=(lista[0] + lista[1] +lista[2])//3
print('el promedio de las calificaciones es: ', promedio)
