import pandas as pd
from scoring_model import score_frame
from risk_rules import apply_rules

def simulate_thresholds(df: pd.DataFrame, th_divida_receita: float, th_score_aprovar: float, th_score_revisar: float):
    if df.empty:
        return {"msg": "dataset vazio"}
    # Reaplica regras com novo threshold
    df_rules = apply_rules(df, th_divida_receita=th_divida_receita)
    df_scored = score_frame(df_rules)
    # Reclassifica com novos cutoffs
    def relabel(s):
        if s >= th_score_aprovar: return "APROVAR"
        if s >= th_score_revisar: return "REVISAR"
        return "RECUSAR"
    df_scored["decisao_preliminar"] = df_scored["baseline_score"].apply(relabel)
    # Estatísticas de distribuição
    counts = df_scored["decisao_preliminar"].value_counts().to_dict()
    return {
        "distribuicao": counts,
        "amostra": df_scored.head(20).to_dict(orient="records")
    }
