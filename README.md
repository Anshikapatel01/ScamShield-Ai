# 🛡️ ScamShield AI

**ScamShield AI** is a senior-friendly AI-powered scam message detection system designed to help users understand whether an incoming message looks **safe, suspicious, or high-risk**.

It combines **machine learning and rule-based detection** to classify messages into three risk levels:

- 🟢 **GREEN** — Looks safe / normal
- 🟠 **ORANGE** — Suspicious or potentially promotional
- 🔴 **RED** — High-risk scam indicators detected

The project focuses on making scam detection easier for users who may not be comfortable understanding technical or financial scam signals.

---

## 🌐 Live Demo

- **Frontend:** https://anshikapatel01.github.io/ScamShield-Ai/
- **Backend API:** https://scamshield-ai-t7gl.onrender.com
- **API Documentation:** https://scamshield-ai-t7gl.onrender.com/docs

---

## ✨ Features

### 🛡️ Risk Classification

ScamShield AI provides three simple risk levels:

| Level | Meaning |
|---|---|
| 🟢 GREEN | Message appears normal/safe |
| 🟠 ORANGE | Message contains suspicious or promotional patterns |
| 🔴 RED | Message contains strong scam indicators |

### 👴 Senior-Friendly Interface

- Large and simple interface
- Clear risk colours
- Hindi language support
- Read-aloud feature
- Simple safety instructions
- Scam reporting guidance

### 🤖 Machine Learning

The project uses:

- TF-IDF text vectorization
- Multinomial Naive Bayes classifier
- Rule-based scam detection
- FastAPI backend

### 🌐 Web Application

The frontend communicates with the deployed FastAPI backend and provides predictions without requiring the user to understand machine learning.

### 📝 Message History

Recent predictions can be viewed through the browser interface.

---

## 🧠 How It Works

```text
User enters message
        ↓
ScamShield AI backend
        ↓
Rule-based detection
        +
TF-IDF + Naive Bayes model
        ↓
Risk classification
        ↓
GREEN / ORANGE / RED
        ↓
Reasons + confidence + safety guidance
```

---

## 📊 Model Evaluation

The final training dataset contains **380 unique messages**:

| Label | Messages |
|---|---|
| 🟢 GREEN | 133 |
| 🟠 ORANGE | 120 |
| 🔴 RED | 127 |
| **Total** | **380** |

### Holdout Evaluation

A stratified 75/25 train-test split was used.

- **Training samples:** 285
- **Test samples:** 95
- **Model:** TF-IDF + Multinomial Naive Bayes
- **Accuracy:** 86.32%

### Classification Results

| Class | Precision | Recall | F1-score |
|---|---|---|---|
| 🟢 GREEN | 93% | 79% | 85% |
| 🟠 ORANGE | 79% | 87% | 83% |
| 🔴 RED | 88% | 94% | 91% |

The model achieved **94% recall for RED-risk messages** on the holdout test set.

### External Test

An additional set of 15 previously unseen challenge messages was tested separately.

**Result:** 15/15 correct — 100% on this small external test set.

> ⚠️ This external result should not be interpreted as general real-world accuracy because the test set is intentionally small.

---

## 📚 Dataset

The dataset contains curated and synthetic examples based on documented scam-message patterns.

Examples cover:

- OTP scams
- KYC scams
- Fake banking alerts
- Prize and reward scams
- Electricity/payment scams
- Government-benefit scams
- Refund scams
- SIM-related scams
- Promotional messages
- Normal everyday messages

Languages covered:

- English
- Hinglish
- Hindi / Devanagari

The dataset is intended for educational and prototype evaluation purposes and should not be treated as a representative sample of all real-world scam messages.

---

## 🛠️ Technologies

- Python
- Scikit-learn
- FastAPI
- HTML
- CSS
- JavaScript
- Joblib
- Pytest
- Machine Learning (TF-IDF Vectorizer + Multinomial Naive Bayes)

---

## 📁 Project Structure

```text
ScamShield-AI/
│
├── backend/
│   ├── app.py
│   ├── detector.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── data/
│   ├── messages.csv
│   ├── external_test.csv
│   ├── messages_additional_225.csv
│   ├── messages_hard_examples_60.csv
│   └── messages_safety_hard_30.csv
│
├── models/
│   └── scam_model.joblib
│
├── frontend/
│   └── index.html
│
├── tests/
│
├── prepare_data.py
├── predict_message.py
├── test_predictions.py
├── index.html
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/Anshikapatel01/ScamShield-Ai.git
cd ScamShield-Ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python backend/train_model.py
```

This creates `models/scam_model.joblib`.

### 4. Run the backend

```bash
uvicorn backend.app:app --reload
```

The API will run at: http://127.0.0.1:8000

### 5. Open API documentation

http://127.0.0.1:8000/docs

### 6. Run the frontend

Open `frontend/index.html` in a browser.

---

## 🔌 API Example

### Endpoint

`POST /predict`

### Example request

```json
{
  "message": "Urgent! Your account is blocked. Share your OTP."
}
```

### Example response

```json
{
  "message": "Urgent! Your account is blocked. Share your OTP.",
  "risk_level": "RED",
  "confidence": 0.91,
  "reasons": [
    "Urgent language detected",
    "OTP-related request detected"
  ],
  "rule_risk": "RED"
}
```

> Example values are illustrative; actual confidence and reasons depend on the message.

---

## 🔐 Safety Guidance

If a message is suspicious:

- ❌ Never share an OTP
- ❌ Never share your UPI PIN
- ❌ Never share passwords or CVV
- ❌ Avoid clicking suspicious links
- ✅ Verify through the organization's official app or website
- ✅ In India, suspected cyber fraud can be reported through **1930** or the official cybercrime reporting portal

---

## ⚠️ Limitations

ScamShield AI is a prototype, not a guaranteed scam detector.

- The dataset is relatively small.
- Many training examples are curated or synthetic.
- Real-world scam language changes continuously.
- Some legitimate messages may look suspicious.
- Some sophisticated scams may not be detected.
- The reported accuracy comes from a single stratified holdout split.
- External testing used only 15 additional messages.

The model should therefore be treated as a decision-support tool, not as definitive proof that a message is safe or fraudulent.

---

## 🚀 Future Improvements

- 📷 OCR for screenshots and images
- 📞 Real-time call scam detection
- 📱 WhatsApp / Telegram integration
- 🌍 More Indian languages
- 🗃️ Community-based scam-number database
- 🔄 Larger real-world datasets
- 📈 More robust cross-validation and continuous evaluation
- 🏛️ Integration with official cyber-fraud reporting systems

*These are future plans and are not currently implemented.*

---

## 👨‍💻 Project

**ScamShield AI** — built as an AI/ML project focused on improving scam awareness and making scam detection easier for everyday users and senior citizens.

---

## ⚠️ Disclaimer

ScamShield AI is an educational and prototype project. Its predictions are not guaranteed to be accurate. Always independently verify suspicious messages and never share OTPs, passwords, UPI PINs, CVV numbers, or other sensitive financial information.