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
        elif response.startswith('o'):
            mode = "decrypt"
            break
        print('Wprowadź literę "z" lub "o".')

    return mode


def choose_key(symbols: str):
    """
    Zwraca wybrany przez użytkownika klucz szyfrowania.
    """
    key = None

    while True:
        maxKey = len(symbols) - 1
        print("Podaj klucz (od 0 do {})".format(maxKey))
        response = input("> ").upper()

        if not response.isdecimal():
            continue
        if 0 <= int(response) < len(symbols):
            key = int(response)
            break

    return key


def get_message(mode: str):
    print("Podaj wiadomość w trybie: {}".format(mode))
    message = input("> ")
    message = message.upper()

    return message


def do_translation():
    """
    Metoda szyfrująca otrzymają wiadomość w trybie podanym jako drugi paramter,
    kluczem podanym jako trzeci parametr.

    :return: przetworzoną wiadomość.
    """
    return 0


def main():
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print("szyfr Cezara, w oparciu o książkę Ala Sweigarta")

    mode = choose_mode()
    key = choose_key(SYMBOLS)
    message = get_message(mode)
    translated = do_translation()


if __name__ == "__main__":
    main()
