*** Settings ***
Resource  resource.robot

*** Test Cases ***
User Can Browse Tips
    Input Command  1
    Input Command  testikirja
    Input Command  2
    Input Stop Application
    Run Application
    ${browse greet} =  Get Ui Message  BrowseTips  GREET_TEXT
    Output Should Contain  ${browse greet}