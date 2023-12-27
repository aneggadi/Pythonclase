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
