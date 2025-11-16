# -------------------------------- #
# Importação das bibliotecas
# -------------------------------- #
import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq
import boto3
import logging
import dotenv

dotenv.load_dotenv()  # carrega .env

logging.basicConfig(level=logging.INFO)

# -------------------------------- #
# Processamento do arquivo CSV
# -------------------------------- #
def process_csv(csv_file: str, output_dir: str, bucket_name: str, s3_key: str) -> None:
    os.makedirs(output_dir, exist_ok=True) # Cria o diretório de saída se não existir
    
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                      region_name=os.getenv('AWS_DEFAULT_REGION')
                      )
    
    df = pd.read_csv(csv_file)

    parquet_file = os.path.join(output_dir, "movies_and_tv_shows.parquet")
    table = pa.Table.from_pandas(df)

    # Conversão para Parquet
    pq.write_table(table, parquet_file)
    
    # Upload para o S3
    s3.upload_file(parquet_file, bucket_name, s3_key)