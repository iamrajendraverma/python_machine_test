"""Level 4 — OOP, exceptions, and JSON (Q13–Q16)."""

import json


class Patient:
    """Patient record. Synthetic data only."""

    def __init__(self, id, name, age, glucose):
        self.id = id
        self.name = name
        self.age = age
        self.glucose = glucose



    def get_patient_details(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "glucose":self.glucose
        }


def divide(numerator, denominator):
    """Q14: Divide two numbers, returning (result, error_message)."""

    if not isinstance(numerator, (int, float)) or isinstance(numerator, bool):
        return None, "Numerator must be a number"

    if not isinstance(denominator, (int, float)) or isinstance(denominator, bool):
        return None, "Denominator must be a number"

    if denominator == 0:
        return None, "Cannot divide by zero"

    return numerator / denominator, None

def json_round_trip(data):
    """Q15: Dict -> JSON string (json.dumps) -> dict (json.loads)."""

    # Step 1: Convert dictionary into JSON string
    json_string = json.dumps(data)

    # Step 2: Convert JSON string back into dictionary
    result = json.loads(json_string)

    return result


def handle_api_response(response):
    """Q16: Return a predictable structure for a model/API-style response.

    Result: {"ok": bool, "patient_id": ..., "result": ..., "error": ...}
    """
    if not isinstance(response, dict):
        return {"ok": False, "patient_id": None, "result": None,
                "error": "response must be a dictionary"}

    if response.get("status") != "success":
        return {"ok": False, "patient_id": None, "result": None,
                "error": "API is not success"}

    data = response.get("data")
    if not isinstance(data, dict):
        return {"ok": False, "patient_id": None, "result": None,
                "error": "data is missing or invalid"}

    if "patient_id" not in data:
        return {"ok": False, "patient_id": None, "result": None,
                "error": "patient_id is missing"}

    if "result" not in data:
        return {"ok": False, "patient_id": None, "result": None,
                "error": "result is missing"}

    return {"ok": True, "patient_id": data["patient_id"],
            "result": data["result"], "error": None}


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
