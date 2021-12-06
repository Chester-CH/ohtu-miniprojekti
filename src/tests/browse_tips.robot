*** Settings ***
Resource  resource.robot

*** Keywords ***
Browse Tips From Main Menu
    Input Command  2

*** Test Cases ***
User Can Browse Tips
    Input Command  1
    Input Command  testikirja
    Browse Tips From Main Menu
    Input Stop And Run Application
    ${browse greet} =  Get Ui Message  BrowseTips  GREET_TEXT
    Output Should Contain  ${browse greet}

User Can See Added Tip In List
    User Adds New Tip Successfully  Dune
    Browse Tips From Main Menu
    Input Stop And Run Application
    Output Should Contain  Dune
