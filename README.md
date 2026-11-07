# 📊 Excel to Pandas Analytics - Análise de Dados com Python & Pandas

Projeto prático de estudos focado na exploração, tratamento e análise de dados transacionais de vendas no varejo de informática (fictício). O objetivo é demonstrar a transição entre manipulação de planilhas Excel e automação analítica com Python e a biblioteca **Pandas**.

---

## 🎯 Objetivos de Aprendizado

- **Leitura & Validação:** Carregamento de planilhas Excel estruturadas com múltiplas abas via `pandas` e `openpyxl`.
- **Limpeza & Sanitização:** Conversão de formatos de datas (`datetime64`), tratamento de nulos e recálculo seguro de métricas.
- **Engenharia de Features:** Aplicação de regras de negócio customizadas via funções e `.apply()` (ex.: classificação do status de estoque).
- **Agregações & Resumos:** Uso de `groupby` e `.agg()` para consolidações mensais e análises temporais.
- **Raciocínio Analítico & Métricas:** Cálculo aprofundado de indicadores de negócio como **Ticket Médio**, diferenciando cálculos ingênuos de agregações por transação única (`nunique` e `groupby`).

---

## 🗂️ Estrutura do Projeto

```text
excel-to-pandas-analytics/
├── data/
│   ├── raw/
│   │   └── loja_informatica_2026.xlsx   # Dados brutos (abas: 'Dados Detalhados' e 'Resumo Mensal')
│   └── processed/
│       └── loja_informatica_tratada.xlsx# Dados limpos e enriquecidos exportados via script
├── notebooks/
│   ├── 01_analise.ipynb                # Exploração inicial (head, info, describe)
│   ├── 02_analise.ipynb                # Limpeza, tipagem de datas, regras de estoque e exportação
│   ├── 03_analise.ipynb                # Agregações por período (faturamento e volume por mês)
│   └── 04_analise.ipynb                # Métricas de negócio: Ticket Médio e validação por pedido
├── src/
│   └── excel-to-pandas-analytics/      # Módulos Python reutilizáveis do pacote
├── pyproject.toml                      # Gerenciamento de dependências via Poetry
└── README.md                           # Documentação do projeto
```

---

## 🔬 OBSERVAÇÂO

As planilhas estão no repositório porque os dados são fictícios, somente para estudo.

---

## 🔬 Trilha dos Notebooks

1. **`01_analise.ipynb` - Exploração Inicial:**
   - Carga da aba `Dados Detalhados`.
   - Inspeção de tipos (`df.info()`), valores nulos e distribuição estatística inicial (`df.describe()`).

2. **`02_analise.ipynb` - Tratamento e Pipeline:**
   - Conversão explícita de formato de data brasileiro (`%d/%m/%Y`).
   - Recálculo programático de `Faturamento Total (R$)` = `Preço Unitário` $\times$ `Qtd Vendida`.
   - Criação da coluna categórica `Status Estoque` (*Crítico* < 10, *Baixo* < 25, *Normal* $\ge$ 25).
   - Exportação para a camada de dados tratados em `data/processed/`.

3. **`03_analise.ipynb` - Agregações Temporais:**
   - Agrupamento mensal (`groupby('Mês')`).
   - Totalização de receita, volume de itens e contagem de transações.

4. **`04_analise.ipynb` - Métricas Analíticas & Boas Práticas:**
   - Cálculo do **Ticket Médio por Transação**.
   - Comparativo metodológico: `.sum() / len()` vs `.mean()` vs agrupamento por pedido real (`.nunique()` e `.groupby()`).
   - Simulação analítica com carrinhos com múltiplos itens, demonstrando a prevenção de distorções estatísticas.

---

## 🛠️ Tecnologias e Bibliotecas

- **Linguagem:** Python 3.14+
- **Gerenciador de Ambientes:** [Poetry](https://python-poetry.org/)
- **Manipulação de Dados:** `pandas`, `numpy`, `openpyxl`
- **Visualização (Ambiente pronto):** `matplotlib`, `seaborn`
- **Ambiente Interativo:** `jupyter`, `notebook`

---

## 🚀 Como Executar

1. **Clone ou acesse o repositório:**
   ```bash
   cd /caminho/excel-to-pandas-analytics
   ```

2. **Instale as dependências via Poetry:**
   ```bash
   poetry install
   ```

3. **Inicie o servidor do Jupyter Notebook:**
   ```bash
   poetry run jupyter notebook
   ```

4. Acesse a pasta `notebooks/` e execute as análises sequencialmente (de `01` a `04`).
