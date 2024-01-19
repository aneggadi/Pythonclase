#Anwar Neggadi

num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))
num3=int(input("Ingrese el tercer numero:"))
print("El mayor numero de los dos es:")
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)