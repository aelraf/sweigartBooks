# -*- coding: utf-8 -*-
# RafKac

"""
Gra ze średniowiecznej Japonii.

Dwie sześcienne kostki są pod kubkiem.
Zgadujemy, czy suma jest parzysta (even), czy nieparzysta (odd).

"""

import random
import sys


JAPANESE_NUMBERS = {1: 'ICHI', 2: "NI", 3: "SAN", 4: "SHI", 5: "GO", 6: "ROKU"}


def get_bet_casch(purse: int) -> int:
    print("Masz {} monet. Ile obstawiasz? (lub ZAKONCZ)".format(purse))
    while True:
        pot = input('> ')
        if pot.upper() == 'ZAKONCZ':
            print('Dziękuję za grę!')
            sys.exit()
        elif not pot.isdecimal():
            print("Proszę wprowadzić numer.")
            continue
        elif int(pot) > purse:
            print("Nie masz środków na tak duży zakład.")
            continue
        else:
            pot = int(pot)
            break

    return pot


def get_dices() -> ():
    """
    Losuje wartości obu kości i je zwraca.
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    return dice1, dice2


def get_bet_player_cho_or_han() -> str:
    bet = ''
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print("Proszę podaj 'CHO' albo 'HAN'. ")
            continue
        else:
            break

    return bet


def main():
    print("""
    Cho-Han, tradycyjna gra Japońska. Dwie kostki są w bambusowych filiżankach.
    Gracz musi zgadnąć, czy suma wyników jest parzysta (CHO), czy nieparzysta (HAN).
    """)
    purse = 5000
    while True:
        get_bet_casch(purse=purse)
        pass


if __name__ == "__main__":
    main()
