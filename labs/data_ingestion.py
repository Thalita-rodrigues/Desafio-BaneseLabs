import os, json
from pathlib import Path
import pandas as pd
import xml.etree.ElementTree as ET

canonical_cols = {
    "empresa": ["empresa", "Empresa", "nome_empresa", "nome"],
    "receita_anual": ["receita_anual", "Receita Anual", "receita", "faturamento", "annual_revenue"],
    "divida_total": ["divida_total", "Dívida Total", "divida", "total_debt"],
    "prazo_pagamento_dias": ["prazo_pagamento_dias", "Prazo de Pagamento (dias)", "prazo_pagamento", "payment_term_days"],
    "setor": ["setor", "Setor", "categoria_setor", "industry"],
    "rating": ["rating", "Rating", "avaliacao", "credit_rating"],
    "noticias_recentes": ["noticias_recentes", "Notícias Recentes", "news", "recent_news"]
}

def normalize_df(df):
    df2 = df.copy()
    df2.columns = [str(c) for c in df2.columns]
    out = pd.DataFrame()
    for norm, candidates in canonical_cols.items():
        for c in df2.columns:
            if c in candidates:
                out[norm] = df2[c]
                break
        if norm not in out.columns:
            out[norm] = pd.NA
    return out

def try_read_csv(p):
    try:
        return pd.read_csv(p)
    except Exception:
        try:
            return pd.read_csv(p, sep=';')
        except Exception:
            return None

def try_read_json(p):
    try:
        with open(p, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
        return pd.DataFrame(data)
    except Exception:
        try:
            return pd.read_json(p, lines=True)
        except Exception:
            return None

def try_read_xml(p):
    try:
        tree = ET.parse(p)
        root = tree.getroot()
        candidates = [child for child in root if list(child)] or list(root)
        rows = []
        for rec in candidates:
            d = {}
            for child in list(rec):
                if list(child):
                    for gc in list(child):
                        d[f"{child.tag}_{gc.tag}"] = (gc.text or "").strip()
                else:
                    d[child.tag] = (child.text or "").strip()
            if d:
                rows.append(d)
        if rows:
            return pd.DataFrame(rows)
        return None
    except Exception:
        return None

def try_read_parquet(p):
    try:
        return pd.read_parquet(p)
    except Exception:
        return None

def load_all(data_dir: str) -> pd.DataFrame:
    p = Path(data_dir)
    frames = []
    for root, _, files in os.walk(p):
        for f in files:
            ext = f.lower().split('.')[-1]
            fp = Path(root) / f
            df = None
            if ext == "csv":
                df = try_read_csv(fp)
            elif ext == "json":
                df = try_read_json(fp)
            elif ext == "xml":
                df = try_read_xml(fp)
            elif ext == "parquet":
                df = try_read_parquet(fp)
            if df is not None and not df.empty:
                nf = normalize_df(df)
                nf["__source_file"] = f
                frames.append(nf)
    if frames:
        df = pd.concat(frames, ignore_index=True)
        df = df.drop_duplicates(subset=["empresa"], keep="first")
    else:
        df = pd.DataFrame(columns=list(canonical_cols.keys()))
    # Numeric casts
    for col in ["receita_anual", "divida_total", "prazo_pagamento_dias"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df
