# Python Machine Test for AI/ML Developers

A practical, hands-on Python assessment designed to strengthen the fundamentals used in **AI, Machine Learning, RAG, and Agentic AI development**.

The exercises progress from basic Python collections to data processing, OOP, NumPy, Pandas, cosine similarity, and a simplified document-retrieval task. They use synthetic healthcare data for practice only.

## Learning objectives

By completing this machine test, you will practise how to:

- Process lists, strings, dictionaries, and sets.
- Transform and filter JSON-like records.
- Write reusable functions and readable Python code.
- Handle exceptions and work with JSON.
- Build simple text preprocessing and document chunking utilities.
- Use NumPy and Pandas for numerical and tabular data.
- Understand cosine similarity and basic retrieval logic used in RAG systems.

## Test overview

| Level | Focus | Questions | Marks |
|---|---|---:|---:|
| 1 | Python fundamentals | 1–4 | 20 |
| 2 | Collections and data structures | 5–8 | 20 |
| 3 | Functions and data processing | 9–12 | 20 |
| 4 | OOP, exceptions, and JSON | 13–16 | 20 |
| 5 | NumPy, Pandas, and AI/ML logic | 17–20 | 20 |
| **Total** | | **20** | **100** |

**Suggested duration:** 120 minutes  
**Difficulty:** Beginner to intermediate, progressing to intermediate/advanced  
**Language:** Python 3

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/iamrajendraverma/python_machine_test.git
cd python_machine_test
```

### 2. Create and activate a virtual environment (recommended)

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install optional data-science dependencies

Questions 1–16 can be completed with Python's standard library. Install NumPy and Pandas for Questions 17–18:

```bash
python -m pip install numpy pandas
```

### 4. Run your code

Use `main.py` as an entry point, or create separate files for each level:

```bash
python main.py
```

You can organise your solutions like this:

```text
python_machine_test/
├── README.md
├── main.py
├── level_1_fundamentals.py
├── level_2_collections.py
├── level_3_functions.py
├── level_4_oop_json.py
└── level_5_ai_ml.py
```

These solution files are suggestions; create them as you work through the test.

---

## Synthetic dataset

Use the following dataset for Questions 1–2 and 5–8, and wherever relevant in later exercises.

```python
patients = [
    {
        "id": 101,
        "name": "Raj",
        "age": 35,
        "condition": "Diabetes",
        "glucose": 180,
        "report": "High glucose level detected"
    },
    {
        "id": 102,
        "name": "Amit",
        "age": 42,
        "condition": "BP",
        "glucose": 110,
        "report": "Normal glucose level"
    },
    {
        "id": 103,
        "name": "Neha",
        "age": 29,
        "condition": "Diabetes",
        "glucose": 210,
        "report": "Critical glucose level detected"
    },
    {
        "id": 104,
        "name": "Priya",
        "age": 31,
        "condition": "None",
        "glucose": 95,
        "report": "Normal glucose level"
    },
    {
        "id": 105,
        "name": "Vikas",
        "age": 50,
        "condition": "Diabetes",
        "glucose": 160,
        "report": "Elevated glucose level"
    }
]
```

> **Data note:** This is entirely synthetic educational data. It is not real patient information and must not be used for diagnosis, treatment, or clinical decisions.

# Machine test

Try to solve each question before looking up a solution. Add test cases for empty input, missing values, unexpected types, and boundary conditions where they make sense.

## Level 1 — Python fundamentals (20 marks)

### Q1. Remove duplicates while preserving order (5 marks)

Given:

```python
data = [1, 2, 2, 3, 4, 3, 5, 1]
```

Write code to remove duplicates while preserving the original order.

Expected output:

```python
[1, 2, 3, 4, 5]
```

**Concepts:** Lists, loops, sets, conditions.

### Q2. Filter patient records (5 marks)

Find all patients whose `glucose` value is greater than 150.

Expected patient names: `Raj`, `Neha`, `Vikas`.

**Concepts:** Loops, conditions, dictionaries.

### Q3. Count word frequency (5 marks)

Given:

```python
text = "AI ML AI Python ML AI"
```

Count how often each word appears.

Expected output:

```python
{
    "AI": 3,
    "ML": 2,
    "Python": 1
}
```

**Concepts:** Strings, `split()`, dictionaries.

### Q4. Find maximum and minimum without built-ins (5 marks)

Given:

```python
scores = [85, 92, 45, 76, 98, 60]
```

Find the maximum and minimum values without using `max()` or `min()`.

**Concepts:** Loops, comparisons, variable updates.

## Level 2 — Collections and data structures (20 marks)

### Q5. Group patients by condition (5 marks)

Create a dictionary that groups patient names by their `condition`.

Expected structure:

```python
{
    "Diabetes": ["Raj", "Neha", "Vikas"],
    "BP": ["Amit"],
    "None": ["Priya"]
}
```

**Concepts:** Dictionaries, loops, `setdefault()`.

### Q6. Extract unique conditions (5 marks)

Extract the unique patient conditions.

Expected values: `Diabetes`, `BP`, and `None` (the string in the dataset).

Return them as a list. The order should follow their first appearance in the dataset.

**Concepts:** Sets, lists, membership checks.

### Q7. Merge two dictionaries (5 marks)

Given:

```python
patient_basic = {
    "id": 101,
    "name": "Raj"
}

patient_health = {
    "age": 35,
    "glucose": 180
}
```

Merge both dictionaries into one dictionary.

**Concepts:** Dictionary unpacking, `update()`, dictionary operators.

### Q8. Sort patients by glucose (5 marks)

Sort the patient records by glucose in descending order.

Expected order:

```text
Neha  -> 210
Raj   -> 180
Vikas -> 160
Amit  -> 110
Priya -> 95
```

**Concepts:** `sorted()`, `key`, lambda functions.

## Level 3 — Functions and data processing (20 marks)

### Q9. Create a reusable filtering function (5 marks)

Implement:

```python
def filter_patients(patients, threshold):
    pass
```

Requirements:

- Accept a list of patient records and a glucose threshold.
- Return records whose glucose is greater than the threshold.
- Do not modify the original dataset.
- Consider what should happen if the input list is empty.

**AI/ML connection:** Reusable filtering functions are common in data-cleaning and preprocessing pipelines.

### Q10. Normalize text (5 marks)

Implement:

```python
def normalize_text(text):
    pass
```

Input:

```python
"  HIGH Glucose LEVEL Detected  "
```

Expected output:

```text
high glucose level detected
```

The function should remove leading/trailing whitespace and convert text to lowercase.

**AI/ML connection:** Text normalization is a common preprocessing step before indexing or embedding generation. Real pipelines may require additional, task-specific normalization.

### Q11. Use list comprehension (5 marks)

Extract patient names whose glucose value is greater than 150 using a **list comprehension**.

Expected output:

```python
["Raj", "Neha", "Vikas"]
```

**Concepts:** List comprehensions, conditions, dictionary access.

### Q12. Create a document chunking function (5 marks)

Implement:

```python
def chunk_text(text, chunk_size):
    pass
```

Use this document:

```python
document = """
Python is used in AI development.
Machine learning requires data preprocessing.
RAG combines retrieval with generation.
Embeddings convert text into vectors.
"""
```

Split the text into chunks containing at most three words each. Return a list of strings. Decide how your function handles empty text and invalid chunk sizes.

**AI/ML connection:** Chunking divides long documents into smaller pieces before embedding and indexing in a RAG pipeline. This exercise uses fixed word counts; production chunking may also respect headings, paragraphs, token limits, and semantic boundaries.

## Level 4 — OOP, exceptions, and JSON (20 marks)

### Q13. Create a Patient class (5 marks)

Create a `Patient` class with:

- `id`
- `name`
- `age`
- `glucose`

Add a method named `get_patient_details()` that returns the patient's information.

Create at least two objects and call the method on each.

**Concepts:** Classes, objects, constructors, instance methods.

### Q14. Exception handling (5 marks)

Write a function that accepts two values and divides the first by the second.

Handle:

- Division by zero.
- Invalid input types or values.
- Other exceptions only where appropriate.

Return a clear result or error message. Avoid hiding errors with a broad, silent `except`.

**AI/ML connection:** Robust data and API pipelines need predictable error handling.

### Q15. JSON processing (5 marks)

Use Python's `json` module to:

1. Convert a Python dictionary into a JSON string.
2. Convert that JSON string back into a Python dictionary.
3. Print the result.

Explain the difference between:

- `json.dumps()`: Python object to JSON-formatted string.
- `json.loads()`: JSON-formatted string to Python object.

**AI/ML connection:** JSON is commonly used for LLM tool arguments, API requests, structured outputs, and configuration.

### Q16. Create an API response handler (5 marks)

Given:

```python
response = {
    "status": "success",
    "data": {
        "patient_id": 101,
        "result": "Report generated"
    }
}
```

Write a function that:

- Checks whether the status is successful.
- Extracts the data.
- Handles missing or unexpected keys.
- Returns a predictable structured result.

Also test a response with a failure status and one with missing data.

**AI/ML connection:** AI applications frequently consume responses from model endpoints and external services.

## Level 5 — NumPy, Pandas, and AI/ML logic (20 marks)

Install dependencies before attempting Questions 17–18:

```bash
python -m pip install numpy pandas
```

### Q17. NumPy operations (5 marks)

Given:

```python
import numpy as np

glucose = np.array([180, 110, 210, 95, 160])
```

Perform these operations:

1. Calculate the mean.
2. Find the maximum.
3. Find the minimum.
4. Filter values greater than 150.
5. Calculate the standard deviation.

**Concepts:** NumPy arrays, aggregation, boolean indexing.

### Q18. Pandas DataFrame (5 marks)

Convert the synthetic `patients` dataset into a Pandas DataFrame.

Then:

1. Display the first three records.
2. Filter records where glucose is greater than 150.
3. Group records by condition.
4. Calculate average glucose for each condition.

**Concepts:** DataFrames, filtering, `groupby()`, aggregation.

### Q19. Calculate cosine similarity (5 marks)

Cosine similarity is used to compare vectors, including text embeddings in retrieval systems.

Given:

```python
import numpy as np

query = np.array([1, 2, 3])

doc1 = np.array([1, 2, 3])
doc2 = np.array([3, 2, 1])
```

Implement a function that calculates:

```text
cosine_similarity(A, B) =
    dot(A, B) / (norm(A) * norm(B))
```

Requirements:

- Return a similarity score.
- Handle zero-length vectors safely (a zero vector has no defined cosine direction).
- Compare the query with both documents.
- Identify which document has the higher similarity.

**AI/ML connection:** Embedding models represent text as vectors. Vector databases use similarity measures to retrieve relevant chunks.

### Q20. Build a mini document-retrieval function (5 marks)

Given:

```python
documents = [
    {"id": 1, "text": "Diabetes causes high glucose"},
    {"id": 2, "text": "Python supports machine learning"},
    {"id": 3, "text": "High glucose is related to diabetes"}
]
```

Build a simple retrieval function that:

1. Accepts a user query.
2. Tokenizes the query and document text.
3. Calculates a word-overlap score for each document.
4. Sorts documents by score in descending order.
5. Returns the top two matching documents.

Define how you handle ties and queries with no matching words.

**AI/ML connection:** This is a basic lexical retrieval exercise. It helps explain the retrieval stage of RAG, but it is not semantic search and does not use embeddings.

---

## Evaluation rubric

Each question is worth 5 marks. Use this rubric as a guide:

| Evaluation area | Marks |
|---|---:|
| Problem-solving logic | 2 |
| Correct Python usage | 1 |
| Edge-case handling | 1 |
| Readability and structure | 1 |
| **Total per question** | **5** |

Suggested overall interpretation:

| Score | Interpretation |
|---|---|
| 90–100 | Strong fundamentals |
| 75–89 | Good; practise edge cases |
| 60–74 | Developing; revisit weak topics |
| Below 60 | Rebuild fundamentals and retry |

## Recommended practice approach

1. Attempt each question without looking at a solution first.
2. Write and run your code locally.
3. Test normal, empty, invalid, and boundary inputs where applicable.
4. Explain your logic in your own words.
5. Refactor repeated logic into reusable functions.
6. Review the AI/ML connection after solving the exercise.

## How these Python skills map to AI/ML projects

| Python skill | Where it is used |
|---|---|
| Lists and dictionaries | JSON records, tool inputs, metadata |
| Sets and comprehensions | Deduplication, filtering, data preparation |
| Functions | Reusable pipeline steps and agent tools |
| OOP | Encapsulating clients, services, and data models |
| Exceptions | API failures, retries, and robust workflows |
| JSON | MCP messages, LLM structured output, API payloads |
| Text processing | Document cleaning and preprocessing |
| Chunking | RAG document ingestion |
| NumPy | Vector operations and numerical computation |
| Pandas | Dataset exploration and preprocessing |
| Cosine similarity | Vector comparison and retrieval |
| Ranking | Selecting relevant documents for RAG context |

## Next learning milestones

After completing this test, extend the exercises into small projects:

1. **CSV data-cleaning pipeline:** Load a dataset with Pandas, handle missing values, and export cleaned data.
2. **Text preprocessing pipeline:** Clean documents, split them into chunks, and attach metadata.
3. **Embedding similarity demo:** Generate embeddings with an embedding model and compare them using cosine similarity.
4. **Mini RAG application:** Retrieve relevant chunks and pass them as context to an LLM.
5. **MCP tool server:** Expose a few Python functions as tools, define input schemas, validate arguments, and return structured results.

---

**Repository:** [iamrajendraverma/python_machine_test](https://github.com/iamrajendraverma/python_machine_test)

**Goal:** Build strong Python fundamentals that translate directly into practical AI/ML and Agentic AI engineering.
