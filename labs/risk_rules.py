import pandas as pd

# Regras determinísticas: thresholds simples; em produção, parametrizar via DB/feature store
def apply_rules(df: pd.DataFrame, th_divida_receita: float = 1.0):
    if df.empty:
        return df
    out = df.copy()
    out["rule_flag_divida"] = out["divida_receita"] > th_divida_receita
    out["rule_flag_prazo"] = out["prazo_pagamento_dias"].fillna(0) > 120
    return out
