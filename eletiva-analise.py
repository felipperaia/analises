"""
Comparação de Grupos - Desafio Eletivo
Autor: Felippe Adriel
Turma: TADS035
Data: 19/04/2024
"""

# Bibliotecas
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Configuração dos plots
print(plt.style.available)
plt.rcParams["figure.dpi"] = 300

# 1. Dados dos grupos
grupo1 = [12, 15, 18, 22, 22, 25, 28, 30, 35, 40]
grupo2 = [15, 18, 21, 25, 25, 28, 31, 33, 38, 43]

# 2. Função para cálculo de estatísticas
def calcular_estatisticas(dados, nome_grupo):
    return pd.DataFrame({
        "Grupo": [nome_grupo],
        "Média": [np.mean(dados)],
        "Variância": [np.var(dados, ddof=1)],
        "IQR": [stats.iqr(dados)]
    })

# Calcula as estatísticas
stats_df = pd.concat([
    calcular_estatisticas(grupo1, "Grupo 1"),
    calcular_estatisticas(grupo2, "Grupo 2")
])

print("\nEstatísticas Descritivas:")
print(stats_df)

# 3. Teste de normalidade (usando o Shapiro)
_, p_g1 = stats.shapiro(grupo1)
_, p_g2 = stats.shapiro(grupo2)

print(f"\nTeste de Normalidade:\nGrupo 1: p={p_g1:.4f}\nGrupo 2: p={p_g2:.4f}")

# 4. Seleção do teste estatístico
if p_g1 > 0.05 and p_g2 > 0.05:
    print("\nAmbos grupos normais: Usando Teste t de Student")
    t_stat, p_valor = stats.ttest_ind(grupo1, grupo2)
    print(f"t = {t_stat:.2f}, p = {p_valor:.4f}")
else:
    print("\nDados não normais: Usando Teste U de Mann-Whitney")
    u_stat, p_valor = stats.mannwhitneyu(grupo1, grupo2)
    print(f"U = {u_stat}, p = {p_valor:.4f}")

# 5. Visualização
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Histograma comparativo
axs[0].hist(grupo1, bins=5, alpha=0.7, label="Grupo 1", color="skyblue")
axs[0].hist(grupo2, bins=5, alpha=0.7, label="Grupo 2", color="salmon")
axs[0].set_title("Distribuição de Idades")
axs[0].legend()

# Boxplot
axs[1].boxplot([grupo1, grupo2], labels=["Grupo 1", "Grupo 2"], patch_artist=True)
axs[1].set_title("Comparação de Médias")

plt.tight_layout()
plt.savefig("comparacao_grupos.tiff", dpi=300, format="tiff")  # Alta resolução
plt.show()