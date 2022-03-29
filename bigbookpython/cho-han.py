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


def which_are_correct(dice1: str, dice2: str) -> str:
    correct_bet = ""

    roll_is_even = (dice1 + dice2) % 2 == 0
    if roll_is_even:
        correct_bet = "CHO"
    else:
        correct_bet = "HAN"

    return correct_bet


def bet_result():



def main():
    print("""
    Cho-Han, tradycyjna gra Japońska. Dwie kostki są w bambusowych filiżankach.
    Gracz musi zgadnąć, czy suma wyników jest parzysta (CHO), czy nieparzysta (HAN).
    """)
    purse = 5000
    while True:
        pot = get_bet_casch(purse=purse)
        dice1, dice2 = get_dices()

        print("Prowadzący wrzuca kostki do filiżanek.")
        print('Kubki na podłodze - co obstawiasz?')
        print("CHO (parzyste) czy HAN (nieparzyste)")

        bet = get_bet_player_cho_or_han()

        print("prowadzący odsłania kubki pokazując zawartość: ")
        print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
        print('    ', dice1, '-', dice2)

        correct_bet = which_are_correct(dice1=dice1, dice2=dice2)

        player_won = bet == correct_bet

        bet_result()

        if purse == 0:
            print('Nie masz więcej pieniędzy.')
            print('dziękuję za grę!')
            sys.exit()


if __name__ == "__main__":
    main()
