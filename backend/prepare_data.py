import csv
from pathlib import Path
from sklearn.model_selection import train_test_split

project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "data" / "messages.csv"

messages = []
labels = []

with open(dataset_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        messages.append(row["message"])
        labels.append(row["label"].strip().upper())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)

print("Total messages:", len(messages))
print("Training messages:", len(X_train))
print("Testing messages:", len(X_test))

print("\nTraining labels:")
for label in sorted(set(y_train)):
    print(label, ":", y_train.count(label))

print("\nTesting labels:")
for label in sorted(set(y_test)):
    print(label, ":", y_test.count(label))