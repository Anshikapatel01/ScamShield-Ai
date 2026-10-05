import csv
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "data" / "messages.csv"

messages = []
labels = []

with open(dataset_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        messages.append(row["message"])
        labels.append(row["label"].strip().upper())

# Stratified 75/25 split
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)

# Final evaluation model
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\n" + "=" * 50)
print("SCAMSHIELD AI - FINAL MODEL EVALUATION")
print("=" * 50)

print(f"\nDataset size: {len(messages)}")
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

print("\nAccuracy:")
print(f"{accuracy_score(y_test, predictions) * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    labels=["GREEN", "ORANGE", "RED"],
    zero_division=0
))

print("Confusion Matrix:")
print(confusion_matrix(
    y_test,
    predictions,
    labels=["GREEN", "ORANGE", "RED"]
))

print("\nIncorrect Predictions:")
print("-" * 50)

errors = 0

for message, actual, predicted in zip(
    X_test, y_test, predictions
):
    if actual != predicted:
        errors += 1
        print(f"Message: {message}")
        print(f"Actual: {actual}")
        print(f"Predicted: {predicted}")
        print("-" * 50)

print(f"\nTotal incorrect predictions: {errors}")
print(f"Total correct predictions: {len(y_test) - errors}")