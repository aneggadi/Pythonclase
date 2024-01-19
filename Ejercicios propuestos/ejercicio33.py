#Anwar Neggadi

x=0
suma=0
nump=int(input("Cuantas personas vas a poner?"))
while x<nump:
    Altura=float(input("Ingrese la altura:"))
    suma=suma+Altura
    x=x+1
media=suma/nump
print("La media de altura es:")
print(media)
#mientras que x sea menor al numero de personas(nump) repite la secuencia
#la secuencia lo que hace es ingresar una altura en decimal y te hace la media de altura
#por ultimo te imprime la media