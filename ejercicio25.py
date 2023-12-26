#Anwar Neggadi

numx=(int(input("Ingrese un punto x:")))
numy=(int(input("Ingrese un punto Y")))
if numx>0 and numy>0:
    print("Los puntos estan en el primer cuadrante")
else:
    if numx<0 and numy>0:
        print("Los puntos estan en el segundo cuadrante")
    if numx<0 and numy<0:
        print("Los puntos estan en el tercer cuadrante")
    else:
        print("Los puntos estan en el cuarto cuadrante")