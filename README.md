# 📊 Excel to Pandas Analytics - Análise de Dados com Python & Pandas

Projeto prático de estudos focado na exploração, tratamento e análise de dados transacionais de vendas no varejo de informática (fictício). O objetivo é demonstrar a transição entre manipulação de planilhas Excel e automação analítica com Python e a biblioteca **Pandas**.

---

## 🎯 Objetivos de Aprendizado

- **Leitura & Validação:** Carregamento de planilhas Excel estruturadas com múltiplas abas via `pandas` e `openpyxl`.
- **Limpeza & Sanitização:** Conversão de formatos de datas (`datetime64`), tratamento de nulos e recálculo seguro de métricas.
- **Engenharia de Features & Pipeline Modular:** Criação de pipeline reutilizável em `src/` para aplicação de regras de negócio (cálculo de faturamento, classificação de status de estoque e ordenação temporal de meses).
- **Agregações & Resumos Temporais:** Uso de `groupby` e `.agg()` para consolidações mensais, respeitando a ordem cronológica real dos meses (evitando a ordenação alfabética padrão).
- **Visualização de Dados:** Gráficos de barras (`seaborn` / `matplotlib`) e formatação monetária de tabelas de resumo.
- **Raciocínio Analítico & Métricas:** Cálculo aprofundado de indicadores de negócio como **Ticket Médio**, diferenciando cálculos ingênuos de agregações por transação única (`nunique` e `groupby`).

---

## 🗂️ Estrutura do Projeto

```text
excel-to-pandas-analytics/
├── data/
│   ├── raw/
│   │   └── loja_informatica_2026.xlsx       # Dados brutos (abas: 'Dados Detalhados' e 'Resumo Mensal')
│   └── processed/
│       └── loja_informatica_tratada.xlsx    # Dados limpos e enriquecidos exportados via script
├── notebooks/
│   ├── 03_analise.ipynb                    # Agregações temporais cronológicas, tabelas e gráficos
│   └── 04_analise.ipynb                    # Métricas de negócio: Ticket Médio e validação por pedido
├── src/
│   └── excel_to_pandas_analytics/          # Pacote Python com utilitários reutilizáveis
│       ├── __init__.py                     # Exportação das funções públicas do pipeline
│       ├── file_base_data.py               # Leitura segura com resolução dinâmica de caminhos
│       ├── tratamento.py                   # Pipeline central de transformação e enriquecimento
│       ├── recalculate_excel.py            # Recálculo de fórmulas de vendas
│       ├── status_estoque.py               # Regras de negócio de estoque (Crítico/Baixo/Normal)
│       └── convertion_to_data_pandas.py    # Conversão de tipagem de datas
├── pyproject.toml                          # Gerenciamento de dependências via Poetry
└── README.md                               # Documentação do projeto
```

---

## 🔬 Observação

As planilhas estão versionadas no repositório apenas porque contêm dados fictícios, criados exclusivamente para fins de estudo e prática.

---

## 🔬 Trilha dos Notebooks

1. **`03_analise.ipynb` - Agregações Temporais & Visualização:**
   - Integração direta com o pacote `excel_to_pandas_analytics` (`carregar_dados_loja` e `tratar_dados`).
   - **Ordenação Cronológica dos Meses:** Uso de `pd.Categorical` para garantir que o `groupby('Mês')` siga o calendário real (`Janeiro -> Fevereiro -> ... -> Dezembro`), eliminando o problema clássico de ordenação alfabética (`Abril -> Agosto...`).
   - Apresentação de tabela resumida estilizada com formatação monetária (`R$`).
   - Gráfico de barras com `seaborn` ilustrando a curva do faturamento ao longo do ano.

2. **`04_analise.ipynb` - Métricas Analíticas & Boas Práticas:**
   - Cálculo do **Ticket Médio por Transação**.
   - Comparativo metodológico: `.sum() / len()` vs `.mean()` vs agrupamento por pedido real (`.nunique()` e `.groupby()`).
   - Simulação analítica com carrinhos com múltiplos itens, demonstrando a prevenção de distorções estatísticas.

---

## 🛠️ Tecnologias e Bibliotecas

- **Linguagem:** Python 3.14+
- **Gerenciador de Ambientes:** [Poetry](https://python-poetry.org/)
- **Manipulação de Dados:** `pandas`, `numpy`, `openpyxl`
- **Visualização:** `matplotlib`, `seaborn`
- **Ambiente Interativo:** `jupyter`, `notebook`

---

## 🚀 Como Executar

1. **Clone ou acesse o repositório:**
   ```bash
   cd /home/legion/var/AD/excelinf
   ```

2. **Instale as dependências via Poetry:**
   ```bash
   poetry install
   ```

3. **Opções para executar as análises:**

   * **Pelo PyCharm / IDE:**
     Abra qualquer notebook (`03_analise.ipynb` ou `04_analise.ipynb`) e execute célula a célula selecionando o kernel Poetry.

   * **Pelo navegador local (Jupyter Notebook / JupyterLab):**
     ```bash
     poetry run jupyter notebook
     ```

   * **Execução em lote via linha de comando (Headless):**
     ```bash
     poetry run jupyter nbconvert --to notebook --execute notebooks/03_analise.ipynb --output notebooks/03_analise.ipynb
     ```
