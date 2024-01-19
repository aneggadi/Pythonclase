#Anwar Neggadi

lista=[1, 2, 3, 100, 101] #creamos una lista con 5 valores
x=0
while x<len(lista): #mientras que la longitud de la lista sea mayor que x hace lo siguiente
    if lista[x]>=7: #lee si algun numero es mayor que 7
        print(lista[x])
    x=x+1 #pasamos al siguiente numero de la lista