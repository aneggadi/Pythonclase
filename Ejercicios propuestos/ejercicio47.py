#Anwar Neggadi

n=int(input("Cuantos triángulos procesará:")) #pide qie ingreses cuantos valor vas a ingresar
cantidad=0
for x in range(n): #en funcion del valor ingresado anteriormente (n) realiza lo siguiente:
    basetri=int(input("Ingrese el valor de la base:")) 
    altura=int(input("Ingrese el valor de la altura:")) #pide que ingreses los valores de la base (basetri) y la alutra del triangulo
    superficie=basetri*altura/2 #calcula la superficie del triangulo (base*altura/2)
    print("La superficie es")
    print(superficie) #e imprime la superfice
    if superficie>12: 
        cantidad=cantidad+1 #si la superficie es mayor que 12 añade uno a la cantidad 
print("La cantidad de triángulos con superficie superior a 12 son")
print(cantidad) #fuera del bucle te imprime la cantidad de triangulos superiores a 12  