import re
import unicodedata
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho do arquivo (coloque ambiental_rios.csv na mesma pasta deste script)
CSV_PATH = Path(__file__).parent / "ambiental_rios.csv"
OUTPUT_RANKING = Path(__file__).parent / "ranking_rios.csv"
OUTPUT_PLOT = Path(__file__).parent / "ranking_poluição.png"

def normalize_col(name: str) -> str:
    # remove acentos, coloca em minúsculas e substitui não-alfa por underscore
    nfkd = unicodedata.normalize("NFKD", str(name))
    no_accent = "".join([c for c in nfkd if not unicodedata.combining(c)])
    s = re.sub(r"\W+", "_", no_accent.lower()).strip("_")
    return s

def LoadAndPrepare(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")
    df = pd.read_csv(csv_path)
    # normaliza os nomes das colunas
    col_map = {c: normalize_col(c) for c in df.columns}
    df = df.rename(columns=col_map)
    # identifica as colunas de rio e índice
    possible_rio = [c for c in df.columns if c in ("rio", "nome", "name")]
    possible_indice = [c for c in df.columns if "indice" in c or "polu" in c or "pollu" in c]
    if not possible_rio or not possible_indice:
        raise ValueError(f"Colunas esperadas não encontradas. Colunas do CSV: {list(df.columns)}")
    rio_col = possible_rio[0]
    indice_col = possible_indice[0]
    # garantir tipo numérico no índice
    df[indice_col] = pd.to_numeric(df[indice_col], errors="coerce")
    df = df.dropna(subset=[rio_col, indice_col]).copy()
    df = df.rename(columns={rio_col: "rio", indice_col: "indice"})
    return df[["rio", "indice"]]

def classify_rules(df: pd.DataFrame) -> pd.DataFrame:
    #Regras: <=45 seguro, 46-75 Alerta, >75 critico
    conditions = [
        (df["indice"] <= 45),
        (df["indice"] >= 46) & (df["indice"] <= 75),
        (df["indice"] > 75),
    ]
    choices = ["Seguro", "Alerta", "Crítico"]
    df["classificacao"] = np.select(conditions, choices, default="Desconhecido")
    return df

def build_ranking(df: pd.DataFrame) -> pd.DataFrame:
    df_sorted = df.sort_values("indice", ascending=False).reset_index(drop=True)
    df_sorted["ranking"] = np.arange(1, len(df_sorted) + 1)
    return df_sorted

def plot_ranking(df: pd.DataFrame, out_path: Path):
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data=df, x="rio", y="indice", palette="rocket")
    ax.set_xlabel("Rio")
    ax.set_ylabel("Índice de poluição")
    ax.set_title("Ranking de rios por índice de poluição")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.show()

def main():
    df = LoadAndPrepare(CSV_PATH)
    df = classify_rules(df)
    ranked = build_ranking(df)
    # salvar ranking
    ranked.to_csv(OUTPUT_RANKING, index=False, encoding="utf-8-sig")
    print(f"Ranking salvo em: {OUTPUT_RANKING}")
    print("Top 10 rios mais poluídos:")
    print(ranked.head(10)[["ranking", "rio", "indice", "classificacao"]].to_string(index=False))
    plot_ranking(ranked, OUTPUT_PLOT)
    print(f"Gráfico salvo em: {OUTPUT_PLOT}")

if __name__ == "__main__":
    main()