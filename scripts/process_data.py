"""
Processamento e consolidação de dados (opcional).
Apenas como documentação técnica.

Fluxo:
1. Carrega um CSV 
2. Normaliza colunas.
3. Calcula faturamento.
4. Gera agregados por produto e região.

"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
INPUT = DATA_DIR / "base_de_dados.csv"
OUTPUT = DATA_DIR / "consolidado.csv"

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def compute_revenue(df: pd.DataFrame) -> pd.DataFrame:
    if "faturamento" not in df.columns:
        if "quantidade" in df.columns and "preco_unitario" in df.columns:
            df["faturamento"] = df["quantidade"] * df["preco_unitario"]
    return df

def consolidate(df: pd.DataFrame) -> pd.DataFrame:
    group_cols = ["produto", "regiao"]
    agg = df.groupby(group_cols, as_index=False).agg(
        quantidade_total=("quantidade", "sum"),
        faturamento_total=("faturamento", "sum")
    )
    return agg

def main():
    if not INPUT.exists():
        print(f"Aviso: {INPUT} não existe. Este script é opcional e serve como referência.")
        return

    df = pd.read_csv(INPUT)
    df = normalize_columns(df)
    df = compute_revenue(df)
    df_out = consolidate(df)
    df_out.to_csv(OUTPUT, index=False)
    print(f"Consolidação concluída: {OUTPUT}")

if __name__ == "__main__":
    main()
