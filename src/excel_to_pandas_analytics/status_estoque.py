from typing import Optional
import pandas as pd
from excel_to_pandas_analytics.file_base_data import carregar_dados_loja
from excel_to_pandas_analytics.tratamento import classificar_estoque, definir_status_estoque


def recalcular_estoque(df: Optional[pd.DataFrame] = None) -> pd.Series:
    """Aplica a classificação de status de estoque (Crítico, Baixo, Normal)."""
    alvo = df if df is not None else carregar_dados_loja()
    classificar_estoque(alvo)
    return alvo["Status Estoque"]
