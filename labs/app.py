from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any
import pandas as pd

from data_ingestion import load_all
from preprocessing import make_features
from scoring_model import score_frame
from explain import generate_explanations
from simulator import simulate_thresholds

from schemas import ScoreRequest, SimulacaoRequest
from audit import write_audit
from data_checks import run_checks
from model_inference import infer_proba
import yaml, os

with open("config/config.yaml", "r", encoding="utf-8") as fh:
    CFG = yaml.safe_load(fh)

app = FastAPI(title=CFG['app']['title'])

# Em produção, dados viriam de um data lake / DB. Aqui lemos um caminho local.
DATA_DIR = CFG['data']['path']
AUDIT_LOG = CFG['security']['audit_log_path']

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/score")
def score(limit:int = 50):
    df = load_all(DATA_DIR)
    feats = make_features(df)
    scored = score_frame(feats).head(limit)
    return scored.to_dict(orient="records")

@app.get("/explicar")
def explicar(limit:int = 10):
    df = load_all(DATA_DIR)
    feats = make_features(df)
    scored = score_frame(feats).head(limit)
    exps = generate_explanations(scored)
    return exps

@app.get("/simular")
def simular(th_divida_receita: float = 1.0, th_score_aprovar: float = 3.0, th_score_revisar: float = 2.0):
    df = load_all(DATA_DIR)
    feats = make_features(df)
    result = simulate_thresholds(feats, th_divida_receita, th_score_aprovar, th_score_revisar)
    return result

