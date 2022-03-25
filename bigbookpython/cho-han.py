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


def get_bet(purse: int):
    print("Masz {} monet. Ile obstawiasz? (lub ZAKONCZ)".format(purse))
    while True:
        pot = input('> ')
        if pot.upper() == 'ZAKONCZ':
            print('Dziękuję za grę!')
            sys.exit()
        elif not pot.isdecimal():
            print("Proszę wprowadzić numer.")


def main():
    while True:
        pass


if __name__ == "__main__":
    main()
