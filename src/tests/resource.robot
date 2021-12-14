*** Settings ***
Library  ../ReadingTipAppLibrary.py

*** Keywords ***
User Adds New Tip Successfully
    [Arguments]  ${tip title}
    Input Command  1
    Input Command  1
    Input Command  ${tip title}
    Input Stop Application
    Run Application
    ${success} =  Get Ui Message  AddNewTip  ADDITION_SUCCESS_TEXT
    Output Should Contain  ${success}

User Adds New Tip With Specific Type Successfully
    [Arguments]  ${tip title}  ${tip type}
    Input Command  1
    Input Command  ${tip type}
    Input Command  ${tip title}
    Input Stop Application
    Run Application
    ${success} =  Get Ui Message  AddNewTip  ADDITION_SUCCESS_TEXT
    Output Should Contain  ${success}

Input Stop And Run Application
    Input Stop Application
    Run Application

Select Add New Tip From Main Menu
    Input Command  1

Browse Tips From Main Menu
    Input Command  2

Input Title
    [Arguments]  ${title}
    Input Command  ${title}

Quit Browsing Tips
    Input command  l

Select Tip Type Book
    Input Command  1

Select Tip Type Video
    Input Command  2

Select Tip Type Blogpost
    Input Command  3

Select Tip Type Podcast
    Input Command  4

Select Quit Program From Main Menu
    Input Command  0

Input Book Name
    [Arguments]  ${name}
    Input Command  ${name}

Input Writer
    [Arguments]  ${name}
    Input Command  ${name}

Input ISBN
    [Arguments]  ${isbn}
    Input Command  ${isbn}

Input Description
    [Arguments]  ${desc}
    Input Command  ${desc}