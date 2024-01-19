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
#te pide que ingreses cuantos numeros vas a poner el codigo se repite tantas veces como numeros quieras poner
#ingresas el numero y te busca el resto de su division entre 2, si es 0 (significa que es par) suma uno al par
#si es uno es impar. Al final te imprime cuantos numeros pares e impares has puesto