#Anwar Neggadi

oracion=input("Ingrese la oracion:")
espacios=0
x=0
while x<len(oracion):
    if oracion[x]==" ":
        espacios=espacios+1
    x=x+1
print("La cantidad de espacios en la oracion es:", espacios)