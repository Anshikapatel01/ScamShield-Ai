import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "data" / "messages.csv"

messages = []
valid_labels = {"RED", "ORANGE", "GREEN"}

with open(dataset_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        messages.append(row)

print("Total messages:", len(messages))

# Check dataset quality
errors = []

for index, item in enumerate(messages, start=2):
    message = item.get("message", "").strip()
    label = item.get("label", "").strip().upper()

    if not message:
        errors.append(f"Row {index}: Message is empty")

    if label not in valid_labels:
        errors.append(f"Row {index}: Invalid label '{label}'")

if errors:
    print("\nDataset problems:")
    for error in errors:
        print("-", error)
else:
    print("\nDataset validation: PASSED")

# Count labels
label_counts = {}

for item in messages:
    label = item["label"].strip().upper()
    label_counts[label] = label_counts.get(label, 0) + 1

print("\nLabel counts:")
for label, count in sorted(label_counts.items()):
    print(label, ":", count)