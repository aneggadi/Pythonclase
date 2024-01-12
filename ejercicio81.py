#Anwar Neggadi

lista=[]
for x in range (5):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)

menor=lista[0]
posicion=0
for x in range (1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x
print("Lista completa:", lista)
print("Menor de la lista:", menor)
print("posicion del menor de la lista:", posicion)