# Manual smoke tests
- GET /health -> {"status":"ok"}
- GET /score?limit=10 -> 10 registros com baseline_score/decisao_preliminar
- GET /explicar -> lista de objetos com justificativa
- GET /simular -> alterar thresholds e checar distribuição
