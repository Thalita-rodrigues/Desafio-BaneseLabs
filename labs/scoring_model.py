import pandas as pd
import numpy as np
from risk_rules import apply_rules

def baseline_score(df: pd.DataFrame):
    dr = df["divida_receita"].fillna(0)
    term = df["prazo_pagamento_dias"].fillna(0)
    score = (
        df["rating_score"].fillna(2.5)
        - 2.0 * np.clip(dr, 0, 3)
        - 0.002 * np.clip(term, 0, 360)
        + 0.3 * df["news_sent"].fillna(0)
        - 0.5 * df["sector_risk"].fillna(0)
    )
    return score

def label_from_score(s):
    if s >= 3.0:
        return "APROVAR"
    elif s >= 2.0:
        return "REVISAR"
    return "RECUSAR"

def score_frame(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty: return df
    out = apply_rules(df)
    out["baseline_score"] = baseline_score(out)
    out["decisao_preliminar"] = out["baseline_score"].apply(label_from_score)
    return out
