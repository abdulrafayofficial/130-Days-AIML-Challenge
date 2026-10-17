"""
data_parser.py
Day 34: Real-world data parsing in pure Python (no pandas).

Pipeline: load CSV -> inspect missing values -> clean -> compute stats -> save CSV.
Dataset: Titanic (Kaggle).
"""

import csv

INPUT_FILE = r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\Titanic-Dataset.csv"
OUTPUT_FILE = r"C:\Users\SL\OneDrive\Desktop\Study Corner\Python\Day 130 Challenge\Day34_Real-world data parsing — CSV, JSON, data cleaning in pure Python\titanic_clean.csv"


# ---------- 1. LOAD ----------
def load_csv(filepath):
    """Read a CSV file and return its rows as a list of dictionaries."""
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        # list() copies the data into memory before the file is closed
        return list(csv.DictReader(f))


# ---------- 2. MISSING VALUES ----------
def count_missing(rows):
    """Count empty values in every column. Returns {column: count}."""
    missing = {}
    for column in rows[0].keys():
        count = 0
        for row in rows:
            if row[column].strip() == "":
                count += 1
        missing[column] = count
    return missing


# ---------- 3. HELPERS ----------
def to_float(value):
    """Convert a string to float. Return None if it is empty or invalid."""
    try:
        return float(value)
    except ValueError:
        return None


def get_median(values):
    """Return the median of a list of numbers."""
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        # Odd count: take the middle element
        return sorted_values[mid]
    # Even count: average of the two middle elements
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def get_mode(values):
    """Return the most frequent value in a list."""
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return max(counts, key=counts.get)


# ---------- 4. CLEAN ----------
def clean_data(rows):
    """
    Clean the raw Titanic rows.

    Rules:
    - Drop the Cabin column (687 of 891 values are missing).
    - Fill missing Age with the median age.
    - Fill missing Embarked with the most common port (mode).
    - Strip extra spaces from text fields and lowercase Sex.
    - Convert numeric columns to int/float.
    - Skip rows with an invalid (missing or negative) Fare.
    - Skip duplicate PassengerId values.
    """
    # Compute fill values once, using only valid data
    valid_ages = [to_float(r["Age"]) for r in rows if to_float(r["Age"]) is not None]
    age_median = get_median(valid_ages)

    embarked_values = [r["Embarked"].strip() for r in rows if r["Embarked"].strip() != ""]
    embarked_mode = get_mode(embarked_values)

    cleaned = []
    seen_ids = set()
    removed_bad = 0
    removed_dup = 0

    for row in rows:
        # Skip duplicates
        pid = row["PassengerId"].strip()
        if pid in seen_ids:
            removed_dup += 1
            continue
        seen_ids.add(pid)

        # Skip rows with an invalid fare
        fare = to_float(row["Fare"])
        if fare is None or fare < 0:
            removed_bad += 1
            continue

        # Fill missing Age with the median
        age = to_float(row["Age"])
        if age is None:
            age = age_median

        # Fill missing Embarked with the mode
        embarked = row["Embarked"].strip()
        if embarked == "":
            embarked = embarked_mode

        cleaned.append({
            "PassengerId": int(pid),
            "Survived": int(row["Survived"]),
            "Pclass": int(row["Pclass"]),
            "Name": row["Name"].strip(),
            "Sex": row["Sex"].strip().lower(),
            "Age": age,
            "SibSp": int(row["SibSp"]),
            "Parch": int(row["Parch"]),
            "Ticket": row["Ticket"].strip(),
            "Fare": fare,
            "Embarked": embarked,
            # Cabin is intentionally left out
        })

    print(f"\nRemoved bad rows: {removed_bad}")
    print(f"Removed duplicates: {removed_dup}")
    print(f"Age median used: {age_median}")
    print(f"Embarked mode used: {embarked_mode}")
    return cleaned


# ---------- 5. STATS ----------
def compute_stats(rows, column):
    """Return mean, median, min and max of a numeric column."""
    values = [row[column] for row in rows]
    return {
        "mean": round(sum(values) / len(values), 2),
        "median": get_median(values),
        "min": min(values),
        "max": max(values),
    }


# ---------- 6. SAVE ----------
def save_csv(rows, outpath):
    """Write a list of dictionaries to a CSV file."""
    with open(outpath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


# ---------- MAIN ----------
def main():
    rows = load_csv(INPUT_FILE)
    print("Total rows:", len(rows))

    print("\nMissing values (BEFORE cleaning):")
    for column, count in count_missing(rows).items():
        print(f"  {column}: {count}")

    cleaned = clean_data(rows)
    print("Clean rows:", len(cleaned))

    # count_missing expects strings, so convert values back to str for the check
    print("\nMissing values (AFTER cleaning):")
    as_strings = [{k: str(v) for k, v in r.items()} for r in cleaned]
    for column, count in count_missing(as_strings).items():
        print(f"  {column}: {count}")

    print("\nStats:")
    for column in ["Age", "Fare"]:
        print(f"  {column}: {compute_stats(cleaned, column)}")

    survived = sum(r["Survived"] for r in cleaned)
    print(f"\nSurvival rate: {round(survived / len(cleaned) * 100, 1)}%")

    save_csv(cleaned, OUTPUT_FILE)
    print("\nClean data saved:", OUTPUT_FILE)


if __name__ == "__main__":
    main()