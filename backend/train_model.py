import csv
from pathlib import Path
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Project ke folders
project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "data" / "messages.csv"
model_path = project_root / "models" / "scam_model.joblib"

# Dataset load karo
messages = []
labels = []

with open(dataset_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        messages.append(row["message"])
        labels.append(row["label"].strip().upper())

# Vectorizer aur model ko ek pipeline mein jodo
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Model train karo
model.fit(messages, labels)

# Trained model save karo
joblib.dump(model, model_path)

print("Model training complete!")
print("Model saved at:", model_path)

# Ek example message par prediction
message = "Urgent! Your account is blocked. Share your OTP."
prediction = model.predict([message])

print("\nMessage:", message)
print("Predicted risk:", prediction[0])