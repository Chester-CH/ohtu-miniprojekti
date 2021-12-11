*** Settings ***
Resource  resource.robot

*** Keywords ***
Select To Add New Tip
    Input Command  1

Select Book To Tips Type
    Input Command  1

*** Test Cases ***
Program Starts And Prints The Greeting And The Menu
    Input Stop And Run Application
    ${greet} =  Get Ui Message  MainMenu  GREET_TEXT
    ${menu} =  Get Ui Message  MainMenu  MENU_TEXT
    Output Should Contain  ${greet}
    Output Should Contain  ${menu}

User Can Go To Add New Tips Menu
    Select To Add New Tip
    Select Book To Tips Type
    Input Command  Dune
    Input Stop And Run Application
    ${tips menu} =  Get Ui Message  AddNewTip  ADD_NEW_TIP_TEXT
    Output Should Contain  ${tips menu}

User Can Add New Tip From Tips Menu And Gets Success Confirmation
    User Adds New Tip Successfully  Dune

User Can Add New Tip And On Success The Program Will Remember The Addition
    User Adds New Tip Successfully  Dune
    Program Remembers Tip  Dune
