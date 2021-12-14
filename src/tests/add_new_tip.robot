*** Settings ***
Resource  resource.robot

*** Keywords ***

Output Contains Main Menu Instructions
    ${greet} =  Get Ui Message  MainMenu  GREET_TEXT
    ${menu} =  Get Ui Message  MainMenu  MENU_TEXT
    Output Should Contain  ${greet}
    Output Should Contain  ${menu}

Output Contains Tip Type Question
    ${tips menu} =  Get Ui Message  AddNewTip  TIPS_TYPES_TEXT
    Output Should Contain  ${tips menu}

Go To Main Menu From Tip Type Selection
    Input Command  ${EMPTY}

Output Contains Tip Creation Success
    ${tips menu} =  Get Ui Message  AddNewTip  ADDITION_SUCCESS_TEXT
    Output Should Contain  ${tips menu}

*** Test Cases ***
Program Starts And Prints The Greeting And The Menu
    Select Quit Program From Main Menu
    Run Application
    Output Contains Main Menu Instructions
    
User Can Go To Add New Tips Menu
    Select Add New Tip From Main Menu
    Go To Main Menu From Tip Type Selection
    Select Quit Program From Main Menu
    Run Application
    Output Contains Tip Type Question

User Can Add New Tip From Tips Menu And Gets Success Confirmation
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  Dune
    Input Writer  Frank Herbert
    Input ISBN  0441172717
    Input Description  A scifi book
    Select Quit Program From Main Menu
    Run Application
    Output Contains Tip Creation Success

User Can Add New Tip And On Success The Program Will Remember The Addition
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  Dune
    Input Writer  Frank Herbert
    Input ISBN  0441172717
    Input Description  A scifi book
    Select Quit Program From Main Menu
    Run Application
    Program Remembers Tip  Dune
