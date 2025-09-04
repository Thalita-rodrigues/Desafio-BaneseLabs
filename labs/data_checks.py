import pandas as pd

REQUIRED_COLS = ["empresa", "receita_anual", "divida_total", "prazo_pagamento_dias", "setor", "rating", "noticias_recentes"]

def run_checks(df: pd.DataFrame) -> dict:
    issues = []
    # Required columns
    for c in REQUIRED_COLS:
        if c not in df.columns:
            issues.append(f"missing_column:{c}")
    # Basic validity
    if "receita_anual" in df and (df["receita_anual"] <= 0).any():
        issues.append("invalid:receita_anual<=0")
    if "divida_total" in df and (df["divida_total"] < 0).any():
        issues.append("invalid:divida_total<0")
    # Duplicates
    if "empresa" in df and df["empresa"].duplicated().any():
        issues.append("duplicates:empresa")
    return {"ok": len(issues) == 0, "issues": issues}
