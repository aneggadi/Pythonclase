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
#Mientras que el numero personas sea mayor que x va a repetir la siguiente secuencia
#Le ingresas un sueldo
#si el sueldo esta entre 100 y 300 añades 1 al gastomenor si es mayor que 300 añades uno al gastomayor
#hace la suma de del sueldo
# Por ultimo te imprime cauntas personas suponen un gasto menor cuantas un gasto mayor y cuanto es el gasto total de la empresa