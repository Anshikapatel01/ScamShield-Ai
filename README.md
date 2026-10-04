# 🛡️ ScamShield AI

An AI-powered scam message detection system that identifies potentially fraudulent messages and classifies them into three risk levels.

## 🚀 Features

- 🔴 RED: High-risk messages, such as OTP and password scams.
- 🟠 ORANGE: Suspicious messages, such as fake offers and prize scams.
- 🟢 GREEN: Normal and safe-looking messages.
- 🤖 Machine learning using Naive Bayes.
- 🔍 Rule-based scam detection.
- 🌐 FastAPI backend.
- 💻 Simple web interface.
- 📝 Message history.

## 🛠️ Technologies

- Python
- Scikit-learn
- FastAPI
- HTML, CSS, JavaScript
- Joblib
- Pytest

## 📁 Project Structure

```text
ScamShield-AI/
├── backend/
│   ├── app.py
│   ├── detector.py
│   ├── train_model.py
│   └── evaluate_model.py
├── data/
│   └── messages.csv
├── models/
│   └── scam_model.joblib
├── frontend/
│   └── index.html
├── tests/
├── prepare_data.py
├── predict_message.py
├── test_predictions.py
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ScamShield-AI
```

Install dependencies:

```bash
pip install fastapi uvicorn scikit-learn pandas joblib pytest
```

Train the model:

```bash
python backend/train_model.py
```

Start the backend:

```bash
uvicorn backend.app:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

Open `frontend/index.html` in your browser to use the web interface.

## 📊 Model Evaluation

The current experiment compares CountVectorizer and TF-IDF with Multinomial Naive Bayes.

CountVectorizer achieved 94.74% accuracy on the current 19-message test split.

These results are preliminary and do not guarantee real-world scam detection performance.

## ⚠️ Disclaimer

ScamShield AI is an educational project. Its predictions are not guaranteed to be accurate. Always verify suspicious messages independently and never share OTPs, passwords, or sensitive banking information.

## 👨‍💻 Author

Created as an AI and machine learning project.
