num1=(int(input("Ingrese su primer numero:")))
num2=(int(input("Ingrese su segundo numero:")))
num3=(int(input("Ingrese su ultimo valor:")))
valor12=num1-num2
valor13=num1-num3
valor21=num2-num1
valor23=num2-num3
valor31=num3-num1
valor32=num3-num2
if num1>num2>num3:
    print("El rango de variacion es:")
    print(valor13)
    print("El numero mas grande es:")
    print(num1)
else:
    if num1>num3>num2:
        print("El rango de variacion es:")
        print(valor12)
        print("El numero mas grande es:")
        print(num1)
    if num1>num2>num3:
        print("El rango de variacion es:")
        print(valor13)
        print("El numero mas grande es:")
        print(num1)