--- Base de dados manual – Games Shop
Abaixo está uma amostra manual da base de dados para análise (sem CSV). Edite livremente conforme seu contexto.

--- Dicionário de dados
- produto: nome do item vendido.
- regiao: região da venda (Nordeste, Sudeste, Sul, Centro-Oeste, Norte).
- data_venda: data da transação no formato AAAA-MM-DD.
- quantidade: unidades vendidas.
- preco_unitario: preço por unidade (R$).
- faturamento: quantidade × preço_unitário.

--- Tabela (amostra)
| produto   | regiao   | data_venda | quantidade | preco_unitario | faturamento |
|-----------|----------|------------|------------|----------------|-------------|
| Jogo A    | Sudeste  | 2025-01-15 | 120        | 100            | 12000       |
| Jogo B    | Nordeste | 2025-02-10 | 80         | 100            | 8000        |
| Jogo C    | Sul      | 2025-03-12 | 50         | 100            | 5000        |
| Jogo A    | Nordeste | 2025-11-25 | 60         | 100            | 6000        |
| Jogo B    | Sudeste  | 2025-12-05 | 95         | 100            | 9500        |
| Jogo C    | Centro-Oeste | 2025-07-09 | 40     | 100            | 4000        |
| Jogo A    | Sul      | 2025-11-28 | 110        | 100            | 11000       |
| Jogo B    | Norte    | 2025-01-22 | 35         | 100            | 3500        |
| Jogo C    | Sudeste  | 2025-08-14 | 70         | 100            | 7000        |
