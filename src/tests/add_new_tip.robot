*** Settings ***
Resource  resource.robot

*** Keywords ***


*** Test Cases ***
Program Starts And Prints The Greeting And The Menu
    Input Stop And Run Application
    ${greet} =  Get Ui Message  MainMenu  GREET_TEXT
    ${menu} =  Get Ui Message  MainMenu  MENU_TEXT
    Output Should Contain  ${greet}
    Output Should Contain  ${menu}

User Can Go To Add New Tips Menu
    Input Command  1
    Input Command  Dune
    Input Stop And Run Application
    ${tips menu} =  Get Ui Message  AddNewTip  ADD_NEW_TIP_TEXT
    Output Should Contain  ${tips menu}

User Can Add New Tip From Tips Menu And Gets Success Confirmation
    User Adds New Tip Successfully  Dune

User Can Add New Tip And On Success The Program Will Remember The Addition
    User Adds New Tip Successfully  Dune
    Program Remembers Tip  Dune
