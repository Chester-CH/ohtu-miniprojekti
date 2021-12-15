*** Settings ***
Resource  resource.robot

***Keywords***
Browse Tips From Main Menu
    Input Command  2

Quit Browsing Tips
    Input Command  l

Browse Output Contains The Created Book Tip
    Output Should Contain  1: Clean Code, kirja\nKirjailija: Robert C. Martin\nISBN: 9780132350884\nKuvaus: Handbook of Agile

Browse Output Contains The Created Video Tip
    Output Should Contain  1: Helsingin yliopiston Ohjelmistotuotanto, vierailuluento: Digital Product Design (Nitor), video\nURL: https://www.youtube.com/watch?v=dhDusAPpjos&t=816s&ab_channel=moocfi\nKuvaus: Niko Laitinen Nitor:sta pitää vierailuluennon Helsingin yliopiston Ohjelmistotuotanto kurssilla

Browse Output Contains The Created Blogpost Tip
    Output Should Contain  1: A quick maintenance break on September the 9th from 3 pm to 5 pm, blogiposti\nTekijä: Petteri Hemmilä\nURL: https://blogs.helsinki.fi/a-quick-maintenance-break-on-september-the-9th-from-3-pm-to-5-pm/\nKuvaus: Uni Helsinki blogging platform

Browse Output Contains The Created Podcast Tip
    Output Should Contain  1: All Female Panel, podcast\nNimi: Jakso 1: Jotain ämmiä äänessä\nTekijä: Elina Ylä-Mononen\nURL: https://areena.yle.fi/audio/1-50123230\nKuvaus: All Female Panel on feministisen huumorin sysimusta pesäke

Output Contains Warning Text
    ${tips menu} =  Get Ui Message  AddNewTip  FIELD_EMPTY_TEXT
    Output Should Contain  ${tips menu}

*** Test Cases ***
Book Name Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  ${EMPTY}
    Input Book Name  Dune
    Input Writer  Frank Herbert
    Input ISBN  0441172717
    Input Description  A scifi book
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

Book Writer Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  Dune
    Input Writer  ${EMPTY}
    Input Writer  Frank Herbert
    Input ISBN  0441172717
    Input Description  A scifi book
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

Video Name Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  ${EMPTY}
    Input Title  Helsingin yliopiston Ohjelmistotuotanto, vierailuluento: Digital Product Design (Nitor)
    Input URL  https://www.youtube.com/watch?v=dhDusAPpjos&t=816s&ab_channel=moocfi
    Input Description  Niko Laitinen Nitor:sta pitää vierailuluennon Helsingin yliopiston Ohjelmistotuotanto kurssilla 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

Video Link Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Helsingin yliopiston Ohjelmistotuotanto, vierailuluento: Digital Product Design (Nitor)
    Input URL  ${EMPTY}
    Input URL  https://www.youtube.com/watch?v=dhDusAPpjos&t=816s&ab_channel=moocfi
    Input Description  Niko Laitinen Nitor:sta pitää vierailuluennon Helsingin yliopiston Ohjelmistotuotanto kurssilla 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

Blogpost Title Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  ${EMPTY}
    Input Title  A quick maintenance break on September the 9th from 3 pm to 5 pm
    Input URL  https://blogs.helsinki.fi/a-quick-maintenance-break-on-september-the-9th-from-3-pm-to-5-pm/
    Input Writer  Petteri Hemmilä
    Input Description  Uni Helsinki blogging platform 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

Blogpost Link Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  A quick maintenance break on September the 9th from 3 pm to 5 pm
    Input URL  ${EMPTY}
    Input URL  https://blogs.helsinki.fi/a-quick-maintenance-break-on-september-the-9th-from-3-pm-to-5-pm/
    Input Writer  Petteri Hemmilä
    Input Description  Uni Helsinki blogging platform 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

Blogpost Writer Cannot Be Empty
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  A quick maintenance break on September the 9th from 3 pm to 5 pm
    Input URL  https://blogs.helsinki.fi/a-quick-maintenance-break-on-september-the-9th-from-3-pm-to-5-pm/
    Input Writer  ${EMPTY}
    Input Writer  Petteri Hemmilä
    Input Description  Uni Helsinki blogging platform 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text

PodCast Title Cannot Be Empty 
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  ${EMPTY}
    Input Title  All Female Panel
    Input URL  https://areena.yle.fi/audio/1-50123230
    Input Writer  Elina Ylä-Mononen
    Input Episode Name  Jakso 1: Jotain ämmiä äänessä
    Input Description  All Female Panel on feministisen huumorin sysimusta pesäke 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text 

PodCast Link Cannot Be Empty 
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  All Female Panel
    Input URL  ${EMPTY}
    Input URL  https://areena.yle.fi/audio/1-50123230
    Input Writer  Elina Ylä-Mononen
    Input Episode Name  Jakso 1: Jotain ämmiä äänessä
    Input Description  All Female Panel on feministisen huumorin sysimusta pesäke 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text    

PodCast Writer Cannot Be Empty 
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  All Female Panel
    Input URL  https://areena.yle.fi/audio/1-50123230
    Input Writer  ${EMPTY}
    Input Writer  Elina Ylä-Mononen
    Input Episode Name  Jakso 1: Jotain ämmiä äänessä
    Input Description  All Female Panel on feministisen huumorin sysimusta pesäke 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Output Contains Warning Text


Book Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  Clean Code
    Input Writer  Robert C. Martin
    Input ISBN  9780132350884
    Input Description  Handbook of Agile 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Book Tip



Video Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Video
    Input Title  Helsingin yliopiston Ohjelmistotuotanto, vierailuluento: Digital Product Design (Nitor)
    Input URL  https://www.youtube.com/watch?v=dhDusAPpjos&t=816s&ab_channel=moocfi
    Input Description  Niko Laitinen Nitor:sta pitää vierailuluennon Helsingin yliopiston Ohjelmistotuotanto kurssilla 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Video Tip

Blogpost Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  A quick maintenance break on September the 9th from 3 pm to 5 pm
    Input URL  https://blogs.helsinki.fi/a-quick-maintenance-break-on-september-the-9th-from-3-pm-to-5-pm/
    Input Writer  Petteri Hemmilä
    Input Description  Uni Helsinki blogging platform 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Blogpost Tip

PodCast Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  All Female Panel
    Input URL  https://areena.yle.fi/audio/1-50123230
    Input Writer  Elina Ylä-Mononen
    Input Episode Name  Jakso 1: Jotain ämmiä äänessä
    Input Description  All Female Panel on feministisen huumorin sysimusta pesäke 
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Podcast Tip