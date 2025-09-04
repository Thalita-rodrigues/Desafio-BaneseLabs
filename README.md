# Desafio-BaneseLabs
Criando um Assistente de Análise de Crédito Inteligente, com o objetivo de otimizar o processo de concessão de empréstimos a pequenas e médias empresas(PMEs).
# Assistente de Análise de Crédito — Protótipo

Este protótipo demonstra um fluxo ponta-a-ponta para um assistente de análise de crédito:
ingestão de dados, preparação, cálculo de score, geração de justificativas com LLM (mock),
e simulação de cenários via API.

## Estrutura
- `app.py`: API FastAPI com endpoints para score, justificativas e simulações.
- `data_ingestion.py`: Leitura unificada de CSV/JSON/XML/Parquet.
- `preprocessing.py`: Limpeza, padronização e engenharia de features.
- `risk_rules.py`: Regras determinísticas do banco (thresholds e políticas).
- `scoring_model.py`: Score baseline (pode ser substituído por modelo ML).
- `rag_engine.py`: Mock de RAG: busca simples em "notícias" para contexto.
- `explain.py`: Geração de justificativas estruturadas (sem chamada externa).
- `simulator.py`: Cenários alterando parâmetros (ex.: limite de dívida/receita).
- `tests/`: Exemplos de testes unitários.

## Como rodar
```bash
pip install fastapi uvicorn pandas pyarrow
uvicorn app:app --reload --port 8000

Sem docker
cd assistente_credito_propotipo
pip install -r requirements.txt
pyhton train.py

#API
uvicorn app:app --reload -- port 8000

#UI
streamlit run ui_streamlit.py -- server.port 8501

#Com Docker

docker compose up -- build

```
