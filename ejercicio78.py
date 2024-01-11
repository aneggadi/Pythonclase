#Anwar Neggadi

lista=[]
for f in range (5):
    altura=float(input("Ingrese una altura con decimales:"))
    lista.append(altura)
promedio=(lista[1]+lista[2]+lista[3]+lista[4]+lista[5])/5
x=0
maspromedio=0
menospromedio=0
while x<len(lista):
    if lista[x]>promedio:
        maspromedio=maspromedio+1
    else:
        menospromedio=menospromedio+1
    x=x+1
print("Las personas que estan por encima del promedio son:", maspromedio)
print("Las personas que estan por debajo del promedio son:", menospromedio)