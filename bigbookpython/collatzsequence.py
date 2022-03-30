# -*- coding: utf-8 -*-
# RafKac

"""
Ciąg Collatza:
- dla n parzystego następnikiem jest n/2
- dla n nieparzystego, następnikiem jest n*3 + 1
- dla n=1 kończymy działanie.

User podaje liczbę, program sprawdza, czy wyjdzie 1.
"""

import sys
import time


def get_n_from_user():
    while True:
        print("Podaj wartość początkową większą od 0 lub zakończ (QUIT):")
        response = input('> ')

        if not response.isdecimal():
            print('Dziękuję za uwagę, koniec programu.')
            sys.exit()

        if int(response) <= 0:
            print('Wartość n musi być większa od 0, podaj jeszcze raz.')
            continue






def main():
    print("""
    Ciąg Collatza to ciąg liczb począwszy od podanego przez użytkownika n,
    powstały wg zasad:
    1) n parzyste => następnik jest równy n/2
    2) n nieparzyste => następnik jest równy n * 3 + 1
    3) n == 1 => STOP
    """)


if __name__ == "__main__":
    main()
