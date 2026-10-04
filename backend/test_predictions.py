import joblib
from pathlib import Path

# Updated model load karo
project_root = Path(__file__).resolve().parent.parent
model_path = project_root / "models" / "scam_model.joblib"
model = joblib.load(model_path)

# Hindi, Hinglish aur English test messages
test_messages = [
    "Apna OTP mujhe bhejo, tumhara account block ho jayega",
    "Bijli ka bill jama karne ke liye yahan click karo, warna connection kat jayega",
    "Namaste, kal milte hain",
    "Badhaai ho, aapne lottery jeeti hai, inaam pane ke liye paise bhejein",
    "Apna bank password share karo",
    "Main ghar pahunch gaya hoon",
    "Turant link kholo aur apna account verify karo",
    "Your account is blocked. Share your OTP.",
    "Hello, how are you?",
]

print("SCAMSHIELD AI - MULTILINGUAL TEST")
print("-" * 50)

for message in test_messages:
    prediction = model.predict([message])[0]

    print("\nMessage:", message)
    print("Predicted risk:", prediction)
    print("-" * 50)