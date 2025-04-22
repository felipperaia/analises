"""
Análise de Vendas - Desafio Obrigatório
Autor: Felippe Adriel
Turma: TADS035
Data: 19/04/2024
"""

# Bibliotecas do python
import pandas as pd
import numpy as np

# 1. Cria e salva o arquivo vendas.xlsx (Observação: saber se precisa de mais dados com o professor)
data = {
    "Região": ["Norte", "Norte", "Sul", "Sul", "Norte"],
    "Mês": ["Jan", "Fev", "Jan", "Fev", "Mar"],
    "Vendas": [1500, np.nan, 2200, 1800, 2000],
    "Despesas": [300, 250, np.nan, 400, 350]
}

# Cria Dataframe e importa como Excel
df = pd.DataFrame(data)
df.to_excel("vendas.xlsx", index=False, engine="openpyxl")
print("Arquivo 'vendas.xlsx' criado com sucesso!")

# 2. Carrega e processar os dados
df = pd.read_excel("vendas.xlsx")

# Substituir NA: Mediana para vendas e Média para despesas
df["Vendas"] = df["Vendas"].fillna(df["Vendas"].median())  # Mediana = 2000
df["Despesas"] = df["Despesas"].fillna(df["Despesas"].mean())  # Média = 325

# 3. Agrupar por Região e Mês
grouped = df.groupby(["Região", "Mês"]).agg({
    "Vendas": "sum",
    "Despesas": "mean"
}).reset_index()

print("\nDados Agrupados:")
print(grouped)

# 4. Combina as colunas horizontalmente do xlsx
combined = pd.concat([df["Vendas"], df["Despesas"]], axis=1)

# 5. Sumário estatístico
summary = df.describe()
print("\nSumário Estatístico:")
print(summary)