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
        raise ImportError


def choose_mode() -> str:
    """
    Zwraca wybrany tryb - szyfrowanie czy odszyfrowywanie.
    """
    mode = None
    while True:
        print("Czy chcesz (z)aszyfrować, czy (o)dszyfrować?")
        response = input("> ").lower()
        if response.startswith('z'):
            mode = "decrypt"
            break
        elif response.startswith('o'):
            mode = "encrypt"
            break
        print('Wprowadź literę "z" lub "o".')

    return mode


def choose_key(symbols: str) -> int:
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


def get_message(mode: str) -> str:
    print("Podaj wiadomość w trybie: {}".format(mode))
    message = input("> ")
    message = message.upper()

    return message


def do_translation(message: str, symbols: str, mode: str, key: int) -> str:
    """
    Metoda szyfrująca otrzymają wiadomość w trybie podanym jako drugi paramter,
    kluczem podanym jako trzeci parametr.

    :return: przetworzoną wiadomość.
    """
    translated = ""

    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)
            if mode == "encrypt":
                num += key
            elif mode == 'decrypt':
                num -= key

            if num >= len(symbols):
                num -= len(symbols)
            elif num < 0:
                num += len(symbols)
            translated += symbols[num]
        else:
            translated += symbol

    return translated


def copy_to_clipboard(words: str):
    try:
        import pyperclip

        try:
            pyperclip.copy(words)
            print("Cały przetworzony tekst skopiowany do schowka")
        except:
            pass

    except ImportError as err:
        print("importowanie - pyperclip Import Error")


def main():
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print("szyfr Cezara, w oparciu o książkę Ala Sweigarta")

    mode = choose_mode()
    key = choose_key(SYMBOLS)
    message = get_message(mode)
    translated = do_translation(message=message, symbols=SYMBOLS, mode=mode, key=key)

    print(translated)
    
    copy_to_clipboard(translated)


if __name__ == "__main__":
    main()
