# 🧬 MediScan AI — Explainable Disease Prediction System

An AI-powered web app that predicts the most likely diseases from a user's symptoms **and explains why** it reached that conclusion. Built with Python, Scikit-learn, SHAP and Streamlit, with a bilingual **English / Tamil** interface.

🔗 **Live Demo:** https://mediscanai-1001.streamlit.app/

## 📌 Overview

Most symptom checkers give a result without any reasoning. MediScan AI tackles this with **Explainable AI (XAI)**: for every prediction it shows the top 3 likely diseases with confidence scores, a short medical description of each, and the key symptoms that pushed the model towards its answer.

| Item | Details |
|---|---|
| Diseases covered | 41 |
| Symptoms supported | 132 |
| Model | Logistic Regression (balanced class weights) |
| Explainability | SHAP `LinearExplainer` |
| Languages | English, Tamil (தமிழ்) |
| Deployment | Streamlit Community Cloud |

---

## Features

- **Guided 3-step flow** — Profile (name) → Age → Symptoms
- **Searchable multi-select** of 132 symptoms, so users never have to type exact medical keywords
- **Top-3 disease predictions** with confidence bars
- **Disease descriptions** shown for every prediction
- **Explainable results (SHAP)** — symptoms that pushed towards the diagnosis are highlighted in green, atypical ones in red
- **Bilingual UI** — switch between English and Tamil from the top-right dropdown; all labels, messages and symptom names are translated
- **Modern dark UI** — glassmorphism cards, gradient buttons, step indicator, custom fonts

---

## How It Works

```
 User selects symptoms
          │
          ▼
 Symptoms → single text string
          │
          ▼
 TF-IDF Vectorizer  (fitted once, reused at inference)
          │
          ▼
 Logistic Regression  → probabilities for 41 diseases
          │
          ├──► Top-3 diseases + confidence + description
          │
          ▼
 SHAP LinearExplainer → per-symptom contribution scores
          │
          ▼
 Highlighted "Why this prediction?" section
```

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Machine Learning | Scikit-learn (Logistic Regression, TF-IDF), imbalanced-learn (SMOTE) |
| Explainable AI | SHAP |
| Data Handling | Pandas, NumPy, Joblib |
| Web App / UI | Streamlit, custom CSS, Google Fonts |
| Version Control & Deployment | Git, GitHub, Streamlit Community Cloud |

---

## 📁 Project Structure

```
medical-symptom-checker/
├── data/
│   ├── raw/                  # Kaggle CSV files (dataset, descriptions, severity, precautions)
│   └── processed/            # Auto-generated train/val/test splits (git-ignored)
├── models/
│   ├── logreg_model.joblib   # Trained classifier
│   ├── tfidf_vectorizer.joblib
│   ├── label_map.joblib      # Integer ID → disease name
│   └── metrics.csv           # Per-class evaluation report
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── explainer.py
├── tests/
├── app.py                    # Streamlit entry point
├── requirements.txt
└── README.md
```

---

## Dataset

[Disease Symptom Prediction](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset) from Kaggle — 41 diseases, 132 symptoms, plus symptom severity, disease description and precaution files.

---

## Author

**Santhiya**
GitHub: [@santhiyasss](https://github.com/santhiyasss)

---
