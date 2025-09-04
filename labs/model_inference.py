import joblib
import pandas as pd
from pathlib import Path

_model = None

def get_model():
    global _model
    if _model is None:
        p = Path("./models/credit_lr.pkl")
        if p.exists():
            _model = joblib.load(p)
    return _model

def infer_proba(df: pd.DataFrame) -> pd.Series:
    model = get_model()
    if model is None or df.empty:
        return pd.Series([None] * len(df))
    X = df[["divida_receita", "news_sent", "rating_score", "sector_risk", "prazo_pagamento_dias"]].fillna(0)
    return pd.Series(model.predict_proba(X)[:,1], index=df.index)
