# -*- coding: utf-8 -*-
# RafKac

"""
Wyświetlanie cyfr.

 __A__
|     |
F     B
|__G__|
|     |
E     C
|__D__|

"""


def get_sev_seg_str(number, min_width=0):
    number = str(number).zfill(min_width)

    rows = ['', '', '']

    for i, numeral in enumerate(number):
        if numeral == ".":
            rows[0] += ' '
            rows[1] += " "
            rows[2] += "."
            continue
        elif numeral == '-':
            rows[0] += '    '
            rows[1] += " __ "
            rows[2] += "    "
        elif numeral == "0":
            rows[0] += ' __ '
            rows[1] += "|  |"
            rows[2] += "|__|"
        elif numeral == "1":
            rows[0] += '    '
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "2":
            rows[0] += ' __ '
            rows[1] += " __|"
            rows[2] += "|__ "
        elif numeral == "3":
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == "5":
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == "6":
            rows[0] += " __ "
            rows[1] += "|__ "
            rows[2] += "|__|"
        elif numeral == "7":
            rows[0] += " __ "
            rows[1] += "   |"
            rows[2] += "   |"
        elif numeral == "8":
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += "|__|"
        elif numeral == "9":
            rows[0] += " __ "
            rows[1] += "|__|"
            rows[2] += " __|"

    return '\n'.join(rows)


if __name__ == "__main__":
    print("Ten moduł jest do importowania do innych zastosowań, a nie uruchamiania stricte")
    print('Na przykład, taki kod:')
    print('    import sevseg')
    print('    myNumber = sevseg.getSevSegStr(42, 3)')
    print('    print(myNumber)')
    print()
    print('...wydrukuje 42, poprzedzane zerem:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
