import pandas as pd 
import polars as pl
from datetime import datetime
import os 

ENDERECO_DADOS = './../DADOS/'
# pandas 3:59:92
# poulas 3:55:26

try: 
    inicio = datetime.now()
    print('Obtendo os dados de Bolsa Família...')

    df_bolsa_familia = None
    lista_arquivos = [] #lista principal para o processamento

    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    #print(lista_arquivos)

    for arquivo in lista_arquivos:
        print(f'Processando o arquivo{arquivo}')
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso8859-1')
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso8859-1')
        #print(df)

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else: 
           # df_bolsa_familia = pd.concat([df_bolsa_familia, df])
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])


            
        del df
        print(df_bolsa_familia.head())
        print(f'\nArquivo {arquivo} processado com sucesso')

        print(f'Dados concatenados com sucesso!')


    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA')
        .str.replace(',', '.')
        .cast(pl.Float64)
    )


    # salvando em arquivo parquet 
    # instalar biblioteca FASTPARQUET
    print(f'\nSalvando arquivo parquet...')
    df_bolsa_familia.write_parquet('./../DADOS/bolsa_familia.parquet')
    print('Arquivo criado com sucesso')

    

        

    fim = datetime.now()
    print(f'Tempo total{fim - inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')

