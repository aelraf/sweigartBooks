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
    try:
        while True:
            print('\n' * 60)

            hours = str(seconds_left // 3600)

            minutes = str((seconds_left % 3600) // 60)

            seconds = str(seconds_left % 60)

            h_digits = sevseg.get_sev_seg_str(hours, 2)
            h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

            m_digits = sevseg.get_sev_seg_str(minutes, 2)
            m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

            s_digits = sevseg.get_sev_seg_str(seconds, 2)
            s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

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
