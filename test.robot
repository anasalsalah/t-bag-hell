*** Settings ***
Documentation   Suite description
...             Test cases for This is Hell.
Library     test/GameLibrary.py  "I am a useless parameter!"

*** Variables ***
# none for now #

*** Test Cases ***
Begin Game
    [Tags]    DEBUG
    Start game
    ${INTRO_MSG}=   Get Intro Msg
    Result should be    Introduction    ${INTRO_MSG}
Examine Bedroom
    [Tags]    DEBUG
    Start game
    If in room  bedroom
    ${ROOM_DESC}=   Get Room Desc
    Examine room
    Result should be    Bedroom Description    ${ROOM_DESC}

Enter Bad Command
    [Tags]    DEBUG
    Start game
    If in room  bedroom
    ${WRONG_MSG}=   Get Wrong Msg
    Is Wrong Command    Bla_This_Is_Wrong
    Result should be    Wrong Message    ${WRONG_MSG}

Go to Hallway
    [Tags]    DEBUG
    Start game
    If in room  bedroom
    Move    north
    If in room  hallway
    ${ROOM_DESC}=   Get Room Desc
    Result should be    Hallway Description    ${ROOM_DESC}

#Test title
#    [Tags]    DEBUG
#    Provided precondition
#    When action
#    Then check expectations
#*** Keywords ***
#Provided precondition
#    Setup system under test