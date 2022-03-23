# -*- coding: utf-8 -*-
# RafKac
import sys
import unittest
from unittest import TestCase, mock
from unittest.mock import patch

import blackjack
from bagels import get_secret_num, NUM_DIGITS, get_clues
from birthdayproblem import get_birthdays, get_match
from szyfrCezara import *


class TestsBagels(TestCase):
    def test_get_secret_num(self):
        secret = get_secret_num()
        a1 = secret[0]
        a2 = secret[1]
        a3 = secret[2]

        assert len(secret) == NUM_DIGITS
        assert 0 <= int(a1) <= 9
        assert 0 <= int(a2) <= 9
        assert 0 <= int(a3) <= 9

    def test_get_clues_you_guess(self):
        guess = "123"
        secret_num = '123'

        result = get_clues(guess, secret_num)

        assert result == "Zgadłeś!"

    def test_get_clues_one_digit_properly(self):
        guess = "123"
        secret_num = '145'

        result = get_clues(guess, secret_num)

        assert result == 'Fermi'

    def test_get_clues_two_digit_properly(self):
        guess = "123"
        secret_num = '153'

        result = get_clues(guess, secret_num)

        assert result == "Fermi Fermi"

    def test_get_clues_two_digits_on_bad_places(self):
        guess = "123"
        secret_num = '612'

        result = get_clues(guess, secret_num)

        assert result == "Pico Pico"

    def test_get_clues_one_digit_on_bad_place(self):
        guess = "123"
        secret_num = '618'

        result = get_clues(guess, secret_num)

        assert result == "Pico"

    def test_get_clues_three_digits_on_bad_places(self):
        guess = "123"
        secret_num = '312'

        result = get_clues(guess, secret_num)

        assert result == "Pico Pico Pico"

    def test_get_clues_one_properly_one_on_bad_place(self):
        guess = "613"
        secret_num = '312'

        result = get_clues(guess, secret_num)

        assert result == "Fermi Pico"

    def test_get_clues_one_properly_two_on_bad_places(self):
        guess = "321"
        secret_num = '312'

        result = get_clues(guess, secret_num)

        assert result == "Fermi Pico Pico"


class TestBirthdayProblem(TestCase):
    def test_get_birthdays(self):
        lista = get_birthdays(10)

        assert lista is not []
        assert len(lista) == 10

    def test_get_birthdays_with_number_zero(self):
        lista = get_birthdays(0)

        self.assertEqual(lista, [])

    def test_get_match_empty_list(self):
        lista = []
        wynik = get_match(lista)

        self.assertIs(wynik, None)

    def test_get_match_without_match(self):
        birthdays = [1, 2, 3, 4, 5, 6, 7]
        wynik = get_match(birthdays)

        self.assertIs(wynik, None)

    def test_get_match_with_4_match(self):
        birthdays = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]
        wynik = get_match(birthdays)

        assert wynik == 1


class TestsBlackjack(TestCase):
    def test_get_bet_max_is_100_read_100(self):
        max = 100

        with mock.patch('builtins.input', return_value='100'):
            wynik = blackjack.get_bet(max_bet=max)

        assert wynik == 100

    def test_get_bet_max_is_1000_read_10(self):
        max = 1000

        with mock.patch('builtins.input', return_value='10'):
            wynik = blackjack.get_bet(max_bet=max)

        assert wynik == 10

    def test_get_deck(self):
        wynik = blackjack.get_deck()

        assert wynik != []
        assert len(wynik) == 52

    def test_get_hand_value_without_ases(self):
        cards = ['K', '2', '3']
        wynik = blackjack.get_hand_value(cards)

        assert wynik == 15

    def test_get_hand_value_with_one_ases(self):
        cards = ['K', 'Q', 'A']

        wynik = blackjack.get_hand_value(cards)

        assert wynik == 21

    def test_get_hand_value_with_two_ases(self):
        cards = ['6' 'A', 'A']
        wynik = blackjack.get_hand_value(cards)

        assert wynik == 17


class TestsSzyfrCezara(TestCase):
    def setUp(self) -> None:
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def test_import_pyperclip(self):
        with self.assertRaises(ImportError):
            import_pyperclip()

    def test_choose_mode_decrypt(self):
        with mock.patch('builtins.input', return_value='z'):
            wynik = choose_mode()

        assert wynik == 'decrypt'

    def test_choose_mode_encrypt(self):
        with mock.patch('builtins.input', return_value='o'):
            wynik = choose_mode()

        assert wynik == 'encrypt'

    def test_choose_key_decimal(self):
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        with mock.patch('builtins.input', return_value='10'):
            wynik = choose_key(SYMBOLS)

        assert wynik == 'encrypt'


if __name__ == "__main__":
    unittest.main()
