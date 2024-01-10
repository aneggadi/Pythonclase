#Anwar Neggadi

num1=int(input("ingrese el numero de preguntas"))
num2=int(input("ingrese el numero de aciertos"))
porcentaje=(num2/num1)*100
if porcentaje>= 90:
    print("Tienes el nuvel maximo")
else:
    if 90>porcentaje>=75:
        print("Tienes el nivel medio")
    if 75>porcentaje>=50:
        print("Tienes el nivel regular")
    if 50>porcentaje:
        print("Estas fuera de nivel")
#Lee 2 numeros (el numero de prguntas y el numero de aciertos) y hace que si el numero es mayor o igual que 90% te dice que tienes el nivel maximo
#si tienes un porcentaje entre 90 y 75 te ice que tienes el nivel medio
#si estas entre el 75% y el 50% te dice que tienes un nivel regular
#y si es un % debajo del 50% te dice que estas fuera de nivel