#Anwar Neggadi

oracion=input("Ingrese una calve de entre 10 y 20 caractertres:")#ingresa una oracion
if 10>len(oracion)>20: #lee la longitud de la oracion y la compara para ver si esta entre 10 y 20
    print("La oracion esta fuera del rango de letras") #si no lo estsa imprime error
else:
    print("La contraseña esta dentro del rango de letras")#si lo esta imprime esto