#Anwar Neggadi

x=0
gastot=0
gastomenor=0
gastomayor=0
nump=int(input("Cuantas personas trabajan en la empresa?"))
while x<nump:
    sueldo=int(input("Ingrese el sueldo:"))
    if 100<=sueldo<=300:
        gastomenor=gastomenor+1
    if sueldo>300:
        gastomayor=gastomayor+1
    gastot=gastot+sueldo
    x=x+1
print("El numero de personas de personas que cobran entre 100 y 300 euros son:")
print(gastomenor)
print("El numero de personas que cobran mas de 300 euros son:")
print(gastomayor)
print("El gasto de la empresa en sueldos es:")
print(gastot)