"""Pacote excel_to_pandas_analytics.

Utilitários para carregamento, limpeza e preparação de dados de vendas.
"""

from excel_to_pandas_analytics.file_base_data import carregar_dados_loja
from excel_to_pandas_analytics.tratamento import (
    aplicar_pipeline_tratamento,
    calcular_faturamento,
    classificar_estoque,
    converter_datas,
    definir_status_estoque,
    ordenar_meses_cronologicamente,
    tratar_dados,
)

__all__ = [
    "carregar_dados_loja",
    "aplicar_pipeline_tratamento",
    "tratar_dados",
    "calcular_faturamento",
    "classificar_estoque",
    "converter_datas",
    "definir_status_estoque",
    "ordenar_meses_cronologicamente",
]
