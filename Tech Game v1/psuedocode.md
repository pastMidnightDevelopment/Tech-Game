TECH GAME V1 PSEUDOCODE

START PROGRAM

LOAD case_001

DISPLAY game title
DISPLAY case title
DISPLAY work order

REPEAT until player exits or finishes case:

    DISPLAY menu options:
        1. Show components
        2. Inspect component
        3. Test component
        4. Show evidence log
        5. Make final diagnosis
        6. Exit

    GET player choice

    IF choice is Show Components:
        DISPLAY each component name and id

    IF choice is Inspect Component:
        ASK player for component id
        FIND matching component
        DISPLAY inspect result
        ADD result to evidence log

    IF choice is Test Component:
        ASK player for component id
        FIND matching component
        DISPLAY test result
        ADD result to evidence log

    IF choice is Show Evidence Log:
        DISPLAY all saved evidence

    IF choice is Make Final Diagnosis:
        DISPLAY possible answers
        ASK player to choose an answer
        COMPARE selected answer to correct answer

        IF answer is correct:
            DISPLAY success message
        ELSE:
            DISPLAY failure message

        ASK player if they want to play again

        IF yes:
            RESTART game
        ELSE:
            DISPLAY goodbye message

        END current case

    IF choice is Exit:
        DISPLAY exit message
        END PROGRAM

END PROGRAM