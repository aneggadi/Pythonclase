#Anwar Neggadi

cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0
n=int(input("Ingrese el numero de cordenadas que vas a escribir"))
for f in range (n):
    numx=(int(input("Ingrese un punto x:")))
    numy=(int(input("Ingrese un punto Y")))
    if numx>0 and numy>0:
        cuadrante1=cuadrante1+1
    else:
        if numx<0 and numy>0:
            cuadrante2=cuadrante2+1
        if numx<0 and numy<0:
            cuadrante3=cuadrante3+1
        else:
            cuadrante4=cuadrante4+1
print("El numero de coordenadas en el primer cuadrante es:", cuadrante1)
print("El numero de coordenadas en el segundo cuadrante es:", cuadrante2)
print("El numero de coordenadas en el tercer cuadrante es:", cuadrante3)
print("El numero de coordenadas en el cuarto cuadrante es:", cuadrante4)
#primero cuantas coordenadas vas ingresar y se crea un bucle que se repite durante el numero que hayas elegido
#y busca en que cuadrante esta dependiendo si los numeros ingresados son positivos negativos
#al finalizar el bucle te imprime la cantidad de coordenadas en cada cuadrante 