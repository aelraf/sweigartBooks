# -*- coding: utf-8 -*-
# RafKac
# na podstawie kodu udostępnionego przez Ala Sweigerta

"""
Gra dla dwóch osób - marchew w pudełku.
Każdy gracz ma pudełko. W jednym z nich jest marchew, każdy gracz chce ją mieć.
Pierwszy gracz zagląda do swojego pudła i informuje drugiego, czy ma marchew.

Drugi gracz decyduje, czy zamienić pudła, czy nie.
"""


import random


carrot_in_first_box: bool = False


def start():
    print("""
    Gra dla dwóch ludzi. Każdy z nich ma pudło. W jednym pudle jest marchewka. 
    Aby wygrać, musisz mieć pudło z marchewką.
    
    Pierwszy gracz patrzy do swojego pudła (drugi nie podgląda).
    Pierwszy mówi "mam marchewkę" albo "nie mam". 
    Wtedy drugi decyduje, czy zamienić pudła, czy nie. 
    
    """)
    input('Press Enter to begin')


def what_in_box(name):
    print(name + " w swoim pudle masz: ")

    if random.randint(1, 2) == 1:
        carrot_in_first_box = True
    else:
        carrot_in_first_box = False

    if carrot_in_first_box:
        print("""
           __VV___
          |  VV   |
          |  VV   |
          |__||___|    ___________
         /   ||  /|   /         / |
        +-------+ |  +----------+ |
        |  RED  | |  |   GOLD   | |
        |  BOX  | /  |   BOX    | /
        +-------+/   +----------+/
          
          
        """)


def print_boxes(player_names, p1_name, p2_name):
    print("""
    Dwa pudła:
      _______      _______
     /      /|    /      /| 
    +------+ |   +------+ |
    | RED  | |   | GOLD | |
    |      | /   |      | /
    +------+/    +------+/
    """)

    print()
    print(player_names)
    print()
    print(p1_name + ', masz przed sobą czerwone pudło.')
    print(p2_name + ', masz przed sobą złote pudło.')
    print()
    print(p1_name + ", możesz zajrzeć do swojego pudła.")
    print(p2_name.upper() + ", zamknij oczy i nie podglądaj!")
    input("Kiedy " + p2_name + " zamknie oczy, wciśnij Enter...")
    print()

    what_in_box(name=p1_name)


def read_names() -> (str, str):
    p1_name = input("podaj imię pierwszego gracza: ")
    p2_name = input("podaj imię drugiego gracza: ")
    player_names = p1_name[:11].center(11) + "    " + p2_name[:11].center(11)
    print_boxes(p1_name=p1_name, p2_name=p2_name, player_names=player_names)
    print()


def main():
    pass


if __name__ == "__main__":
    main()
