#Anwar Neggadi

lista=[]
for f in range(5):
    n=int(input("Ingrese un valor:"))
    lista.append(n)

mayor=0
repetido=0
for x in range (len(lista)):
    print(lista[x])
    print(mayor)
    if lista[x]>mayor:
        mayor=lista[x]
    if lista[x]==mayor:
        repetido=repetido+1
        print("El numero mayor se repite:", repetido)
print("La lista es:", lista)
print("El numero mayor es:", mayor)