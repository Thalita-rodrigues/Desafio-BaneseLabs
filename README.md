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
# Arquitetura e Fluxo

### Fontes de dados: CSV, JSON, XML, Parquet e notícias para contexto.

### Pipeline principal:

01. Ingestão: pandas/pyarrow → leitura unificada.

02. Limpeza e padronização.

03. Feature Store: ex.: dívida/receita, rating, setor.

04. Regras de Risco: flags determinísticas (ex.: dívida/receita > 1).

05. Modelo/Score baseline: combina rating, dívida/receita, prazo, setor e sinais de notícias; rótulos “APROVAR / REVISAR / RECUSAR”.

06. RAG mock: extrai termos positivos/negativos de notícias como contexto.

07. LLM de explicação (mock): gera justificativas estruturadas.

08. API FastAPI: endpoints /score, /explicar, /simular.

09. UI Streamlit: painel do analista com score, explicações e simulação de cortes.

10. Logs e monitoramento: auditoria, drift, viés e armazenamento seguro.


 <img width="540" height="675" alt="Image" src="https://github.com/user-attachments/assets/b91c7ad0-4e1f-41e5-ae2d-9c1b3c4a167e" />

A arquitetura atende aos objetivos do desafio: sintetizar dados, identificar riscos, gerar recomendações e simular cenários.

