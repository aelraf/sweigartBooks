# -*- coding: utf-8 -*-
# RafKac
"""
Program używa wieloliniowego Stringa jako bitmapy, czyli dwuwymiarowego obrazu z tylko dwoma kolorami
możliwymi dla każdego piksela. W dodatku bitmapa będzie wiadomością dla użytkownika (spacja jako puste,
inny znak jako "niepuste".

Autor: Al Sweigart, Big book of small python projects.
"""


import sys


bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
 ....................................................................
"""


def main():
    print("Bitmap message")
    print("Enter the message to display the bitmap.")
    message = input('> ')
    if message == '':
        sys.exit()

    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == ' ':
                print(' ', end='')
            else:
                print(message[i % len(message)], end='')
        print()


if __name__ == "__main__":
    main()
