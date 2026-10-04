import csv
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Dataset ka path
project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "data" / "messages.csv"

messages = []
labels = []

# Dataset load karo
with open(dataset_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        messages.append(row["message"])
        labels.append(row["label"].strip().upper())

# Training aur testing data alag karo
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)

# Dono models compare karo
models = {
    "CountVectorizer": Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB())
    ]),
    "TF-IDF": Pipeline([
        ("vectorizer", TfidfVectorizer()),
        ("classifier", MultinomialNB())
    ])
}

for name, model in models.items():
    print(f"\n{'=' * 40}")
    print(f"Model: {name}")
    print("=" * 40)

    # Training
    model.fit(X_train, y_train)

    # Testing
    predictions = model.predict(X_test)

    # Accuracy
    print("Accuracy:", accuracy_score(y_test, predictions))

    # Classification report
    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        labels=["GREEN", "ORANGE", "RED"],
        zero_division=0
    ))

    # Confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix(
        y_test,
        predictions,
        labels=["GREEN", "ORANGE", "RED"]
    ))

    # Incorrect predictions
    print("\nIncorrect Predictions:")
    for message, actual, predicted in zip(X_test, y_test, predictions):
        if actual != predicted:
            print(f"Message: {message}")
            print(f"Actual: {actual}")
            print(f"Predicted: {predicted}")
            print("-" * 30)