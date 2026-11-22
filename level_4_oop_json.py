"""Level 4 — OOP, exceptions, and JSON (Q13–Q16)."""

import json


class Patient:
    """Patient record. Synthetic data only."""

    def __init__(self, id, name, age, glucose):
        pass

    def get_patient_details(self):
        pass


def divide(numerator, denominator):
    """Q14: Divide two numbers, returning (result, error_message).

    Exactly one of the two is None. Errors are reported, not hidden.
    """
    pass


def json_round_trip(data):
    """Q15: Dict -> JSON string (json.dumps) -> dict (json.loads)."""
    pass


def handle_api_response(response):
    """Q16: Return a predictable structure for a model/API-style response.

    Result: {"ok": bool, "patient_id": ..., "result": ..., "error": ...}
    """
    pass


def run():
    raj = Patient(101, "Raj", 35, 180)
    neha = Patient(103, "Neha", 29, 210)
    print("Q13:", raj.get_patient_details())
    print("Q13:", neha.get_patient_details())

    print("Q14:", divide(10, 2))
    print("Q14:", divide(10, 0))
    print("Q14:", divide("10", 2))

    data = {"patient_id": 101, "result": "Report generated"}
    text, restored = json_round_trip(data)
    print("Q15 dumps:", text)
    print("Q15 loads:", restored)

    success = {"status": "success",
               "data": {"patient_id": 101, "result": "Report generated"}}
    failure = {"status": "error", "data": None}
    missing = {"status": "success"}
    print("Q16 success:", handle_api_response(success))
    print("Q16 failure:", handle_api_response(failure))
    print("Q16 missing:", handle_api_response(missing))


if __name__ == "__main__":
    run()
