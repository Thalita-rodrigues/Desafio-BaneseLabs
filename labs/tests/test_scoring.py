import pandas as pd
from preprocessing import make_features
from scoring_model import score_frame

def test_score_not_empty():
    df = pd.DataFrame([{
        "empresa": "Teste SA",
        "receita_anual": 1_000_000,
        "divida_total": 200_000,
        "prazo_pagamento_dias": 90,
        "setor": "Varejo",
        "rating": "BBB",
        "noticias_recentes": "Empresa anuncia expansão e investimento."
    }])
    feats = make_features(df)
    scored = score_frame(feats)
    assert not scored.empty
    assert "baseline_score" in scored.columns
