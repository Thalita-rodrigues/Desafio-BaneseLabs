from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class ScoreRequest(BaseModel):
    limit: int = Field(50, ge=1, le=1000)

class SimulacaoRequest(BaseModel):
    th_divida_receita: float = 1.0
    th_score_aprovar: float = 3.0
    th_score_revisar: float = 2.0

class EmpresaScore(BaseModel):
    empresa: str
    baseline_score: float
    decisao_preliminar: str

class SimulacaoResponse(BaseModel):
    distribuicao: Dict[str, int]
    amostra: List[Dict]
