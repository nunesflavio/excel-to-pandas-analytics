from pathlib import Path
from typing import Optional, Union
import pandas as pd

# Caminho base do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]


def carregar_dados_loja(
    caminho_arquivo: Optional[Union[str, Path]] = None,
    sheet_name: str = "Dados Detalhados",
) -> pd.DataFrame:
    """Carrega a base de dados da loja de informática.

    Procura o arquivo por padrão em data/raw a partir da raiz do projeto,
    com fallback para caminho relativo se executado dentro da pasta notebooks.
    """
    if caminho_arquivo is not None:
        caminho = Path(caminho_arquivo)
    else:
        caminho_padrao = ROOT_DIR / "data" / "raw" / "loja_informatica_2026.xlsx"
        if caminho_padrao.exists():
            caminho = caminho_padrao
        else:
            # Fallback para execução direta em subdiretórios
            caminho = Path("../data/raw/loja_informatica_2026.xlsx")

    return pd.read_excel(caminho, sheet_name=sheet_name)
