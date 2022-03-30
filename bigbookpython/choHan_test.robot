*** Settings ***
Documentation    A test suite for multiple cho-han game.
Library    Process
Library    Collections


*** Test Cases ***
Bet Should Be Done Two Times
    Run Program
    Input Value Of Bet
    Random Value Of Dices
    Player Choose Cho Or Han
    Get Result Of The Bet


*** Keywords ***
Run Program
    # poniższe mi uruchomi proces w nowym oknie,
    # a ja chcę po prostu instancję procesu do testów
    # Run Process    choHan.py    shell=True

    Log To Console    ${\n} Pierwszy test do Cho-Han - uruchamiamy gre
    Log To Console    ${\n} Gra zostala uruchomiona, wczytujemy dane.

Input Value Of Bet
    Log To Console    ${\n} Podajemy wartosc zakladu

Random Value Of Dices
    Log To Console    ${\n} losowa wartosc kosci

Player Choose Cho Or Han
    Log To Console    ${\n} gracz wybiera Cho lub Han

Get Result Of The Bet
    Log To Console    ${\n} wynik zakladu:

