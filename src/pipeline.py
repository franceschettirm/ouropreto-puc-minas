import boto3

s3 = boto3.client("s3", region_name="us-east-1")
lambda_op = boto3.client("lambda", region_name="us-east-1")

INPUT_BUCKET_COMBUSTIVEIS = "puc-dados-combustiveis"
INPUT_BUCKET_DADOS_MACRO = "puc-dados-macro"

FOLDER_COMBUSTIVEIS = "db-combustiveis-ingestion/"
FOLDER_DADOS_MACRO = "db-macrodata-ingestion/"

DATA_PATH = "/Users/rafaelmacedo/Documents/Code/ouropreto-puc-minas/data/"

DADOS_COMBUSTIVEIS = "tb_preco_combustiveis.csv"
DADOS_MACRO = "tb_dados_macro.csv"

try:
    s3.upload_file(
        DATA_PATH + DADOS_COMBUSTIVEIS,
        INPUT_BUCKET_COMBUSTIVEIS,
        FOLDER_COMBUSTIVEIS + DADOS_COMBUSTIVEIS,
    )

    s3.upload_file(
        DATA_PATH + DADOS_MACRO,
        INPUT_BUCKET_DADOS_MACRO,
        FOLDER_DADOS_MACRO + DADOS_MACRO,
    )
except Exception as e:
    print(f"Failed to process due to error: {e}")

stepfunc = boto3.client("stepfunction", region_name="us-east-1")

response = stepfunc.start_execution(
    stateMachineArn="arn:aws:states:us-east-1:253490758634:stateMachine:PucProcessingPipeline",
)
