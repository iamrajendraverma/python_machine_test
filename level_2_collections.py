"""Level 2 — Collections and data structures (Q5–Q8)."""

from dataset import patients


def group_names_by_condition(records):
    """Q5: Map each condition to the list of patient names with that condition."""
    diabeties =[item["name"] for item in records
    if item["condition"] =="Diabetes"
    ]
    bp =[item["name"] for item in records
    if item["condition"] =="BP"
    ]
    none_list  =[item["name"] for item in records
    if item["condition"] !="None"
    ]
    return {
    "Diabetes": diabeties,
    "BP": bp,
    "None": none_list
}

    pass


def unique_conditions(records):
    """Q6: Return unique conditions in order of first appearance."""
    unique_condition = []
    seen = set()
    for item in records:
        condition = item["condition"]
        if condition not in seen:
            seen.add(condition)
            unique_condition.append(condition)
    return unique_condition



def merge_dicts(first, second):
    """Q7: Merge two dictionaries into a new one. Values in `second` win on conflict."""
    result = first | second
    return result


def sort_by_glucose_desc(records):
    """Q8: Return records sorted by glucose, highest first. Original list is not changed."""
    return sorted(records,key=lambda x: x["glucose"],reverse=True)



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
