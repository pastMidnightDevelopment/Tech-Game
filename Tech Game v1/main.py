"""
File: main.py
Version: 0.1
Purpose: Run a simple terminal prototype for Tech Game.
"""

# IMPORTS
from game_session import start_case
from game_session import perform_action
from game_session import check_answer
from game_session import get_evidence_log


# FUNCTIONS
def show_components(case_data):
    print("\nComponents:")
    for component in case_data["components"]:
        print(f"- {component['id']}: {component['name']}")


def show_answers(case_data):
    print("\nPossible Diagnoses:")
    for index, answer in enumerate(case_data["answers"], start=1):
        print(f"{index}. {answer}")


def run_game():
    case_data = start_case("case_001")

    print("\n=== TECH GAME V1 ===")
    print(f"\nCase: {case_data['title']}")
    print(case_data["work_order"])

    while True:
        print("\nOptions:")
        print("1. Show components")
        print("2. Inspect component")
        print("3. Test component")
        print("4. Show evidence log")
        print("5. Make final diagnosis")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_components(case_data)

        elif choice == "2":
            component_id = input("Enter component id: ")
            print(perform_action(component_id, "inspect"))

        elif choice == "3":
            component_id = input("Enter component id: ")
            print(perform_action(component_id, "test"))

        elif choice == "4":
            print("\nEvidence Log:")
            for evidence in get_evidence_log():
                print(f"- {evidence}")

        elif choice == "5":
            show_answers(case_data)
            answer_number = input("Choose diagnosis number: ")

            if answer_number.isdigit():
                answer_index = int(answer_number) - 1

                if 0 <= answer_index < len(case_data["answers"]):
                    selected_answer = case_data["answers"][answer_index]
                    print(check_answer(selected_answer))
                    play_again = input("\nPlay again? y/n: ").lower()
                    if play_again == "y":
                        run_game()
                    else:
                        print("Thanks for playing.")
                    break

            print("Invalid diagnosis choice.")

        elif choice == "6":
            print("Exiting game.")
            break

        else:
            print("Invalid option.")


# PROGRAM START
if __name__ == "__main__":
    run_game()