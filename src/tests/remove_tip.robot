*** Settings ***
Resource  resource.robot

*** Test Cases ***
Removing Tip Gives Right Message
    User Adds New Tip Successfully  Ilias
    Browse Tips From Main Menu
    Erase First Tip And Quit
    Input Stop And Run Application
    ${REMOVE TEXT} =  Get Ui Message  RemoveTip  REMOVAL_SUCCESS_TEXT
    Output Should Contain  ${REMOVE TEXT}

Tip Is Not Visible After Removing
    User Adds New Tip Successfully  Ilias
    Browse Tips From Main Menu
    Erase First Tip And Quit
    Input Stop And Run Application
    Program Doesnt Show Tip  Ilias

*** Keywords ***
Browse Tips From Main Menu
    Input Command  2

Erase First Tip And Quit
    Input command  p
    Input command  1
    Input command  l
