#Anwar Neggadi

numt=int(input("Cuantos numeros vas a poner?"))
x=0
par=0
impar=0
while x<numt:
    num=int(input("Ingrese un valor:"))
    x=x+1
    numpar=num%2
    if numpar==0:
        par=par+1
    if numpar==1:
        impar=impar+1
print("El numero de numeros pares es:")
print(par)
print("El numero de numeros impares es:")
print(impar)