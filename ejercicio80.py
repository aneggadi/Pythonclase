#Anwar Neggadi

lista=[]
for x in range (5):
    valor=int(input("Ingrese un valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range (1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print("Lista completa", lista)
print("Mayor de la lista", mayor)
