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
#mientras este en un rango elegido previamiente realizara el siguiente programa
#lee 3 lados, si los 3 lados son iguales añade uno al equilatero
#si 2 de los lados son iguales añade uno al isosceles 
#si no hay nignun lado igual suma uno al escaleno
#al termiar el bucle imrpime cuantos triangulos equilateros isosceles y escalenos has igresado