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
MONTHS = ()


def get_calendar_for(year, month):
    cal_text = ""
    cal_text += (' ' * 34) + MONTHS[month - 1]


def main():
    pass


if __name__ == "__main__":
    main()
