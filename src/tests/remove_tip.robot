*** Settings ***
Resource  resource.robot

*** Test Cases ***
Removing Tip Gives Right Message
    Select Add New Tip From Main Menu
    From Add Menu Add New Book Tip On Book Written By  Ilias  Homer
    Browse Tips From Main Menu
    Erase First Tip And Quit
    Select Quit Program From Main Menu
    Run Application
    Output Contains Successful Removal Message

Tip Is Not Visible After Removing
    Select Add New Tip From Main Menu
    From Add Menu Add New Book Tip On Book Written By  Ilias  Homer
    Browse Tips From Main Menu
    Erase First Tip And Quit
    Select Quit Program From Main Menu
    Run Application
    Program Doesnt Show Tip  Ilias

*** Keywords ***
Browse Tips From Main Menu
    Input Command  2

Erase First Tip And Quit
    Input command  p
    Input command  1
    Input command  l

Output Contains Successful Removal Message
    ${REMOVE TEXT} =  Get Ui Message  RemoveTip  REMOVAL_SUCCESS_TEXT
    Output Should Contain  ${REMOVE TEXT}