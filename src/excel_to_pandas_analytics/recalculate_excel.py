from typing import Optional
import pandas as pd
from excel_to_pandas_analytics.file_base_data import carregar_dados_loja
from excel_to_pandas_analytics.tratamento import calcular_faturamento


def recalculate_excel_to_pandas(df: Optional[pd.DataFrame] = None) -> pd.Series:
    """Recálculo seguro das colunas (substituindo fórmulas vazias do Excel).

    Faturamento Total = Preço Unitário * Quantidade Vendida
    """
    alvo = df if df is not None else carregar_dados_loja()
    calcular_faturamento(alvo)
    return alvo["Faturamento Total (R$)"]
