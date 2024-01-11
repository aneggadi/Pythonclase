#Anwar Neggadi

x=1
suspensos=0
aprobados=0
while x<=10:
    nota=int(input("Ingrese un valor:"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        suspensos=suspensos+1
    x=x+1
print("El numero de aprobados es:")
print(aprobados)
print("El numero de suspensos es:")
print(suspensos)
#Repite la secuencia 10 veces y en cada secuencia te ingresa una nota si la nota es mayor a 7 suma 1 al numero de aprobados 
#pero si la nota es menor a 7 asumenta el numero de suspensos
#por ultimo te imprime el numero de aprobados y de suspensos