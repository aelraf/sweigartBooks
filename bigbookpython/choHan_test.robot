*** Settings ***
Documentation    A test suite for multiple cho-han game.
Library    Process
Library    Collections


*** Test Cases ***
Bet Should Be Done Two Times
    Run Program


*** Keywords ***
Run Program
    #[Arguments]    @{args}
    # poniższe mi uruchomi proces w nowym oknie,
    # a ja chcę po prostu instancję procesu do testów
    # Run Process    choHan.py    shell=True
    Log To Console   ${\n} Pierwszy test do Cho-Han - uruchamiamy gre
    Log To Console   ${\n} Gra zostala uruchomiona, wczytujemy dane.

