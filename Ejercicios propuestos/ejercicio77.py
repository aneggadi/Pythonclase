#Anwar Neggadi

lista=[] #creamos una lista vacia
for f in range(5): #repetimos la funcion 5 veces
    num=float(input("Ingrese un sueldo con decimales:")) #ingresamos un sueldo con numeros decimales
    lista.append(num) #ingresamos los numeros decimales a la lista
promedio=(lista[1]+lista[2]+lista[3]+lista[4]+lista[5])/5 #hacemos la media
print("La lista es:",lista)
print("El primedio es:", promedio) #imprimimos la lista y la media de los sueldos
