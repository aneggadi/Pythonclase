#Anwar Neggadi

lista=[]
x=0
for f in range(5):
    n=int(input("Ingrese un valor:"))
    lista.append(n)
print(lista)
while x<len(lista):
    if lista[x]>=10:
        lista.pop(x)
        x=x-1
    x=x+1
print(lista)
#crea una ista y repite un bucle 5 veces qwue ingresa 5 valores distintos luego compara la longitud de la lista y si algun valor de la listas es mayor igual que 10 elimina el valor de la lista
