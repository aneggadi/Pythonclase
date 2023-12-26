#Anwar Neggadi

num1=int(input("Ingrese su sueldo:"))
num2=int(input("Ingrese el numero de años trabajados:"))
subida1=num1*1.2
subida2=num1*1.05
if num1<500 and num2<10:
    print("Le vamos a hacer un aumento del 20%")
    print(subida1)
else:
    if num1<500 and num2>10:
        print("Le vamos a hacer un aumento del 5%")
        print(subida2)
    if num1>500:
        print("El sueldo se queda como estaba")
        print(num1)
