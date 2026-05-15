import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
import joblib
import os

# ── Paths ──────────────────────────────────────────────
RAW   = "data/raw/dataset.csv"
OUT   = "data/processed/"
MDL   = "models/"

os.makedirs(OUT, exist_ok=True)
os.makedirs(MDL, exist_ok=True)

# ── Load & Clean ───────────────────────────────────────
df = pd.read_csv(RAW)
df.columns = df.columns.str.strip()

# Combine all symptom columns into one text string
symptom_cols = [c for c in df.columns if c != "Disease"]
df["symptoms_text"] = df[symptom_cols].fillna("").apply(
    lambda row: " ".join(v.strip() for v in row if v.strip()), axis=1
)

# ── Encode Labels ──────────────────────────────────────
le = LabelEncoder()
df["label"] = le.fit_transform(df["Disease"])
label_map = dict(zip(le.transform(le.classes_), le.classes_))
joblib.dump(label_map, MDL + "label_map.joblib")
print(f"✅ Saved label_map.joblib  ({len(label_map)} diseases)")

# ── TF-IDF Vectorise ───────────────────────────────────
tfidf = TfidfVectorizer(token_pattern=r"[a-zA-Z_]+")
X = tfidf.fit_transform(df["symptoms_text"])
y = df["label"].values
joblib.dump(tfidf, MDL + "tfidf_vectorizer.joblib")
print("✅ Saved tfidf_vectorizer.joblib")

# ── SMOTE ──────────────────────────────────────────────
sm = SMOTE(random_state=42)
X_bal, y_bal = sm.fit_resample(X, y)
print(f"✅ SMOTE done  — {X_bal.shape[0]} samples")

# ── Split ──────────────────────────────────────────────
X_tr, X_tmp, y_tr, y_tmp = train_test_split(X_bal, y_bal, test_size=0.2, random_state=42)
X_val, X_te, y_val, y_te = train_test_split(X_tmp, y_tmp, test_size=0.5, random_state=42)

# ── Save splits ────────────────────────────────────────
def save_split(X, y, name):
    pd.DataFrame.sparse.from_spmatrix(X).assign(label=y).to_csv(OUT + name, index=False)
    print(f"✅ Saved {name}")

save_split(X_tr,  y_tr,  "train.csv")
save_split(X_val, y_val, "val.csv")
save_split(X_te,  y_te,  "test.csv")

print("\n🎉 Preprocessing complete!")