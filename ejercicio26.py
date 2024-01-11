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
#si el sueldo ingresado es menor a 500 y los años trabajdos son mas de diez te hace un aumento del 20% y te imprime el sueldo despues del aumento
#si el sueldo es menor a 500 pero los años trabajdados son menores a 10 años te hace un ingreso del 5% y te imprime el sueldo despues del aumento
#si el sueldo es mayor que 500 te dice que no te hace subida