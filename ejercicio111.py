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
