from random import *


print('*'*5 + ' BLACKJACK', '*'*5)
nom = input('Introduzca su nombre: ')

palos = 'pique', 'corazón', 'trébol', 'diamante'

end = False
carta_jugador = randint(1, 13)
carta_crupier = randint(1, 13)
ant_jugad = 0
ant_crup = 0
palo_jug = choice(palos)
palo_crup = choice(palos)
tot_jugador = carta_jugador
tot_crupier = carta_crupier
as_jugador = False
as_crupier = False

if carta_jugador == 1:
    as_jugador = True
if carta_crupier == 1:
    as_crupier = True

print('Primera carta del jugador: ', carta_jugador, 'de', palo_jug)
print('Primera carta del crupier: ', carta_crupier, 'de', palo_crup)

if palo_jug == palo_crup:
    print('El crupier y', nom, 'tienen el mismo palo en la primera carta!!')
    if carta_crupier == carta_jugador:
        print('El crupier y', nom, 'tienen el mismo palo y número en la primera carta!!')
    else:
        print('El crupier y', nom, 'tienen el mismo palo en la primera carta!!')

ant_jugad = carta_jugador
ant_crup = carta_crupier

carta_crupier = randint(1, 13)
print('Carta del crupier:', carta_crupier)
if as_crupier:
    if carta_crupier == 1:
        tot_crupier = 12
    else:
        if carta_crupier + 11 <= 21:
            tot_crupier = 11 + carta_crupier
            ant_crup = carta_crupier
            as_crupier = False
        else:
            tot_crupier = 1 + carta_crupier
            ant_crup = carta_crupier
            as_crupier = False
else:
    if carta_crupier == 1:
        if tot_crupier + 11 <= 21:
            tot_crupier += 11
            as_crupier = True
            ant_crup = carta_crupier
        else:
            tot_crupier += 1
    else:
        if carta_crupier + tot_crupier <= 21:
            tot_crupier += carta_crupier
        else:
            print('El crupier perdió')
            tot_crupier += carta_crupier
            end = True
print('Total del crupier:', tot_crupier)


if not end:
    print('Deséa otra carta?')
    op = int(input('Ingrese 1 para SI ; Ingrese 0 para NO: '))
    if op == 1:
        carta_jugador = randint(1, 13)
        print('carta del jugador: ', carta_jugador)
        if as_jugador:
            if carta_jugador == 1:
                tot_jugador = 12
            elif 11 + carta_jugador <= 21:
                tot_jugador = 11 + carta_jugador
                ant_jugad = carta_jugador
            else:
                tot_jugador += 1

        elif carta_jugador == 1:
            if tot_jugador + 11 <= 21:
                tot_jugador += 11
                ant_jugad = carta_jugador
            else:
                tot_jugador += 1
                ant_jugad = 1

        else:
            if carta_jugador + tot_jugador <= 21:
                tot_jugador += carta_jugador

            else:
                print('el jugador perdió')
                end = True
                tot_jugador += carta_jugador

        print('El total del jugador es', tot_jugador)

    else:
        if tot_crupier >= tot_jugador:
            print('Ganó el crupier')
        else:
            print('Ganó el jugador')

    if not end:
        if tot_crupier >= 16:
            print('El crupier se planta')
        else:
            print('El crupier pide otra')
            carta_crupier = randint(1, 13)
            print('Carta del crupier:', carta_crupier)
            if carta_crupier == 1:
                if tot_crupier + 11 <= 21:
                    tot_crupier += 11
                elif tot_crupier + 1 <= 21:
                    tot_crupier += 1
                else:
                    print('El crupier perdió')
                    print('Total de crupier: ', tot_crupier)
                    end = True

            else:
                if tot_crupier + carta_crupier <= 21:
                    tot_crupier += carta_crupier
                else:
                    print('El crupier perdió')
                    tot_crupier += carta_crupier
                    print('Total de crupier: ', tot_crupier)
                    end = True

    if not end:
        op = int(input('Desea otra carta?: (1 o 0): '))
        if op == 1:
            carta_jugador = randint(1, 13)
            print('Carta del jugador:', carta_jugador)
            if carta_jugador == 1:
                if tot_jugador + 11 <= 21:
                    tot_jugador += 11
                elif tot_jugador + 1 <= 21:
                    tot_jugador += 1
                else:
                    print('el jugador se pasó de 21')
                    end = True
                    print('Total del jugador:', tot_jugador)
                    print('Gana el crupier')
            else:
                if tot_jugador + carta_jugador <= 21:
                    tot_jugador += carta_jugador

                else:
                    print('el jugador se pasó de 21')
                    end = True
                    print('Total del jugador:', tot_jugador)
                    print('Gana el crupier')

    if not end:
        print('fin del juego')
        if tot_jugador > tot_crupier:
            print('Ganó el jugador')
        else:
            print('Ganó el crupier')

        print('\nTotales:')
        print('Total del jugador:', tot_jugador, '\nTotal del crupier:', tot_crupier)

else:
    print('El crupier se pasó de 21, usted ganó')
