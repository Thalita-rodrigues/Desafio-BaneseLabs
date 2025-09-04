# Model Card — Assistente de Análise de Crédito (Protótipo)

**Propósito**: Apoiar analistas com score e explicações preliminares.  
**Dados**: Fictícios, multiformato (CSV/JSON/XML/Parquet).  
**Modelo**: Regras + baseline score + opcional Logistic Regression treinada em rótulos sintéticos.  
**Riscos**: vieses por setor/rating/notícias.  
**Mitigação**: regras transparentes, auditoria, simulações de corte, monitoramento de drift (PSI), checagens de dados.

**Não usar para** decisão final automatizada. Exige validação humana e políticas do banco.
