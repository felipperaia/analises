
# Análise Estatística: Comparação de Grupos Etários

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Repositório contendo análises estatísticas para comparação de distribuições etárias entre dois grupos, desenvolvido como parte da disciplina de Data Science.

---

## 📌 Visão Geral do Projeto

Este projeto foi desenvolvido para **comparar estatisticamente dois grupos etários**, testando se há diferenças significativas em suas distribuições. Utiliza técnicas como teste de normalidade (Shapiro-Wilk), teste t de Student e visualização de dados.

### Objetivos Principais:
1. Realizar análise descritiva das idades.
2. Testar normalidade dos dados.
3. Aplicar testes estatísticos paramétricos/não paramétricos.
4. Gerar visualizações profissionais (histograma e boxplot).

---

## 🚀 Funcionalidades

- **Análise Descritiva**: Cálculo de média, variância e IQR.
- **Testes Estatísticos**:
  - Shapiro-Wilk (normalidade).
  - Teste t de Student (dados normais).
  - Teste U de Mann-Whitney (dados não normais).
- **Visualização**: Gráficos em alta resolução (TIFF/PNG).
- **Relatório Técnico**: Documentação detalhada em Markdown.

---

---

## ⚙️ Pré-requisitos

- Python 3.10+
- Bibliotecas:
  ```bash
  pip install pandas numpy scipy matplotlib openpyxl
  ```

---

## 🛠️ Instalação e Uso

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/analise-grupos-etarios.git
   cd analise-grupos-etarios
   ```

2. **Execute a análise eletiva**:
   ```bash
   python notebooks/eletiva-analise.py
   ```

3. **Gere o relatório**:
   - O relatório técnico (`relatorio.md`) e os gráficos (`results/`) serão atualizados automaticamente.

---

## 📊 Resultados Destacados

### Estatísticas Descritivas
| Grupo   | Média | Variância | IQR  |
|---------|-------|-----------|------|
| Grupo 1 | 24.5  | 76.06     | 13   |
| Grupo 2 | 26.4  | 63.38     | 10   |

### Teste t de Student
- **Estatística t**: -1.02  
- **p-valor**: 0.317  
- **Conclusão**: Não há diferença significativa (p > 0.05).

---

## 📚 Referências

- **SciPy**: Virtanen, P. et al. (2020). *Nature Methods*.  
- **pandas**: McKinney, W. (2010). *Proceedings of the 9th Python in Science Conference*.  
- **Matplotlib**: Hunter, J. D. (2007). *Computing in Science & Engineering*.

---

## 👥 Contribuição

Contribuições são bem-vindas! Siga os passos:
1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

**Desenvolvido por Felippe Adriel**  
📧 Contato: [LinkedIn](https://www.linkedin.com/in/felippe-adriel-232527163/) | [GitHub](https://github.com/felipperaia)
