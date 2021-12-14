*** Settings ***
Resource  resource.robot

*** Keywords ***
Browse Tips From Main Menu
    Input Command  2

Quit Browsing Tips
    Input Command  l

Add New Book Tip On Book Written By
    [Arguments]  ${book}  ${author}
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  ${book}
    Input Writer  ${author}
    Input ISBN  0
    Input Description  ${EMPTY}

Output Contains Browse Tips Instructions
    ${browse greet} =  Get Ui Message  BrowseTips  GREET_TEXT
    Output Should Contain  ${browse greet}

Output Contains Browse Tips Listing For Book
    [Arguments]  ${book}
    Output Should Contain  1: ${book}

*** Test Cases ***
User Can Browse Tips
    Add New Book Tip On Book Written By  Atomised  Michel Houellebecq
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Browse Tips Instructions
    Input Stop And Run Application

User Can See Added Tip In List
    Add New Book Tip On Book Written By  Dune  Frank Herbert
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Browse Tips Listing For Book  Dune
