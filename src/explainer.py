import shap
import joblib
import numpy as np

# ── Load model & vectorizer ────────────────────────────
model     = joblib.load("models/logreg_model.joblib")
tfidf     = joblib.load("models/tfidf_vectorizer.joblib")
label_map = joblib.load("models/label_map.joblib")

# ── Build SHAP explainer ───────────────────────────────
background = np.zeros((1, len(tfidf.get_feature_names_out())))
explainer  = shap.LinearExplainer(model, shap.maskers.Independent(background))

def explain(symptoms_text, top_n=10):
    X          = tfidf.transform([symptoms_text])
    pred_label = int(model.predict(X)[0])
    disease    = label_map[pred_label]

    shap_values    = explainer.shap_values(X)
    scores         = np.array(shap_values).flatten()
    feature_names  = tfidf.get_feature_names_out()

    pairs  = [(str(feature_names[i]), float(scores[i])) for i in range(len(feature_names))]
    scored = sorted(pairs, key=lambda x: abs(x[1]), reverse=True)

    return disease, scored[:top_n]

if __name__ == "__main__":
    sample = "itching skin rash nodal skin eruptions dischromic patches"
    disease, top_words = explain(sample)
    print(f"\nPredicted disease : {disease}")
    print("\nTop contributing words:")
    for word, score in top_words:
        print(f"  {word:30s}  {score:+.4f}")