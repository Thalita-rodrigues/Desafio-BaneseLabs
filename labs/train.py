import os, json
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score
import joblib

from data_ingestion import load_all
from preprocessing import make_features
from scoring_model import label_from_score
from scoring_model import baseline_score

MODELS_DIR = Path("./models")
MODELS_DIR.mkdir(exist_ok=True)

def create_synthetic_labels(df: pd.DataFrame) -> pd.Series:
    # Usa baseline_score para gerar rótulos binários (aprovado vs não)
    s = baseline_score(df)
    # Aprovado se >= 3.0
    y = (s >= 3.0).astype(int)
    return y

def train_model():
    df = load_all("./data")
    feats = make_features(df)
    # Seleciona features numéricas simples
    X = feats[["divida_receita", "news_sent", "rating_score", "sector_risk", "prazo_pagamento_dias"]].fillna(0)
    y = create_synthetic_labels(feats)
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    # Avaliação básica
    prob = model.predict_proba(X)[:,1]
    roc = roc_auc_score(y, prob)
    pr = average_precision_score(y, prob)
    joblib.dump(model, MODELS_DIR / "credit_lr.pkl")
    return {"roc_auc": roc, "pr_auc": pr, "n": int(X.shape[0])}

if __name__ == "__main__":
    metrics = train_model()
    print(json.dumps(metrics, indent=2))
