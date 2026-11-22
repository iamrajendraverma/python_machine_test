"""Level 5 — NumPy, Pandas, and AI/ML logic (Q17–Q20)."""

import re

import numpy as np
import pandas as pd

from dataset import patients


def numpy_operations(glucose):
    """Q17: Basic NumPy statistics and filtering."""
    pass


def pandas_operations(records):
    """Q18: DataFrame preview, filter, groupby, and average glucose per condition."""
    pass


def cosine_similarity(a, b):
    """Q19: dot(a, b) / (|a| * |b|). Returns 0.0 if either vector is zero-length."""
    pass


def tokenize(text):
    pass


def retrieve_top_documents(query, documents, top_k=2):
    """Q20: Rank documents by word overlap with the query.

    - Ties keep the original document order.
    - Documents with zero overlap are excluded, so a query with no matching
      words returns an empty list.
    """
    pass


def run():
    glucose = np.array([180, 110, 210, 95, 160])
    stats = numpy_operations(glucose)
    print("Q17 mean:", stats["mean"])
    print("Q17 max:", stats["max"], "min:", stats["min"])
    print("Q17 >150:", stats["above_150"])
    print("Q17 std:", round(stats["std"], 2))

    result = pandas_operations(patients)
    print("Q18 head:\n", result["head"], sep="")
    print("Q18 >150:\n", result["above_150"], sep="")
    print("Q18 avg by condition:\n", result["avg_glucose_by_condition"], sep="")

    query = np.array([1, 2, 3])
    doc1 = np.array([1, 2, 3])
    doc2 = np.array([3, 2, 1])
    sim1 = cosine_similarity(query, doc1)
    sim2 = cosine_similarity(query, doc2)
    print(f"Q19 doc1 similarity: {sim1:.4f}")
    print(f"Q19 doc2 similarity: {sim2:.4f}")
    print("Q19 higher:", "doc1" if sim1 > sim2 else "doc2" if sim2 > sim1 else "tie")

    documents = [
        {"id": 1, "text": "Diabetes causes high glucose"},
        {"id": 2, "text": "Python supports machine learning"},
        {"id": 3, "text": "High glucose is related to diabetes"},
    ]
    print("Q20:", retrieve_top_documents("glucose diabetes", documents))
    print("Q20 no match:", retrieve_top_documents("banana", documents))


if __name__ == "__main__":
    run()
