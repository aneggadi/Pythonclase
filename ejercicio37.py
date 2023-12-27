#Anwar Neggadi

x=1
y=1
list1=0
list2=0
while x<=15:
    lista1=int(input("ingrese los valores de la primera lista:"))
    list1=list1+lista1
    x=x+1
while y<=15:
    lista2=int(input("Ingrese el valor de la segunda lista:"))
    list2=list2+lista2
    y=y+1
if list1>list2:
    print("La primera lista es mayor")
if list2>list1:
    print("La segunda lista es mayor")
if list1 == list2:
    print("Las listas son iguales")