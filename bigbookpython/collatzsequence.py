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


def get_n_from_user() -> int:
    while True:
        print("Podaj wartość początkową większą od 0 lub zakończ (QUIT):")
        response = input('> ')

        if not response.isdecimal():
            print('Dziękuję za uwagę, koniec programu.')
            sys.exit()

        if int(response) <= 0:
            print('Wartość n musi być większa od 0, podaj jeszcze raz.')
            continue

        if int(response) > 1:
            return int(response)


def collatz_sequence(n: int):
    print(str(n) + ", ", end='', flush=True)

    i = 0
    liczba = n

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        i += 1
        print(str(n) + ', ', end='', flush=True)
        if i % 10 == 0:
            print()
        time.sleep(0.1)

    print("\n ilość wyrazów w ciągu dla n={}: {}".format(liczba, i))


def main():
    print("""
    Ciąg Collatza to ciąg liczb począwszy od podanego przez użytkownika n,
    powstały wg zasad:
    1) n parzyste => następnik jest równy n/2
    2) n nieparzyste => następnik jest równy n * 3 + 1
    3) n == 1 => STOP
    """)
    while True:
        n = get_n_from_user()
        collatz_sequence(n=n)


if __name__ == "__main__":
    main()
