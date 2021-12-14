*** Settings ***
Resource  resource.robot

*** Test Cases ***
Tip With Right Name And Type Book Is Saved
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Runotyttö etsii tähteään
    Go To Main Menu From Book Tip Writer Selection
    Select Quit Program From Main Menu
    Run Application
    Check Tips Title And Type Match  Runotyttö etsii tähteään  book

Tips Type Book Is Shown When Browsing Tips
    Select Add New Tip From Main Menu
    Select Tip Type Book
    Input Title  Marcovaldo
    Go To Main Menu From Book Tip Writer Selection
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Book Tip

Tip With Right Name And Type Video Is Saved
    Select Add New Tip From Main Menu
    Select Tip Type Video
    Input Title  Darude - Sandstorm
    Go To Main Menu From Video Tip Url Selection
    Select Quit Program From Main Menu
    Run Application
    Check Tips Title And Type Match  Darude - Sandstorm  video

Tips Video Type Is Shown When Browsing Tips
    Select Add New Tip From Main Menu
    Select Tip Type Video
    Input Title  Darude - Sandstorm
    Go To Main Menu From Video Tip Url Selection
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Video Tip

Tip With Right Name And Type Blogpost Is Saved
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  Omikron jäi haaviin nopeasti
    Go To Main Menu From Blogpost Tip Url Selection
    Select Quit Program From Main Menu
    Run Application
    Check Tips Title And Type Match  Omikron jäi haaviin nopeasti  blogpost

Tips Blogpost Type Is Shown When Browsing Tips
    Select Add New Tip From Main Menu
    Select Tip Type Blogpost
    Input Title  Omikron jäi haaviin nopeasti
    Go To Main Menu From Blogpost Tip Url Selection
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Blogpost Tip
    Output Should Contain  1: Omikron jäi haaviin nopeasti, blogiposti

Tip With Right Name And Type Podcast Is Saved
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  Vortex Traks Podcast 07 - Datawave
    Go To Main Menu From Podcast Tip Url Selection
    Select Quit Program From Main Menu
    Run Application
    Check Tips Title And Type Match  Vortex Traks Podcast 07 - Datawave  podcast

Tips Podcast Type Is Shown When Browsing Tips
    Select Add New Tip From Main Menu
    Select Tip Type Podcast
    Input Title  Vortex Traks Podcast 07 - Datawave
    Go To Main Menu From Podcast Tip Url Selection
    Browse Tips From Main Menu
    Quit Browsing Tips
    Select Quit Program From Main Menu
    Run Application
    Browse Output Contains The Created Podcast Tip


*** Keywords ***
Go To Main Menu From Book Tip Writer Selection
    Input Command  Montgomery LM
    Input Command  ${EMPTY}
    Input Command  ${EMPTY}
    Input Command  ${EMPTY}

Go To Main Menu From Video Tip Url Selection
    Input Command  https://www.youtube.com/watch?v=y6120QOlsfU
    Input Command  ${EMPTY}

Go To Main Menu From Blogpost Tip Url Selection
    Input Command  https://www.tiede.fi/blogit/kaiken-takana-loinen/omikron-jai-haaviin-nopeasti
    Input Command  Tuomas Aivelo
    Input Command  ${EMPTY}

Go To Main Menu From Podcast Tip Url Selection
    Input Command  https://soundcloud.com/vortex-traks/vtx-podcast-07-datawave
    Input Command  Datawave
    Input Command  Vortex Traks Podcast
    Input Command  ${EMPTY}

Browse Output Contains The Created Book Tip
    Output Should Contain  1: Marcovaldo, kirja

Browse Output Contains The Created Video Tip
    Output Should Contain  1: Darude - Sandstorm, video

Browse Output Contains The Created Blogpost Tip
    Output Should Contain  1: Omikron jäi haaviin nopeasti, blogiposti

Browse Output Contains The Created Podcast Tip
    Output Should Contain  1: Vortex Traks Podcast 07 - Datawave, podcast
