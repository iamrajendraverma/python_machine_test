"""Level 1 — Python fundamentals (Q1–Q4)."""



def remove_duplicates(items):
    """Q1: Return a new list with duplicates removed, preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result



def remove_duplicates_old_app(items):
    """Q1: Return a new list with duplicates removed, preserving order.
    dis-advantage of this solution is it does not maintain the order
    what if there is a 100000 records of visiter
    """
    no_duplicates =set(items)
    return list(no_duplicates)


def filter_high_glucose_names(records, threshold=150):
    """Q2: Return names of patients whose glucose is greater than threshold."""
    filter_records  = [item["name"] for item in records
    if item["glucose"]>=threshold
    ]
    return filter_records



def count_word_frequency(text):
    """Q3: Count how often each word appears in text."""
    word_count ={}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1

    return word_count



def find_max_min(values):
    """Q4: Return (maximum, minimum) without using max() or min()."""

    sorted_value  = sorted(values)
    smallest  = sorted_value[0]
    largest  = sorted_value[len(sorted_value)-1]
    return {
        "min":smallest,
        "max":largest
    }
