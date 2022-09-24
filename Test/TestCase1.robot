*** Settings ***
Library         OperatingSystem
Documentation   This is my first practice with robotframework!

*** Keywords ***

*** Variables ***

*** Test Cases ***

TEST_CASE1
    [Tags]  TAG1
    LOG     This is a log for Test Case 1

TEST_CASE2
    [Tags]  TAG1    TAG2
    log     This is a log for Test Case 2

TEST_CASE3
    [Tags]  TAG2
    log     This is a log for Test Case 3