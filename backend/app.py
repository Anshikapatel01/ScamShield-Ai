from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import joblib
from pathlib import Path
from backend.detector import detect_scam

# Load the trained ScamShield model
project_root = Path(__file__).resolve().parent.parent
model_path = project_root / "models" / "scam_model.joblib"
model = joblib.load(model_path)

# Create the API
app = FastAPI(title="ScamShield AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the message format
from pydantic import BaseModel, Field

class MessageRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=5000,
        description="Message to analyze (1 to 5000 characters)"
    )
# API homepage
@app.get("/")
def home():
    return {"message": "ScamShield AI API is running!"}

# Analyze a message
@app.post("/predict")
def predict(request: MessageRequest):
    message = request.message.strip()

    if not message:
        return {"error": "Please enter a message."}

    prediction = model.predict([message])[0]
    rule_risk, rule_reasons = detect_scam(message)
    probabilities = model.predict_proba([message])[0]
    classes = model.classes_
    index = list(classes).index(prediction)
    confidence = round(float(probabilities[index]) * 100, 2)
    print("AI prediction:", prediction)
    print("All probabilities:", dict(zip(classes, probabilities)))
    if rule_risk == "RED" or prediction == "RED":
        final_risk = "RED"
    elif rule_risk == "ORANGE" or prediction == "ORANGE":
        final_risk = "ORANGE"
    else:
        final_risk = "GREEN"

    return {
        "message": message,
        "risk_level": final_risk,
        "confidence": confidence,
        "reasons": rule_reasons,
        "rule_risk": rule_risk
    }