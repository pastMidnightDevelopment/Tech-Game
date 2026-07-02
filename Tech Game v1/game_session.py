"""
File: game_session.py
Version: 0.1
Purpose: Manage one simple Tech Game troubleshooting session.
"""

# IMPORTS
from case_loader import load_case


# STATE
current_case = None
evidence_log = []


# FUNCTIONS
def start_case(case_id):
    """
    Start a new case and reset evidence.
    """

    global current_case
    global evidence_log

    current_case = load_case(case_id)
    evidence_log = []

    return current_case


def perform_action(component_id, action_name):
    """
    Perform an investigation action on a component.
    """

    for component in current_case["components"]:
        if component["id"] == component_id:
            if action_name in component["actions"]:
                result = component["actions"][action_name]
                evidence_log.append(result)
                return result

    return "That action is not available."


def check_answer(selected_answer):
    """
    Check the player's final diagnosis.
    """

    if selected_answer == current_case["correct_answer"]:
        return current_case["success_message"]

    return current_case["failure_message"]


def get_evidence_log():
    """
    Return all evidence found so far.
    """

    return evidence_log


# PROGRAM START
if __name__ == "__main__":
    start_case("case_001")

    print(current_case["work_order"])
    print(perform_action("start_button", "inspect"))
    print(perform_action("fuse", "test"))
    print(check_answer("Blown control fuse"))