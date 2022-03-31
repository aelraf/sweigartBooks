# https://robotframework.org/robotframework/3.1.1/RobotFrameworkUserGuide.html

*** Settings ***
Documentation    A test suite for multiple cho-han game.
Library    Process
Library    Collections
Library    OperatingSystem


*** Variables ***
@{FIRST_LIST}    100    1000    500    5000


*** Test Cases ***
Bet Should Be Done Two Times
    Run Program    shell=True
    FOR     ${ELEMENT}    IN    @{FIRST_LIST}
        Log To Console    ${\n} ${ELEMENT}
        Input Value Of Bet
        Random Value Of Dices
        Player Choose Cho Or Han
        Get Result Of The Bet
    END

*** Keywords ***
Run Program
    # poniższe mi uruchomi proces w nowym oknie,
    # a ja chcę po prostu instancję procesu do testów
    [Arguments]    @{args}
    # ${result}=    Run Process    python    choHan.py    shell=True

    # piąte podejście
    # ${result}=    Run Process    choHan.py    /I    shell=True

    # to podejście nic nie robi
    # Run    choHan.py @{args}

    # trzecia próba
    # Start Process    ${CURDIR}/choHan.py
    # też generuje OSError [WinError 193]

    # czwarta próba, wymaga biblioteki WhiteNoise,
    # Launch Application    python.exe    choHan.py

    # szósta próba - start process innaczej
    # zwraca znów OSError
    ${result}=    start process    choHan.py
    Log to console    ${\n} id procesu: ${result.pid}

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

