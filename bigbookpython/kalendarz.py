# -*- coding: utf-8 -*-
# RafKac
# na podstawie książki bigbookpython

"""
Program generuje plik tekstowy z miesięcznym kalendarzem dla miesiąca i roku podanego
przez użytkownika.

Za pilnowanie daty, przestępności, liczebności miesiąca etc odpowiada biblioteka datetime.
"""


import datetime


DAYS = ('Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota')
MONTHS = ('Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec',
          'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień')


def get_year_from_user() -> int:
    year = 0
    while True:
        print('Podaj rok dla kalendarza: ')
        response = input('> ')

        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break

        print('Proszę podać wartość liczbową, w stylu 2022.')
        continue

    return year


def get_calendar_for(year, month):
    cal_text = ""
    cal_text += (' ' * 34) + MONTHS[month - 1]


def main():
    pass


if __name__ == "__main__":
    main()
