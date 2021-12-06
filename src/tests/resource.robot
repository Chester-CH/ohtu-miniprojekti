*** Settings ***
Library  ../ReadingTipAppLibrary.py

*** Keywords ***
User Adds New Tip Successfully
    [Arguments]  ${tip title}
    Input Command  1
    Input Command  ${tip title}
    Input Stop Application
    Run Application
    ${success} =  Get Ui Message  AddNewTip  ADDITION_SUCCESS_TEXT
    Output Should Contain  ${success}

Input Stop And Run Application
    Input Stop Application
    Run Application
