#Anwar Neggadi

lista=["paco", "juan", "dudi", "machiej", "moro"] #creamos una lista con 5 nombres
x=0
mayorigual5=0
while x<len(lista): #mientras que la longitud de la lista sea mayor que x hace lo siguiente
    if len(lista[x])>=5: #mira si la longitud de cada nombre es mayor que 5
        mayorigual5=mayorigual5+1 #si lo es suma 1 a la cantidad de nombres con 5 o mas letras
    x=x+1
print("La cantidad de nombres con 5 o mas caracteres son:", mayorigual5) #imprime la cantidad de nomnres con 5 o mas letras