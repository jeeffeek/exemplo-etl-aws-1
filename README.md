# ETL AWS - CSV to S3 Parquet

## Descrição

Projeto de ETL (Extract, Transform, Load) que demonstra o pipeline completo de processamento de dados usando AWS, convertendo arquivos CSV em formato Parquet, armazenando no S3 e consultando via Athena com catálogo Glue.

## Fluxo do Projeto

1. **Extract**: Leitura de arquivo CSV local
2. **Transform**: Conversão para DataFrame com Pandas
3. **Transform**: Conversão para formato Parquet com PyArrow
4. **Load**: Upload para bucket S3
5. **Catalog**: Catalogação no AWS Glue Data Catalog
6. **Query**: Consultas com Amazon Athena

## Arquitetura

```
CSV Local → Pandas DataFrame → PyArrow Table → Parquet → S3 Bucket → Glue Catalog → Athena
```

## Tecnologias

- **Python 3.8+**: Pandas, PyArrow, Boto3
- **AWS Services**: S3, Glue Data Catalog, Athena
- **Formatos**: CSV, Parquet

## Pré-requisitos

- Python 3.8+
- Conta AWS ativa
- Credenciais AWS configuradas (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION)
- Bucket S3 criado
- Database no Glue Data Catalog configurado
- Arquivo `.env` com credenciais AWS

## Como Usar

1. Criar arquivo `.env` com credenciais AWS
2. Preparar arquivo CSV de entrada
3. Executar script Python `csv_to_parquet.py`
4. Arquivo Parquet é gerado localmente e enviado ao S3
5. Configurar tabela no Glue Data Catalog (apontando para o S3)
6. Consultar dados via Athena usando SQL

## Estrutura do Projeto

```
exemplo-aws-1/
├── src/
│   └── csv_to_parquet.py
├── data/
│   └── input/
│       └── movies_and_tv_shows.csv
├── output/
│   └── movies_and_tv_shows.parquet
├── .env
└── README.md
```
