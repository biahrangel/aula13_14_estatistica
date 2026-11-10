import pandas as pd
import polars as pl # pip install polars
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

# Obtendo Janeiro e Fevereiro
try:
    inicio = datetime.now()
    print('Carregando Dados de Janeiro e Fevereiro. . .')

    lista_arquivos = ['202601_NovoBolsaFamilia.csv', '202602_NovoBolsaFamilia.csv', '202603_NovoBolsaFamilia.csv', '202604_NovoBolsaFamilia.csv', '202605_NovoBolsaFamilia.csv']
    df_bolsa_familia = None

    for arquivo in lista_arquivos:
        df = pl.read_csv(
            ENDERECO_DADOS + arquivo, 
            separator=';', 
            encoding='iso-8859-1'
        )

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else: 
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df # deleta o dataframe temporário

    print(df_bolsa_familia)

    fim = datetime.now()
    print(f'Tempo total: {fim - inicio}')

except Exception as e:
    print(f'Erro ao obter dados - {e}')