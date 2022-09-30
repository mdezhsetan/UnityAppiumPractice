*** Settings ***
Library         OperatingSystem
Documentation   This is my first practice with robotframework!
...    I practice commands declared in the robot_commands.txt
Resource     ../Resources/resources.robot

*** Test Cases ***

TEST_CASE1
    [Tags]  TAG1
    LOG     output3: ${MESSAGE}
    LOG     output1: ${LIST}[1]
    LOG     output4: ${MULTILINE}
    LOG     output2: ${MANY.first}

TEST_CASE2
    [Tags]  TAG1    TAG2
    log     This is a log for Test Case 2

TEST_CASE3
    [Tags]  TAG2
    log     This is a log for Test Case 3

Test_Case4
        [Tags]  KeyWordTest
        log Usesrname and Password    ${VARIABLE1}  ${Variable2}