#Anwar Neggadi

listaemp=[]
listasuel=[]
#crea dos listas separadas
x=0
n=int(input("Cuantos empleados trabajan en la empresa:"))
for f in range(n):
    empleados=input("Ingrese el nombre del empleado:")
    sueldo=int(input("Ingrese el sueldo del empleado:"))
    listaemp.append(empleados) #mete los datos ingresados por teclado dentro de las listas
    listasuel.append(sueldo)
    if listasuel[x]>10000: #compara si el sueldo es mayor y lo elimina si es mayor
        listaemp.pop(x)
        listasuel.pop(x)
        x=x-1 #x se resta ya que al eliminar la variable el tamaño de la lista dismunuye entonces tiene que restar 1
    x=x+1
print("Tus empleados son:", listaemp)
print("El sueldo de tus empleados es:", listasuel)
print("Los empleados que cobran menos de diezmil euros son:", listaemp)
print("Sus sueldos son:", listasuel)

