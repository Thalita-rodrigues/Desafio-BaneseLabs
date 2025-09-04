import pandas as pd
from rag_engine import retrieve_context

def explain_row(row: pd.Series) -> str:
    ctx = retrieve_context(row.get("noticias_recentes") or "")
    bullets = []
    bullets.append(f"Rating: {row.get('rating')} (score {row.get('rating_score'):.2f})")
    dr = row.get('divida_receita')
    if pd.notna(dr):
        bullets.append(f"Dívida/Receita: {dr:.2f}")
    term = row.get('prazo_pagamento_dias')
    if pd.notna(term):
        bullets.append(f"Prazo de pagamento: {int(term)} dias")
    if ctx["positivos"]:
        bullets.append(f"Notícias positivas: {', '.join(ctx['positivos'])}")
    if ctx["negativos"]:
        bullets.append(f"Sinais de alerta em notícias: {', '.join(ctx['negativos'])}")
    return " • ".join(bullets)

def generate_explanations(df: pd.DataFrame):
    exps = []
    for _, row in df.iterrows():
        exps.append({
            "empresa": row.get("empresa"),
            "score": float(row.get("baseline_score")),
            "decisao_preliminar": row.get("decisao_preliminar"),
            "justificativa": explain_row(row)
        })
    return exps
