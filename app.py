import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from src.explainer import explain

# ── Page config ────────────────────────────────────────
st.set_page_config(
    page_title="Medical Symptom Checker",
    page_icon="🏥",
    layout="wide"
)

# ── Custom CSS ─────────────────────────────────────────
st.markdown("""
<style>
    /* Background */
    .stApp { background-color: #f0f4f8; }

    /* Top header bar */
    .header-bar {
        background: linear-gradient(90deg, #0077b6, #00b4d8);
        padding: 30px 40px;
        border-radius: 16px;
        margin-bottom: 30px;
        color: white;
        text-align: center;
    }
    .header-bar h1 { font-size: 2.5rem; margin: 0; }
    .header-bar p  { font-size: 1.1rem; margin-top: 8px; opacity: 0.9; }

    /* Cards */
    .card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }

    /* Disease rank card */
    .disease-card {
        background: white;
        border-left: 6px solid #0077b6;
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 14px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .disease-card h3 { color: #0077b6; margin: 0 0 4px 0; }
    .disease-card p  { color: #555; margin: 0; font-size: 0.95rem; }

    /* SHAP word pills */
    .pill-green {
        display: inline-block;
        background: #d4edda;
        color: #155724;
        border-radius: 20px;
        padding: 4px 14px;
        margin: 4px;
        font-size: 0.88rem;
        font-weight: 600;
    }
    .pill-red {
        display: inline-block;
        background: #f8d7da;
        color: #721c24;
        border-radius: 20px;
        padding: 4px 14px;
        margin: 4px;
        font-size: 0.88rem;
        font-weight: 600;
    }

    /* Section titles */
    .section-title {
        color: #0077b6;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 16px;
        border-bottom: 2px solid #00b4d8;
        padding-bottom: 6px;
    }

    /* Disclaimer */
    .disclaimer {
        background: #fff3cd;
        border-left: 5px solid #ffc107;
        border-radius: 10px;
        padding: 14px 18px;
        font-size: 0.9rem;
        color: #856404;
    }

    /* Hide streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── Load artifacts ─────────────────────────────────────
@st.cache_resource
def load_artifacts():
    model     = joblib.load("models/logreg_model.joblib")
    tfidf     = joblib.load("models/tfidf_vectorizer.joblib")
    label_map = joblib.load("models/label_map.joblib")
    desc_df   = pd.read_csv("data/raw/symptom_Description.csv")
    desc_df.columns = desc_df.columns.str.strip()
    desc_map  = dict(zip(desc_df["Disease"].str.strip(), desc_df["Description"].str.strip()))
    return model, tfidf, label_map, desc_map

model, tfidf, label_map, desc_map = load_artifacts()

# ── Header ─────────────────────────────────────────────
st.markdown("""
<div class="header-bar">
    <h1>🏥 Medical Symptom Checker</h1>
    <p>Enter your symptoms and get AI-powered disease predictions with explanations</p>
</div>
""", unsafe_allow_html=True)

# ── Layout ─────────────────────────────────────────────
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Enter Your Symptoms</div>', unsafe_allow_html=True)

    symptoms_input = st.text_area(
        "",
        placeholder="e.g. itching skin rash fever headache fatigue...",
        height=160,
        label_visibility="collapsed"
    )

    analyse = st.button("🔍 Analyse Symptoms", use_container_width=True)

    st.markdown("""
    <div class="disclaimer">
    ⚠️ <b>Disclaimer:</b> This tool is for <b>educational purposes only</b>.
    It is NOT a substitute for professional medical advice.
    Always consult a qualified doctor.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if analyse:
        if not symptoms_input.strip():
            st.warning("Please enter at least one symptom.")
        else:
            # ── Predict top-3 ──────────────────────────
            X     = tfidf.transform([symptoms_input])
            probs = model.predict_proba(X)[0]
            top3  = np.argsort(probs)[::-1][:3]

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">🩺 Top 3 Predicted Diseases</div>', unsafe_allow_html=True)

            for rank, idx in enumerate(top3, 1):
                disease = label_map[idx]
                conf    = probs[idx] * 100
                desc    = desc_map.get(disease, "No description available.")

                st.markdown(f"""
                <div class="disease-card">
                    <h3>#{rank} — {disease}</h3>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
                st.progress(int(conf))
                st.caption(f"Confidence: {conf:.1f}%")

            st.markdown('</div>', unsafe_allow_html=True)

# ── SHAP explanation ───────────────────────────────────
if analyse and symptoms_input.strip():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔬 Why this prediction? (Key Symptoms)</div>', unsafe_allow_html=True)

    disease, top_words = explain(symptoms_input)

    st.markdown(f"The model predicted **{disease}** based on these key words in your input:")
    st.markdown("<br>", unsafe_allow_html=True)

    pills_html = ""
    for word, score in top_words:
        css_class = "pill-green" if score >= 0 else "pill-red"
        arrow     = "▲" if score >= 0 else "▼"
        pills_html += f'<span class="{css_class}">{arrow} {word}</span>'

    st.markdown(pills_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("🟢 Green = symptom pushed TOWARDS this disease   |   🔴 Red = symptom pushed AWAY from this disease")
    st.markdown('</div>', unsafe_allow_html=True)