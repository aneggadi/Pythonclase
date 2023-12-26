#Anwar Neggadi

num1=int(input("Ingrese un numero de hasta tres cifras:"))
if 9>=num1>=0:
    print("tu numero tiene una cifra")
else:
    if 99>=num1>=10:
        print("Tu numero tiene 2 cifras")
    if 999>=num1>=100:
        print("Tu numero tiene 3 cifras")
    else:
        print("No te pases crack")