#Anwar Neggadi

sumam=0
sumat=0
suman=0
for f in range(5):
    turnm=int(input("Ingrese la edad de estudiante del turno de mañana:"))
    sumam=sumam+turnm
promediom=sumam/5
for x in range(6):
    turnt=int(input("Ingrese la edad de estudiante del turno de tarde:"))
    sumat=sumat+turnt
promediot=sumat/6
for y in range(11):
    turnn=int(input("Ingrese la edad de estudiante del turno de Noche:"))
    suman=suman+turnn
promedion=suman/11
print("El promedio de edad del turno de mañana es:", promediom)
print("El promedio de edad del turno de tarde es:", promediot)
print("El promedio de edad del turno de noche es:", promedion)
if promediom>promediot>promedion:
    print("El promedio de edad mas grande es el turno de mañana")
else:
    if promediot>promediom>promedion:
        print("El promedio de edad mas grande es el turno de tarde")
    else:
        print("El promedio de edad mas grande es el tuerno de noche")
#crea 3 bucles distinos, en el primer bucle se repite 5 veces el segundo bucle se repite 6 veces y el ultimo se repite 11 veces
#en cada bucle pide que ingreses la edad de los estudiantes de distintos tipos de turnos y hace la media de cada edad
#por ultimo imprime la media de edad de que cada turno