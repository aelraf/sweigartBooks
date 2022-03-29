# -*- coding: utf-8 -*-
# RafKac
import builtins
import sys
import unittest
from unittest import TestCase, mock
from unittest.mock import patch

import blackjack
from bagels import get_secret_num, NUM_DIGITS, get_clues
from birthdayproblem import get_birthdays, get_match
from szyfrCezara import *
from kalendarz import *
from choHan import *


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

    def test_choose_key_string(self):
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with mock.patch('builtins.input', return_value='10'):
            wynik = choose_key(SYMBOLS)

        assert wynik == 10

    def test_choose_key_decimal(self):
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        with mock.patch('builtins.input', return_value=22):
            with self.assertRaises(AttributeError):
                wynik = choose_key(SYMBOLS)

                assert wynik == 22

    def test_get_message_encrypted_small(self):
        mode = 'encrypt'

        with mock.patch('builtins.input', return_value="abc"):
            wynik = get_message(mode)

        assert wynik == 'ABC'

    def test_get_message_encrypted_big(self):
        mode = 'encrypt'

        with mock.patch('builtins.input', return_value="ABC"):
            wynik = get_message(mode)

        assert wynik == 'ABC'

    def test_do_translation_good_key_good_mode(self):
        message = "Ala ma kota".upper()
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mode = 'encrypt'
        key = 2

        wynik = do_translation(message=message, symbols=SYMBOLS, mode=mode, key=key)

        assert wynik == "CNC OC MQVC"

    def test_do_translation_to_big_key_good_mode(self):
        message = "Ala ma kota".upper()
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mode = 'encrypt'
        key = 29

        wynik = do_translation(message=message, symbols=SYMBOLS, mode=mode, key=key)

        assert wynik == "DOD PD NRWD"

    def test_do_translation_good_key_second_mode(self):
        message = "CNC OC MQVC".upper()
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mode = 'decrypt'
        key = 2

        wynik = do_translation(message=message, symbols=SYMBOLS, mode=mode, key=key)

        assert wynik == "ALA MA KOTA"

    def test_do_translation_good_key_bad_mode(self):
        message = "ALA MA KOTA"
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mode = 'something'
        key = 2

        wynik = do_translation(message=message, symbols=SYMBOLS, mode=mode, key=key)

        assert wynik == "ALA MA KOTA"

    def test_copy_to_clipboard(self):
        words = "Ala ma kota"
        with self.assertRaises(ImportError):
            copy_to_clipboard(words=words)


class TestsKalendarz(TestCase):
    def test_get_year_from_user(self):
        with mock.patch('builtins.input', return_value="2022"):
            wynik = get_year_from_user()

        assert wynik == 2022

    def test_get_year_from_user_small_date(self):
        with mock.patch('builtins.input', return_value='1'):
            wynik = get_year_from_user()

            assert wynik == 1

    def test_get_year_from_user_big_date(self):
        with mock.patch('builtins.input', return_value='123456789012345678901234567890'):
            wynik = get_year_from_user()

            assert wynik == 123456789012345678901234567890

    def test_get_month_from_user_1(self):
        with mock.patch('builtins.input', return_value="1"):
            wynik = get_month_from_user()

        assert wynik == 1

    def test_get_month_from_user_12(self):
        with mock.patch('builtins.input', return_value="12"):
            wynik = get_month_from_user()

        assert wynik == 12

    def test_get_month_from_user_7(self):
        with mock.patch('builtins.input', return_value="7"):
            wynik = get_month_from_user()

        assert wynik == 7

    def test_get_calendar_for(self):
        year = 2022
        month = 4

        wynik = get_calendar_for(year=year, month=month)

        self.assertRegex(wynik, "...")
        self.assertRegex(wynik, "Poniedziałek")
        self.assertRegex(wynik, "Środa")
        self.assertRegex(wynik, "Czwartek.....Piątek")
        self.assertRegex(wynik, "30")

        self.assertNotRegex(wynik, "32")

    def test_get_calendar_for_february_2021(self):
        year = 2021
        month = 2

        wynik = get_calendar_for(year=year, month=month)

        self.assertRegex(wynik, 'Środa')
        self.assertRegex(wynik, '28')
        self.assertRegex(wynik, '1')

        self.assertNotRegex(wynik, '29')
        self.assertNotRegex(wynik, '30')


class TestsChoHan(TestCase):
    def test_get_bet_casch(self):
        purse = 100

        with mock.patch('builtins.input', return_value="100"):
            pot = get_bet_casch(purse)

            assert pot == 100

    def test_get_dices(self):
        dice1, dice2 = get_dices()

        self.assertIsInstance(dice1, int)
        self.assertIsInstance(dice2, int)

        assert 0 < dice1 < 7
        assert 0 < dice2 < 7

    def test_get_bet_player_cho_or_han(self):
        with mock.patch("builtins.input", return_value='CHO'):
            bet = get_bet_player_cho_or_han()

            assert bet == "CHO"

    def test_get_bet_player_cho_or_han_han(self):
        with mock.patch("builtins.input", return_value='HAN'):
            bet = get_bet_player_cho_or_han()

            assert bet == "HAN"

    def test_which_are_correct_cho(self):
        dice1 = 1
        dice2 = 2

        wynik = which_are_correct(dice1=dice1, dice2=dice2)

        self.assertEqual(wynik, 'HAN')

    def test_which_are_correct_han(self):
        dice1 = 5
        dice2 = 3

        wynik = which_are_correct(dice1=dice1, dice2=dice2)

        self.assertEqual(wynik, 'CHO')

    def test_which_are_correct_both_odd(self):
        dice1 = 6
        dice2 = 6

        wynik = which_are_correct(dice1=dice1, dice2=dice2)

        self.assertEqual(wynik, 'CHO')


if __name__ == "__main__":
    unittest.main()
