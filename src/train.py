import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score
import joblib
import os

# ── Paths ──────────────────────────────────────────────
OUT  = "data/processed/"
MDL  = "models/"

# ── Load splits ────────────────────────────────────────
print("Loading data...")
train_df = pd.read_csv(OUT + "train.csv")
val_df   = pd.read_csv(OUT + "val.csv")
test_df  = pd.read_csv(OUT + "test.csv")

X_train = train_df.drop("label", axis=1).fillna(0).values
y_train = train_df["label"].values

X_val   = val_df.drop("label", axis=1).fillna(0).values
y_val   = val_df["label"].values

X_test  = test_df.drop("label", axis=1).fillna(0).values
y_test  = test_df["label"].values

print(f"✅ Train: {X_train.shape}, Val: {X_val.shape}, Test: {X_test.shape}")

# ── Train ──────────────────────────────────────────────
print("\nTraining Logistic Regression...")
model = LogisticRegression(
    class_weight="balanced",
    max_iter=1000,
    random_state=42
)
model.fit(X_train, y_train)
print("✅ Model trained!")

# ── Evaluate ───────────────────────────────────────────
val_preds  = model.predict(X_val)
test_preds = model.predict(X_test)

val_f1  = f1_score(y_val,  val_preds,  average="weighted")
test_f1 = f1_score(y_test, test_preds, average="weighted")

print(f"\n✅ Val  F1: {val_f1:.4f}")
print(f"✅ Test F1: {test_f1:.4f}")

# ── Save metrics ───────────────────────────────────────
report = classification_report(y_test, test_preds, output_dict=True)
metrics_df = pd.DataFrame(report).transpose()
metrics_df.to_csv(MDL + "metrics.csv")
print("✅ Saved metrics.csv")

# ── Save model ─────────────────────────────────────────
joblib.dump(model, MDL + "logreg_model.joblib")
print("✅ Saved logreg_model.joblib")

print("\n🎉 Training complete!")