import numpy as np
import pandas as pd
from typing import Dict

def psi(expected: pd.Series, actual: pd.Series, bins: int = 10) -> float:
    # Population Stability Index
    e_counts, e_edges = np.histogram(expected.dropna(), bins=bins)
    a_counts, _ = np.histogram(actual.dropna(), bins=e_edges)
    e_perc = e_counts / max(e_counts.sum(), 1)
    a_perc = a_counts / max(a_counts.sum(), 1)
    e_perc = np.where(e_perc == 0, 1e-6, e_perc)
    a_perc = np.where(a_perc == 0, 1e-6, a_perc)
    return float(np.sum((a_perc - e_perc) * np.log(a_perc / e_perc)))

def group_rates(df: pd.DataFrame, group_col: str, label_col: str) -> Dict[str, float]:
    rates = {}
    for g, part in df.groupby(group_col):
        rates[str(g)] = float((part[label_col] == "APROVAR").mean())
    return rates
