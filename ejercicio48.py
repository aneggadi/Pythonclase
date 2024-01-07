#Anwar Neggadi

cantidad=0
valor=0
for f in range(10):
    cantidad=cantidad+1
    if cantidad<6:
        num=int(input("Ingrese un valor:"))
    else:
        n=int(input("Ingrese un valor:"))
        valor=valor+n
print("La suma de los ultimos 5 numeros es:")
print(valor)
