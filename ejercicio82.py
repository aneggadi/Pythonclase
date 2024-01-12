#Anwar Neggadi

lista=[]
#ingresa 5 nombres y los almacena en la lista
for x in range (5):
    valor=input("Ingrese un nombre:")
    lista.append(valor)

menor=lista[0]
for x in range (1,5):
#compara los nombres
    if lista[x]<menor:
        menor=lista[x]
#imprime el nombre menor
print("El menor en orden alfabetico es:", menor)