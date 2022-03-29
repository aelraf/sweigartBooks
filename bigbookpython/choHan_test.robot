*** Settings ***
Documentation    A test suite for multiple cho-han game.


*** Test Cases ***
Bet Should Be Done Two Times
    Run Program


*** Keywords ***
Run Program
    [Arguments]    @{args}
    Run Process    choHan.py    @{args}

