import pandas as pd
import numpy as np

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.copy()
    df["divida_receita"] = df["divida_total"] / df["receita_anual"]
    # Simple news sentiment
    bad_words = ["fraude", "queda", "prejuízo", "prejuizo", "investigação", "investigacao", "demissão", "demissao", "rombo", "inadimplência", "inadimplencia", "dívida", "divida", "processo", "crise", "escândalo", "escandalo"]
    good_words = ["lucro", "expansão", "expansao", "contrata", "parceria", "investimento", "crescimento", "recorde", "aumento", "inovação", "inovacao"]
    def sent(t):
        if pd.isna(t): return 0.0
        s = str(t).lower()
        sc = sum(1 for w in good_words if w in s) - sum(1 for w in bad_words if w in s)
        return float(sc)
    df["news_sent"] = df["noticias_recentes"].apply(sent)
    rating_map = {"AAA": 5, "AA": 4.5, "A": 4, "BBB": 3, "BB": 2, "B": 1, "CCC": 0.5, "CC": 0.3, "C": 0.1}
    def rscore(x):
        if pd.isna(x): return 2.5
        return rating_map.get(str(x).upper().strip(), 2.5)
    df["rating_score"] = df["rating"].apply(rscore)
    higher_risk = {"construção", "construcao", "varejo", "restaurantes"}
    def sec_risk(s):
        if pd.isna(s): return 0.0
        st = str(s).lower()
        return 0.5 if any(k in st for k in higher_risk) else 0.0
    df["sector_risk"] = df["setor"].apply(sec_risk)
    return df
