import random

print("- - - - - INICIANDO BLACKJACK - - - - -")
jugador1 = str(input("Ingrese nombre del jugador 1:"))

jugador01 = 0
cuprier = 0
paloA = []
contfigura = 0

carta = int(random.randrange(1, 11))
palo = int(random.randrange(1, 8))
# Genero dos random, con el extremo superiro x+1

# Agregar lo de plantarse. adelante de cada if, con un if y un input. si se planta guardar sus datos
# Con el cuprier hacer lo mismo, solo que a el no se le da la opcion de seguir
jugador01 += carta
if palo == 10 or palo == 11 or palo == 12:
    contfigura += 1

if jugador01 == 21:
    print("Gano ", jugador1)
    print("Cantidad de figuras que le salio al jugador: ", contfigura)
else:
    carta1 = random.randrange(1, 11)
    palo = random.randrange(1, 8)
    jugador01 += carta1
    if palo == 10 or palo == 11 or palo == 12:
        contfigura += 1
        if jugador01 == 21:
            print("Gano ", jugador1)
            print("Cantidad de figuras que le salio al jugador: ", contfigura)
        else:
            carta2 = random.randrange(1, 11)
            palo = random.randrange(1, 8)
            jugador01 += carta2
            if palo == 10 or palo == 11 or palo == 12:
                contfigura += 1
                if jugador01 == 21:
                    print("Gano ", jugador1)
                    print("Cantidad de figuras que le salio al jugador: ", contfigura)
            elif jugador01 == 20:
                carta3 = random.randrange(1, 11)
                if carta3 == 11:
                    carta3 = 1
                    jugador01 += carta3
                    contfigura += 1
                    print("Gano ", jugador1)
                    print("Cantidad de figuras que le salio al jugador: ", contfigura)
            elif jugador01 < 21 and jugador01 != 20:
                carta4 = random.randrange(1, 11)
                palo = random.randrange(1, 8)
                paloA.append(palo)
                jugador01 += carta4
