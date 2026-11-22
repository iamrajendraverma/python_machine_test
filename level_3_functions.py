"""Level 3 — Functions and data processing (Q9–Q12)."""

import re

from dataset import patients


def filter_patients(patients, threshold):
    """Q9: Return new records whose glucose is greater than threshold.

    The input list and its dictionaries are not modified. An empty input
    returns an empty list.
    """
    pass


def normalize_text(text):
    """Q10: Strip leading/trailing whitespace and lowercase the text."""
    pass


def names_above_150(records):
    """Q11: Patient names with glucose > 150, using a list comprehension."""
    pass


def chunk_text(text, chunk_size):
    """Q12: Split text into chunks of at most `chunk_size` words.

    - Empty or whitespace-only text returns an empty list.
    - chunk_size must be a positive integer, otherwise ValueError is raised.
    """
    pass


DOCUMENT = """
Python is used in AI development.
Machine learning requires data preprocessing.
RAG combines retrieval with generation.
Embeddings convert text into vectors.
"""


def run():
    print("Q9:", [r["name"] for r in filter_patients(patients, 150)])
    print("Q10:", repr(normalize_text("  HIGH Glucose LEVEL Detected  ")))
    print("Q11:", names_above_150(patients))
    print("Q12:")
    for chunk in chunk_text(DOCUMENT, 3):
        print("  -", chunk)


if __name__ == "__main__":
    run()
