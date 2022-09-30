*** Keywords ***

Log a Username
    [Arguments]    ${USERNAME}
    log            ${USERNAME}

Log a Password
    [Arguments]    ${PASSWORD}
    log            ${PASSWORD}

log Usesrname and Password
    [Arguments]    ${Username}  ${Password}
    Log a Username    ${Username}
    Log a Password    ${Password}
#    log            Username:    ${Username},\n
#    ...            Passwoed:    ${Password}

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

${variable1}    my name
${Variable2}    my password

