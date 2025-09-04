import pandas as pd
from data_checks import run_checks

def test_data_checks_ok():
    df = pd.DataFrame([{
        "empresa":"X",
        "receita_anual":1000,
        "divida_total":100,
        "prazo_pagamento_dias":30,
        "setor":"Tecnologia",
        "rating":"BBB",
        "noticias_recentes":"crescimento e investimento"
    }])
    res = run_checks(df)
    assert res["ok"]
