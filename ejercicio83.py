#Anwar Neggadi

lista=[]
for f in range(5):
    n=int(input("Ingrese un valor:"))
    lista.append(n)

mayor=0
repetido=0
i=0
for x in range (len(lista)): #el bucle se repite tantas veces como sea la longitud de la lista
    if lista[x]>mayor: #buscamos el mayor numero
        mayor=lista[x]
    if lista[x]==mayor: 
        repetido=repetido+1 #vemos si el numero mayor se repite y si se repite que sume uno
    if mayor!=lista[i]: #una vez tenemos el mayor volvemos a comparar un por uno por en la lista eso creamos otra variable i si el numero mayor es distinto a todos los valores de la lista sale que es uno
        i=i+1
        repetido=1 
print("La lista es:", lista)
print("El numero mayor es:", mayor)
if repetido>1: #por ultimo vemos si el numero mayor aparece mas de una vez y si aparece mas de una vez lo ponemos en plurar sino lo ponemos en singular ya que aparece solo una vez
    print("El numero mayor aparece:", repetido, "veces")
else:
    print("El numero mayor aparece:", repetido, "vez")