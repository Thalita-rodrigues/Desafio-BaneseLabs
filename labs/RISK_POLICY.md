# Política de Risco & Governança (Protótipo)

1. **Validação Humana**: toda decisão automatizada é preliminar.
2. **Auditoria**: toda chamada é logada (endpoint, parâmetros, volume).
3. **Transparência**: justificativas por empresa + documentação de modelo.
4. **Dados**: checagens mínimas (colunas, valores inválidos, duplicatas).
5. **Monitoramento**: PSI para drift; limiar 0.2 aciona revisão.
6. **Viés**: medir taxas por grupo (setor/rating) e abrir investigação se gap > 20%.
