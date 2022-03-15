# -*- coding: utf-8 -*-
# RafKac
# na podstawie książki bigbookpython

"""
Szyfr Cezara - prosty starożytny algorytm szyfrujący.
Szyfruje literę poprzez przesunięcie o stałą-klucz.

Program pozwala zaszyfrować i odszyfrować wiadomość.

Szyfr jest łatwy do złamania "Brutal-force".
"""


def import_pyperclip():
    try:
        import pyperclip
    except ImportError as err:
        print("importowanie - pyperclip Import Error")


def choose_mode():
    """
    Zwraca wybrany tryb - szyfrowanie czy odszyfrowywanie.
    """
    mode = None
    while True:
        print("Czy chcesz (z)aszyfrować, czy (o)dszyfrować?")
        response = input("> ").lower()
        if response.startswith('z'):
            mode = "encrypt"
            break
        elif response.startswith('o')
            mode = "decrypt"
            break
        print('Wprowadź literę "z" lub "o".')
        
    return mode


def main():
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print("szyfr Cezara, w oparciu o książkę Ala Sweigarta")

    mode = choose_mode()


if __name__ == "__main__":
    main()
