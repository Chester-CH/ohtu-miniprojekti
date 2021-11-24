*** Settings ***
Resource  resource.robot

*** Test Cases ***
Program Starts And Prints Hello World
    Run Application
    Output Should Contain  Hello world!
