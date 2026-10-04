import joblib
from pathlib import Path

# Saved model load karo
project_root = Path(__file__).resolve().parent.parent
model_path = project_root / "models" / "scam_model.joblib"

model = joblib.load(model_path)

print("ScamShield AI is ready!")

# User se message lo
message = input("\nEnter a message to check: ").strip()

if not message:
    print("Please enter a message.")
else:
    # Prediction aur confidence scores
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]

    # Predicted class ka confidence score
    classes = model.classes_
    predicted_index = list(classes).index(prediction)
    confidence = probabilities[predicted_index] * 100

    print("\nRisk Level:", prediction)
    print("Model confidence:", round(confidence, 2), "%")

    if prediction == "RED":
        print("Warning: This message may be dangerous.")
    elif prediction == "ORANGE":
        print("Warning: This message looks suspicious.")
    else:
        print("No known warning signs found.")

    print("\nNote: This model cannot guarantee safety.")