*** Settings ***
Resource  resource.robot

*** Test Cases ***
Tip With Right Name And Type Is Saved:
    Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Runotyttö etsii tähteään
    Input Stop And Run Application
    Check Tips Title And Type Match  Runotyttö etsii tähteään  book

Tips Type Is Shown When Browsing Tips
    Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Marcovaldo
    Browse Tips From Main Menu
    Quit Browsing Tips
    Input Stop And Run Application
    Output Should Contain  1: Marcovaldo, kirja

*** Keywords ***
