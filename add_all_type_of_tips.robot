*** Settings ***
Resource  resource.robot

***Keywords***
Browse Tips From Main Menu
    Input Command  2

Quit Browsing Tips
    Input Command  l

Browse Output Contains The Created Book Tip
    Output Should Contain  1: kirja, kirja\nKirjailija: kirjailija\nISBN: 1234\nKuvaus: tyhja

Browse Output Contains The Created Video Tip
    Output Should Contain  1: video, video\nURL: www.\nKuvaus: tyhja

Browse Output Contains The Created Blogpost Tip
    Output Should Contain  1: blogi, blogiposti\nTekijä: joku\nURL: www.\nKuvaus: tyhja

Browse Output Contains The Created Podcast Tip
    Output Should Contain  1: podi, podcast\nNimi: ep1\nTekijä: juontaja\nURL: www.\nKuvaus: tyhja

*** Test Cases ***
Book Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Book Name  kirja
    Input Writer  kirjailija
    Input ISBN  1234
    Input Description  tyhja  
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Book Tip

Video Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Video
    Input Title  video
    Input URL  www.
    Input Description  tyhja  
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Video Tip

Blogpost Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  blogi
    Input URL  www.
    Input Writer  joku
    Input Description  tyhja  
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Blogpost Tip

PodCast Tip Is Saved With The Right Details
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  podi
    Input URL  www.
    Input Writer  juontaja
    Input Episode Name  ep1
    Input Description  tyhja  
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Podcast Tip