#Anwar Neggadi

cantidad=0
valor=0
for f in range(10): #se repite 10 veces la funcion
    cantidad=cantidad+1
    if cantidad<6:
        num=int(input("Ingrese un valor:"))
    else:
        n=int(input("Ingrese un valor:"))
        valor=valor+n
print("La suma de los ultimos 5 numeros es:")
print(valor)
#lo que hace el programa es durante los 5 primeros valores no te cuenta nada a partir del 6 ya empieza a contar y sumar los valores
#y te imprime al finalizar la suma de los ultimos 5 numeros
