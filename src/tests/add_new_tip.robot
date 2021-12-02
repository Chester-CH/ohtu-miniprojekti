*** Settings ***
Resource  resource.robot

*** Keywords ***
User Adds New Tip Successfully
    [Arguments]  ${tip title}
    Input Command  1
    Input Command  ${tip title}
    Input Stop Application
    Run Application
    ${success} =  Get Ui Message  AddNewTip  ADDITION_SUCCESS_TEXT
    Output Should Contain  ${success}

*** Test Cases ***
Program Starts And Prints The Greeting And The Menu
    Input Stop Application
    Run Application
    ${greet} =  Get Ui Message  MainMenu  GREET_TEXT
    ${menu} =  Get Ui Message  MainMenu  MENU_TEXT
    Output Should Contain  ${greet}
    Output Should Contain  ${menu}

User Can Go To Add New Tips Menu
    Input Command  1
    Input Command  testi
    Input Stop Application
    Run Application
    ${tips menu} =  Get Ui Message  AddNewTip  ADD_NEW_TIP_TEXT
    Output Should Contain  ${tips menu}

User Can Add New Tip From Tips Menu And Gets Success Confirmation
    User Adds New Tip Successfully  testi

User Can Add New Tip And On Success The Program Will Remember The Addition
    User Adds New Tip Successfully  testi
    Program Remembers Tip  testi
