# -*- coding: utf-8 -*-
# RafKac
# na podstawie książki bigbookpython
"""
gra logiczna, musisz zgadnąć trzy-cyfrowy numer w oparciu o wskazówki trzech typów:
Pico - dobra cyfra na złym miejscu
Fermi - dobra cyfra w dobrym miejscu
Bagels - jeśli Twoja odpowiedź nie zawiera poprawnych cyfr

Masz 10 prób na zgadnięcie odpowiedzi.
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num() -> str:
    """
    :return: stringa losowych cyfr w ilości NUM_DIGITS
    """
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess: str, secret_num: str) -> str:
    """
    :return:
    """
    if guess == secret_num:
        return 'Zgadłeś!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return '  '.join(clues)


def main():
    print("""
    Bagels, gra logiczna , zaprojektowana przez Ala Sweigarta.
    
    Spróbuj zgadnąć wylosowany ciąg {} niepowtarzających się cyfr. Wskazówki:
    - Pico - jedna poprawna cyfra na niewłaściwym miejscu
    - Fermi - jedna poprawna cyfra na właściwym miejscu
    - Bagels - żadna cyfra nie jest poprawna 
    """.format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print('Masz {} prób do zgadnięcia.'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print('Wykorzystałeś wszystkie próby')
                print('Prawidłowa odpowiedź to: {}'.format(secret_num))

        print("Czy chcesz grać jeszcze raz? (tak lub nie)")
        if not input('> ').lower().startswith('t'):
            break
    print("Dziękujemy za grę!")


if __name__ == "__main__":
    main()
