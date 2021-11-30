*** Settings ***
Resource  resource.robot
Test Setup  Setup Test Database

*** Test Cases ***
Program Starts And Prints The Greeting And The Menu
    Input Stop Application
    Run Application
    ${greet} =  Get Ui Message  GREET_TEXT
    ${menu} =  Get Ui Message  MENU_TEXT
    Output Should Contain  ${greet}
    Output Should Contain  ${menu}
