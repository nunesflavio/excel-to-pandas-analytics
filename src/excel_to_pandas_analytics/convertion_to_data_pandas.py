from typing import Optional, Tuple
import pandas as pd
from excel_to_pandas_analytics.file_base_data import carregar_dados_loja
from excel_to_pandas_analytics.tratamento import converter_datas


def convertion_data(df: Optional[pd.DataFrame] = None) -> Tuple[str, str]:
    """Conversão segura da coluna de Data para datetime."""
    alvo = df if df is not None else carregar_dados_loja()
    converter_datas(alvo)
    return "Tipo da coluna Data após conversão:", str(alvo["Data"].dtype)
