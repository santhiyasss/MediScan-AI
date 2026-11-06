MediScan AI — Explainable Disease Prediction System

An AI-powered web app that predicts the most likely diseases from a user's symptoms and explains why it reached that conclusion. Built with Python, Scikit-learn, SHAP and Streamlit, with a bilingual English / Tamil interface.

Live Demo:https://mediscanai-1001.streamlit.app/

Overview:
Most symptom checkers give a result without any reasoning. MediScan AI tackles this with Explainable AI (XAI): for every prediction it shows the top 3 likely diseases with confidence scores, a short medical description of each, and the key symptoms that pushed the model towards its answer.

Project Structure:
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
