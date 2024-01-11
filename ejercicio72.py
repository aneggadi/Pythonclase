#Anwar Neggadi

lista=[1, 2, 3, 100, 101, 6, 7, 200] #creamos una lista con 8 valores
valormas100=0
x=0
while x<len(lista): #mientras que la longitud de la lista sea mayor que x hace lo siguiente
    if lista[x]>100: #lee si algun numero es mayor que 100
        valormas100=valormas100+1 #si es asi añadimos uno 
    x=x+1 #pasamos al siguiente numero de la lista
print("Los valores de la lista mayores de 100 son:", valormas100) #imprimimos la cantidad de numeros mayores que 100