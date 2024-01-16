import random

# Baraja de cartas
baraja = [
    '2 ' + chr(3), '3 ' + chr(3), '4 ' + chr(3) , '5 ' + chr(3), '6 ' + chr(3), '7 ' + chr(3), '8 ' + chr(3),
    '9 ' + chr(3), '10 ' + chr(3), 'J ' + chr(3), 'Q ' + chr(3), 'K ' + chr(3), 'A ' + chr(3),
    '2 diamantes', '3 diamantes', '4 diamantes', '5 diamantes', '6 diamantes', '7 diamantes', '8 diamantes',
    '9 diamantes', '10 diamantes', 'J diamantes', 'Q diamantes', 'K diamantes', 'A diamantes',
    '2 picas', '3 picas', '4 picas', '5 picas', '6 picas', '7 picas', '8 picas',
    '9 picas', '10 picas', 'J picas', 'Q picas', 'K picas', 'A picas',
    '2 tréboles', '3 tréboles', '4 tréboles', '5 tréboles', '6 tréboles', '7 tréboles', '8 tréboles',
    '9 tréboles', '10 tréboles', 'J tréboles', 'Q tréboles', 'K tréboles', 'A tréboles'
]
 
# Función para repartir cartas
def repartir_cartas(numero_cartas):
    return random.sample(baraja, numero_cartas)
 
# Ejemplo de repartición de cartas
mano_jugador = repartir_cartas(5)
n=0
print("Tu mano:")
while n<5:
    print( mano_jugador[n])
    n=n+1