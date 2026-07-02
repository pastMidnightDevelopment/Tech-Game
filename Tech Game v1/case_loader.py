"""
File: case_loader.py
Version: 0.1
Purpose: Load Tech Game case files from JSON.
"""

# IMPORTS
import json
from pathlib import Path


# CONFIGURATION
CASE_DATA_DIR = Path(__file__).parent / "case_data"


# FUNCTIONS
def load_case(case_id):
    """
    Load a troubleshooting case by case_id.
    """

    case_path = CASE_DATA_DIR / f"{case_id}.json"

    if not case_path.exists():
        raise FileNotFoundError(f"Case file not found: {case_path}")

    with open(case_path, "r", encoding="utf-8") as file:
        case_data = json.load(file)

    return case_data


# PROGRAM START
if __name__ == "__main__":
    test_case = load_case("case_001")
    print(test_case["title"])
    print(test_case["work_order"])