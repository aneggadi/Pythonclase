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