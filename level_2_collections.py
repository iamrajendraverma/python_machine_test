"""Level 2 — Collections and data structures (Q5–Q8)."""

from dataset import patients


def group_names_by_condition(records):
    """Q5: Map each condition to the list of patient names with that condition."""
    pass


def unique_conditions(records):
    """Q6: Return unique conditions in order of first appearance."""
    pass


def merge_dicts(first, second):
    """Q7: Merge two dictionaries into a new one. Values in `second` win on conflict."""
    pass


def sort_by_glucose_desc(records):
    """Q8: Return records sorted by glucose, highest first. Original list is not changed."""
    pass


def run():
    print("Q5:", group_names_by_condition(patients))
    print("Q6:", unique_conditions(patients))
    patient_basic = {"id": 101, "name": "Raj"}
    patient_health = {"age": 35, "glucose": 180}
    print("Q7:", merge_dicts(patient_basic, patient_health))
    print("Q8:")
    for record in sort_by_glucose_desc(patients):
        print(f"  {record['name']:<6} -> {record['glucose']}")


if __name__ == "__main__":
    run()
