#Anwar Neggadi

equilatero=0
isosceles=0
escaleno=0
n=int(input("Cuantos triangulos quieres hacer:"))
for f in range(n):
    lado1=int(input("Ingrese el valor de un lado:"))
    lado2=int(input("Ingrese el valor de otro lado:"))
    lado3=int(input("Ingrese el valor del ultimo lado:"))
    if lado1==lado2==lado3:
        equilatero=equilatero+1
    else:
        if lado1==lado2 or lado2==lado3 or lado1==lado3:
            isosceles=isosceles+1
        else:
            escaleno=escaleno+1
print("El numero de triangulos equilateros es:", equilatero)
print("El nummero de triangulos isosceles es:", isosceles)
print("El numero de triangulos escalenos es:", escaleno)