*** Settings ***
Documentation    A test suite for multiple cho-han game.
Library    Process


*** Test Cases ***
Bet Should Be Done Two Times
    Run Program    #shell=True


*** Keywords ***
Run Program
    #[Arguments]    @{args}
    Run Process    choHan.py    shell=True

