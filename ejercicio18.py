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