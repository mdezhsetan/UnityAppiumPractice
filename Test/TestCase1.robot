*** Settings ***
Library         OperatingSystem
Documentation   This is my first practice with robotframework!
...    I practice commands declared in the robot_commands.txt

*** Keywords ***

*** Variables ***

@{LIST}         one     two 	three

${MULTILINE}    SEPARATOR=\n
...             First line.
...             Second line.
...             Third line.
${MESSAGE}      Hello, world!
&{MANY}         first=1     second=${2}         ${3}=third
&{EVEN MORE}    &{MANY}       first=override      empty=
...             =empty        key\=here=value

*** Test Cases ***

TEST_CASE1
    [Tags]  TAG1
#    LOG     This is a log for Test Case 1
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