from datetime import date, datetime

from airflow.models import DAG
from pandas import DataFrame

from astro import sql as aql
from astro.files import File
from astro. sql.table import Table

S3_FILE_PATH = "s3://marcl-astrosdk/orders_data_header.csv"
S3_CONN_ID = "aws_default"
SNOWFLAKE_CONN_ID = "snowflake_default"
SNOWFLAKE_ORDERS = "orders table"
SNOWFLAKE_FILTERED_ORDERS = "filtered table"
SNOWFLAKE_JOINED = "joined_table"
SNOWFLAKE_CUSTOMERS = "customers table"
SNOWFLAKE_REPORTING = "reporting_table"