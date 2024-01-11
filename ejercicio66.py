#Anwar Neggadi

oracion=input("Ingrese la oracion:")
espacios=0
x=0
while x<len(oracion):
    if oracion[x]==" ": #(" ") esto significa espacio en blanco
        espacios=espacios+1
    x=x+1
print("La cantidad de espacios en la oracion es:", espacios)
#el programa ingresa unas oracion y dentro de la horacion busca caracter por caratcer buscando espacios en blanco