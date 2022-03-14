# -*- coding: utf-8 -*-
# RafKac
"""
Symulacja paradoksu urodzinowego (Birthday Paradox),
na podstawie kodu Ala Sweigarta.

Wykonujemy 100 000 symulacji.
"""

import datetime
import random


MONTHS = ('Jan', 'Feb', 'Mar', "Apr", 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', "Dec")


def get_birthdays(number_of_birthdays: int) -> list:
    """
    Zwraca listę losowych obiektów urodzin.
    """
    birthdays = []

    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days

        birthdays.append(birthday)

    return birthdays


def get_match(birthdays: list) -> datetime:
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a


def main():
    print("""
    Paradox urodzinowy, kod autorstwa Ala Sweigarta.
    
    Ten paradoks pokazuje nam, że w grupie N osób prawdopodobieństwo tego, że dwie będą miały
    urodziny tego samego dnia jest zaskakująco duże
    
    Program wykorzystuje medotę symulacji Monte Carlo do przedstawienia problemu.
    """)

    while True:
        print("Jak dużo urodzin generujemy? (Max 100)")
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            num_b_days = int(response)
            break
    print()

    print("Wygenerowane urodziny: {}".format(num_b_days))
    birthdays = get_birthdays(num_b_days)

    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print(date_text, end='')
    print('\n')

    match = get_match(birthdays)

    print('W tej symulacji, ', end='')
    if match is not None:
        month_name = MONTHS[match.month - 1]
        date_text = '{} {}'.format(month_name, match.day)
        print("Wielu ludzi ma urodziny: ", date_text)
    else:
        print('Nie ma dwóch takich samych urodzin')

    print('\n Generowanie {} losowych urodzin 100 000 razy...'.format(num_b_days))
    input('Wciśnij Enter, aby rozpocząć...')

    print('Uruchamiamy symulację 100 000 razy')
    sim_match = 0

    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, ' symulacja w toku...')
        birthdays = get_birthdays(num_b_days)
        if get_match(birthdays) is not None:
            sim_match += 1

    print('100_000 symulacji wykonano.')

    probability = round(sim_match / 100_000 * 100, 2)
    print('Na 100_000 symulacji {} ludzi było {} dopasowanych urodzin'.format(num_b_days, sim_match))
    print('Tzn. {} ludzi ma {} % szans na kogoś z taką samą datą urodzin'.format(num_b_days, probability))


if __name__ == "__main__":
    main()
