#Anwar Neggadi

neg=0
pos=0
par=0
mul15=0
for f in range(10):
    num=int(input("Ingrese un numero:"))
    if num<0:
        neg=neg+1
    if num>0:
        pos=pos+1
    if num%2==0:
        par=par+1
    if num%15==0:
        mul15=mul15+1
print("La cantidad de numeros negativos es:", neg)
print("La cantidad de numewos positivos es:", pos)
print("La cantidad de numeros pares es:", par)
print("La cantidad de numeros multiplos de 15 es:", mul15)
#repite el bucle 10 veces
#en ese bucle ingresas un numero y lee si es negativo o positivo y si es par o multiplo de 15
#al finalzar te imprime la cantidad de numeros positivos,negativos,pares y multiplos de 15 ingresados