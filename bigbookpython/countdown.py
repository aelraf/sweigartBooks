# -*- coding: utf-8 -*-
# RafKac

"""
Program wyświetla cyfrowo czas, odliczający do zera.

Autor - Al Sweigert, kod zaczerpnięty z książki "Big book python".
"""


import sys, time
import sevseg


seconds_left = 30


def main():
    global seconds_left
    try:
        while True:
            print('\n' * 2)

            hours = str(seconds_left // 3600)
            minutes = str((seconds_left % 3600) // 60)
            seconds = str(seconds_left % 60)

            h_digits = sevseg.get_sev_seg_str(hours, 2)
            h2 = h_digits.splitlines()
            h_top_row, h_middle_row, h_bottom_row = h2

            m_digits = sevseg.get_sev_seg_str(minutes, 2)
            h3 = m_digits.splitlines()
            m_top_row, m_middle_row, m_bottom_row = h3

            s_digits = sevseg.get_sev_seg_str(seconds, 2)
            h4 = s_digits.splitlines()
            s_top_row, s_middle_row, s_bottom_row = h4

            print(h_top_row    + "   " + m_top_row    + "   " + s_top_row)
            print(h_middle_row + " * " + m_middle_row + " * " + s_middle_row)
            print(h_bottom_row + " * " + m_bottom_row + " * " + s_bottom_row)

            if seconds_left == 0:
                print()
                print("   ***** BOOM *****   ")
                break

            print()
            print("Press Ctrl+C to quit")

            time.sleep(1)
            seconds_left -= 1

    except KeyboardInterrupt:
        print("cached Keyboard Interrupt")
        sys.exit()


if __name__ == "__main__":
    main()
