import boto3
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from gravlibs.keys import GravytyKeys

load_dotenv(dotenv_path=str(os.getenv('SCRIPTS_UTILS') or Path(os.environ['HOME']) / 'conf'/ 'scripts-utils' / 'env'))

region_name = "us-east-1"
client = boto3.client("secretsmanager", region_name=region_name)
secret_name = "prod/raise/databases"
keys = json.loads(client.get_secret_value(SecretId=secret_name)["SecretString"])

SOURCE_DB_HOST = keys["PROD_DB_HOST"]
SOURCE_DB_NAME = keys["PROD_DB_NAME"]
SOURCE_DB_USER = keys["PROD_DB_USER"]
SOURCE_DB_PASSWORD = keys["PROD_DB_PASSWORD"]
SOURCE_DB_PORT = keys["PROD_DB_PORT"]
