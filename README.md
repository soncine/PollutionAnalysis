# 🌊 Pollution Analysis - Análise de Poluição de Rios

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Visão Geral

O projeto **Pollution Analysis** é uma ferramenta de linha de comando desenvolvida em Python com foco em **análise de dados ambientais**. Seu principal objetivo é automatizar o processo de leitura, limpeza, classificação e visualização de dados de poluição em corpos d'água (rios). A partir de um arquivo CSV bruto, o sistema gera um ranking ordenado dos rios mais poluídos, classifica cada um em níveis de criticidade e produz um gráfico estatístico de alta qualidade para facilitar a tomada de decisão e comunicação dos resultados.

---

## ✨ Funcionalidades

- **Normalização Inteligente**: Remove acentos, caracteres especiais e padroniza os nomes das colunas automaticamente, garantindo compatibilidade com diferentes formatos de entrada.
- **Pré-processamento Robusto**: Detecta automaticamente as colunas que contêm o nome dos rios e o índice de poluição, tratando valores ausentes (NaN) e convertendo dados para tipos numéricos.
- **Classificação por Criticidade**: Aplica regras de negócio para enquadrar cada rio nas categorias **Seguro**, **Alerta** ou **Crítico**.
- **Geração de Ranking**: Ordena os rios do maior para o menor índice de poluição, atribuindo uma posição numérica no ranking.
- **Exportação de Dados**: Salva o ranking completo em um arquivo CSV estruturado.
- **Visualização Gráfica**: Cria um gráfico de barras profissional utilizando **Seaborn** e **Matplotlib**, salvo em alta resolução (PNG) para apresentações ou relatórios.

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca | Finalidade |
| :--- | :--- |
| **Pandas** | Manipulação, limpeza e estruturação dos dados tabulares. |
| **NumPy** | Operações matemáticas e seleção condicional em arrays. |
| **Matplotlib** | Criação e customização da figura do gráfico. |
| **Seaborn** | Estilização avançada e geração de gráficos estatísticos com alta apelo visual. |
| **Unicodedata / re** | Normalização de strings (remoção de acentos e caracteres especiais). |

---

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina.

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/pollution-analysis.git
cd pollution-analysis
