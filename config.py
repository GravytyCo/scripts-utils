import os
from pathlib import Path

from dotenv import load_dotenv
from gravlibs.keys import GravytyKeys

load_dotenv(dotenv_path=str(os.getenv('SCRIPTS_UTILS') or Path(os.environ['HOME']) / 'conf'/ 'scripts-utils' / 'env'))

keys = GravytyKeys(os.environ['ENVIRONMENT'].lower())

SOURCE_DB_HOST = keys["PROD_DB_HOST"]
SOURCE_DB_NAME = keys["PROD_DB_NAME"]
SOURCE_DB_USER = keys["PROD_DB_USER"]
SOURCE_DB_PASSWORD = keys["PROD_DB_PASSWORD"]
SOURCE_DB_PORT = keys["PROD_DB_PORT"]
