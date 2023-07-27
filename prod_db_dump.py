import os
from datetime import date

from config import SOURCE_DB_HOST, SOURCE_DB_NAME, SOURCE_DB_USER, SOURCE_DB_PASSWORD, SOURCE_DB_PORT

def dump_prod_db():
    """
    This functions creates a new dump of the PROD databae and uploads it to an S3 Folder that is shared with 
    our DEV enviorment. The DEV environment can download the dump when needed and use it to restore the
    DEV DB
    """

    dump_file = "./dump_"
    dump_file += date.today().strftime("%Y-%m-%d") + ".sql"

    #create a dump file in the current directory
    command1 = f"export PGPASSWORD='{SOURCE_DB_PASSWORD}';"
    command2 = command1 + f"pg_dump -h {SOURCE_DB_HOST} -p {SOURCE_DB_PORT} -U {SOURCE_DB_USER} -f {dump_file} -d {SOURCE_DB_NAME}"
    os.system(command2)
    #upload the dump file into S3 bucket
    command3 = f"aws s3 cp {dump_file} s3://gravyty/database_backup/{dump_file}"
    os.system(command3)
    #delete file from current directory
    command4 = f"rm -f {dump_file}"
    os.system(command4)

if __name__ == "__main__":
    dump_prod_db()