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
