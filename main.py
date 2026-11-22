"""Entry point for the Python machine test.

Runs every level in order. Run a single level by executing its file directly,
e.g. `python level_2_collections.py`.
"""

from dataset import patients
import level_1_fundamentals
import level_2_collections
import level_3_functions
import level_4_oop_json
import level_5_ai_ml


def main():
    print("Q1:", level_1_fundamentals.remove_duplicates([1, 2, 2, 3, 4, 3, 5, 1]))
    print("Q2:", level_1_fundamentals.filter_high_glucose_names(patients))
    print("Q3:", level_1_fundamentals.count_word_frequency("AI ML AI Python ML AI"))
    print("Q4:", level_1_fundamentals.find_max_min([85, 92, 45, 76, 98, 60]))


if __name__ == "__main__":
    main()
