import pandas as pd
import polars as pl
from datetime import datetime 
# precisa instalar fastparquet quando vai utilizar o parquet

# pandas 0:0:32
# parquet 0:0:11

ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Obtendo dados parquet')

    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # polars leitura 


    # scan parquet: cria um plano de execucao. nao obtem os dados direto. 
    #print(df_bolsa_familia.head())

    # collect: executa o plano de execucao e traz os dados
    df_bolsa_familia = df_bolsa_familia.collect()
    print(df_bolsa_familia.head())

    fim = datetime.now()
    print(f'tempo total {fim - inicio}')


except Exception as e:
    print(f'Erro ao obter os dados {e}')