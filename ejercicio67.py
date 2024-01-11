#Anwar Neggadi

vocal=0
x=0
oracion=input("Ingrese una horacion:")#ingresamos una oracion
oracionmin=oracion.lower()#la convertimos en minusculuas para hacerlo mas facil
while x<len(oracion):
    if oracionmin[x]=="a" or oracionmin[x]=="e" or oracionmin[x]=="i" or oracionmin[x]=="o" or oracionmin[x]=="u":#buscamos las vocales
        vocal=vocal+1#contabilizamos las vocales
    x=x+1
print("La cantidad de vocales es:", vocal)#imprimimos la cantidad de vocales