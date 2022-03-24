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


def get_month_from_user() -> int:
    month = 0

    while True:
        print("Podaj miesiąc dla kalendarza, 1-12:")
        response = input('> ')

        if not response.isdecimal():
            print("Proszę podać numer miesiąca, 1 dla stycznia etc")
            continue

        month = int(response)
        if 1 <= month <= 12:
            break
        print("Proszę podać numer miesiąca między 1 a 12.")

    return month


def get_calendar_for(year, month):
    cal_text = ""
    cal_text += (' ' * 34) + MONTHS[month - 1] + " " + str(year) + '\n'
    cal_text += '...Niedziela.....Poniedziałek....Wtorek...Środa...Czwartek....Piątek....Sobota..\n'
    # dodajemy poziomą linię, rozdzielającą tekst
    week_separator = ('+----------' * 7) + '+\n'
    # pusty wiersz mający 10 spacji pomiędzy separatorami dni |
    blank_row = ('|          ' * 7) + '|\n'

    current_date = datetime.date(year, month, 1)

    # "przesuwamy" datę, zeby zaczynała się od niedzieli, zgodnie z naszym kalendarzem
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_separator

        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)

        day_number_row += '|\n'

        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        if current_date.month != month:
            break

    cal_text += week_separator
    return cal_text


def main():
    year = get_year_from_user()
    month = get_month_from_user()

    cal_text = get_calendar_for(year=year, month=month)
    print(cal_text)

    # zapisujemy kalendarz do pliku tekstowego
    calendar_filename = 'calendar_{}_{}.txt'.format(year, month)

    with open(calendar_filename, 'w') as file_obj:
        file_obj.write(cal_text)

    print("zapisano: " + calendar_filename)


if __name__ == "__main__":
    main()
