# Mock de um motor RAG: em produção, substituir por busca embutida + embeddings.
from typing import List, Dict

NEG = ["fraude", "queda", "prejuízo", "prejuizo", "investigação", "investigacao", "demissão", "demissao", "rombo", "inadimplência", "inadimplencia",
       "dívida", "divida", "processo", "crise", "escândalo", "escandalo"]
POS = ["lucro", "expansão", "expansao", "contrata", "parceria", "investimento", "crescimento", "recorde", "aumento", "inovação", "inovacao"]

def retrieve_context(noticia: str) -> Dict[str, List[str]]:
    if not noticia:
        return {"positivos": [], "negativos": []}
    t = noticia.lower()
    pos = [w for w in POS if w in t]
    neg = [w for w in NEG if w in t]
    return {"positivos": pos, "negativos": neg}
