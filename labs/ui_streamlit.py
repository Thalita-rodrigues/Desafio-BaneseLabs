import streamlit as st
import pandas as pd
from data_ingestion import load_all
from preprocessing import make_features
from scoring_model import score_frame
from explain import generate_explanations
from simulator import simulate_thresholds
from model_inference import infer_proba

st.set_page_config(page_title="Assistente de Análise de Crédito", layout="wide")

st.title("Assistente de Análise de Crédito — Painel do Analista")

df = load_all("./data")
feats = make_features(df)
scored = score_frame(feats)

st.subheader("Base Unificada")
st.dataframe(scored.head(200))

st.subheader("Amostra de Explicações")
exps = generate_explanations(scored.head(20))
st.json(exps)

st.subheader("Simulação de Cortes")

c1, c2, c3 = st.columns(3)
th_dr = c1.number_input("Threshold Dívida/Receita", value=1.0, step=0.1, help=
"""Se o cliente deve tanto quanto ganha → dívidas/receita = 1.0.

Se deve mais do que ganha →    > 1.0 mais arriscado.

Se deve menos do que ganha →    < 1.0 mais seguro.""")
th_ap = c2.number_input("Score para APROVAR", value=3.0, step=0.1, help= "é o valor mínimo de score que o cliente precisa ter para ser aprovado automaticamente.")
th_rv = c3.number_input("Score para REVISAR", value=2.0, step=0.1, help= 
"""é o valor mínimo de score para que o cliente não seja negado de imediato.

Se o score estiver entre 2.0 e 3.0 → vai para “Revisão manual”.

Se for < 2.0 → negado.""")

sim = simulate_thresholds(feats, th_dr, th_ap, th_rv)
st.write("Distribuição:", sim["distribuicao"])
amostra_df = pd.DataFrame(sim["amostra"])  

if "decisao" in amostra_df.columns:
    opcao = st.selectbox("Filtrar por decisão:", ["Todos", "APROVAR", "REVISAR", "NEGAR"])
    if opcao != "Todos":
        st.dataframe(amostra_df[amostra_df["decisao"] == opcao])
st.dataframe(amostra_df)

st.subheader("Probabilidade (modelo LR opcional)", help="Esse gráfico mostra a probabilidade de aprovação calculada pelo modelo de Regressão Logística." )
proba = infer_proba(feats.head(200))
st.line_chart(proba.dropna())


