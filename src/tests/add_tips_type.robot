*** Settings ***
Resource  resource.robot

*** Keywords ***
Go To Main Menu From Book Tip Writer Selection
    Input Command  Montgomery LM
    Input Command  ${EMPTY}
    Input Command  ${EMPTY}
    Input Command  ${EMPTY}

Browse Output Contains The Created Book Tip
    Output Should Contain  1: Marcovaldo, kirja

*** Test Cases ***
Tip With Right Name And Type Is Saved
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Runotyttö etsii tähteään
    Go To Main Menu From Book Tip Writer Selection
    Select Quit Program From Main Menu
    Run Application
    Check Tips Title And Type Match  Runotyttö etsii tähteään  book

Tips Type Is Shown When Browsing Tips
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Marcovaldo
    Go To Main Menu From Book Tip Writer Selection
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Book Tip
