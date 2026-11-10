import pandas as pd
import polars as pl # pip install polars
from datetime import datetime
ENDERECO_DADOS = './../DADOS/' #.. para sair da pasta atual

# Obtendo dados

try:
    inicio = datetime.now()
    print('Carregando Dados . . .')

    # 0:00:13.99
    # df_janeiro = pd.read_csv(
    #     ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', 
    #     sep=';', 
    #     encoding='iso-8859-1'
    # )

    # POLARS
    df_janeiro = pl.read_csv(
        ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', 
        separator=';', 
        encoding='iso-8859-1'
        )
    
    print(df_janeiro.head())
    # print(df_janeiro.columns.to_list()) # todas as colunas - Pandas
    # print(df_janeiro.columns) # todas as colunas - Polars

    fim = datetime.now()
    print(f'Tempo total: {fim - inicio}')

except Exception as e:
    print(f'Erro ao obter dados - {e}')
