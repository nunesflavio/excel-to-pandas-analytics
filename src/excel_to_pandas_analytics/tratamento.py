from typing import List, Optional
import pandas as pd

# Ordem cronológica padrão dos meses em português
MESES_CRONOLOGICOS: List[str] = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]


def converter_datas(
    df: pd.DataFrame, coluna: str = "Data", formato: str = "%d/%m/%Y") -> pd.DataFrame:
    """Converte a coluna de data especificada para o tipo datetime."""
    if coluna in df.columns:
        df[coluna] = pd.to_datetime(df[coluna], format=formato)
    return df


def calcular_faturamento(
    df: pd.DataFrame,
    coluna_preco: str = "Preço Unitário (R$)",
    coluna_qtd: str = "Qtd Vendida",
    coluna_faturamento: str = "Faturamento Total (R$)",
) -> pd.DataFrame:
    """Calcula a coluna de faturamento total a partir do preço e quantidade vendida."""
    if coluna_preco in df.columns and coluna_qtd in df.columns:
        df[coluna_faturamento] = df[coluna_preco] * df[coluna_qtd]
    return df


def definir_status_estoque(estoque: float | int) -> str:
    """Classifica o status do item com base na quantidade em estoque."""
    if estoque < 10:
        return "Crítico"
    elif estoque < 25:
        return "Baixo"
    return "Normal"


def classificar_estoque(
    df: pd.DataFrame,
    coluna_estoque: str = "Estoque Atual",
    coluna_status: str = "Status Estoque",
) -> pd.DataFrame:
    """Aplica a regra de classificação de estoque ao DataFrame."""
    if coluna_estoque in df.columns:
        df[coluna_status] = df[coluna_estoque].apply(definir_status_estoque)
    return df


def ordenar_meses_cronologicamente(
    df: pd.DataFrame,
    coluna_mes: str = "Mês",
    meses_ordenados: Optional[List[str]] = None,
) -> pd.DataFrame:
    """Define a coluna de mês como categórica ordenada para evitar ordenação alfabética."""
    if coluna_mes in df.columns:
        categorias = meses_ordenados or MESES_CRONOLOGICOS
        df[coluna_mes] = pd.Categorical(df[coluna_mes], categories=categorias, ordered=True)
    return df


def aplicar_pipeline_tratamento(
    df: pd.DataFrame,
    ordenar_meses: bool = True,
) -> pd.DataFrame:
    """Aplica o pipeline completo de limpeza e tratamento dos dados.

    Executa:
    1. Cópia defensiva do DataFrame.
    2. Conversão da coluna 'Data' para datetime.
    3. Recálculo da coluna 'Faturamento Total (R$)'.
    4. Classificação da coluna 'Status Estoque'.
    5. Opcionalmente, ordenação cronológica da coluna 'Mês'.
    """
    df_tratado = df.copy()
    df_tratado = converter_datas(df_tratado)
    df_tratado = calcular_faturamento(df_tratado)
    df_tratado = classificar_estoque(df_tratado)

    if ordenar_meses:
        df_tratado = ordenar_meses_cronologicamente(df_tratado)

    return df_tratado


# Alias para conveniência
tratar_dados = aplicar_pipeline_tratamento
