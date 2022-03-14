# -*- coding: utf-8 -*-
# RafKac
"""
Blackjack - gra karciana, innaczej zwana "21". Gracz próbuje zgadnąć jak najbliżej 21 punktów,
Na podstawie kodu Ala Sweigarta.

Król, królowa, Walet dają 10 punktów.
Asy to 1lub 11 punktów.
karty od 2 do 10 są wartości ich liczby.
H - weź kolejnąkartę,
S - przestań brać karty
D - zmniejszenie zakładu
Kasa - 5000
"""

import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def get_bet(max_bet: int) -> int:
    """
    Pyta gracza, ile obstawi w tej rundzie.
    """
    while True:
        print("Ile obstawiasz? (1-{}, lub QUIT)".format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Dziękuję za grę!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck() -> list:
    """
    Zwraca listę krotek dla wszystkich 52 kart.
    """
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def get_hand_value(cards: list) -> int:
    """
    Zwraca wartości kart
    """
    value = 0
    number_of_aces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards: list):
    """
    Wyświetla szystkie karty z listy cards
    """
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' __ '
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, "_"))

    for row in rows:
        print(row)


def display_hands(player_hand: list, dealer_hand: list, show_dealer_hand: bool):
    """
    Pokazuje karty gracza oraz dilera. Ukrywa pierwszą kartę dilera, jeśli show_dealer_hand jest False
    """
    print()
    if show_dealer_hand:
        print('DEALER: ', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])

    print('PLAYER: ', get_hand_value(player_hand))
    display_cards(player_hand)


def get_move(player_hand: list, money: int) -> str:
    """
    Pyta graczao ruch, zwraca 'H' dla trafienia, 'S' dla pozostania, 'D' zmniejszenie stawki
    """
    while True:
        moves = ['(H)it', '(S)tand']
        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com
 
       Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True:
        if money <= 0:
            print("Jesteś spłukany!")
            print("Dobrze, że nie grałeś na prawdziwe pieniądze! ")
            print("dziękuję za grę")
            sys.exit()

        print('Money: ', money)
        bet = get_bet(money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print("Bet: ", bet)

        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print("Zakład urósł do: {}".format(bet))
                print("Stawka: ", bet)

            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print('Wyciągnąłeś {}  {} '.format(rank, suit))
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break
                input('press Enter to continue... ')
                print('\n\n')

        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print('Dealer busts! Wygrałeś ${}!'.format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print("Przegrałeś!")
            money -= bet
        elif player_value > dealer_value:
            print('Wygrałeś ${}!'.format(bet))
            money += bet
        elif player_value == dealer_value:
            print('Remis - stawka wraca do Ciebie')

        input('wciśnij Enter, aby kontynuować...')
        print('\n\n')


if __name__ == "__main__":
    main()
