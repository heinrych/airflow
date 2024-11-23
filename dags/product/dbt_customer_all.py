"""
A basic dbt DAG that shows how to run dbt commands via the BashOperator

Follows the standard dbt seed, run, and test pattern.
"""


import os
import logging
from airflow import DAG
from pendulum import datetime
from dotenv import load_dotenv
from airflow.operators.bash import BashOperator

load_dotenv()

logger = logging.getLogger("airflow.task")

DBT_DIR = "/opt/***/dbt"

print(f"Variáveis: DBT_REDSHIFT_USER={os.getenv('DBT_REDSHIFT_USER')}, DBT_REDSHIFT_PASSWORD={os.getenv('DBT_REDSHIFT_PASSWORD')}, DBT_REDSHIFT_SCHEMA={os.getenv('DBT_REDSHIFT_SCHEMA')}, DBT_REDSHIFT_PORT={os.getenv('DBT_REDSHIFT_PORT')}")

logger.debug(f"Variáveis: DBT_REDSHIFT_USER={os.getenv('DBT_REDSHIFT_USER')}, DBT_REDSHIFT_PASSWORD={os.getenv('DBT_REDSHIFT_PASSWORD')}, DBT_REDSHIFT_SCHEMA={os.getenv('DBT_REDSHIFT_SCHEMA')}, DBT_REDSHIFT_PORT={os.getenv('DBT_REDSHIFT_PORT')}")

with DAG(
    "dbt_customer_users_all",
    start_date=datetime(2020, 12, 23),
    description="A sample Airflow DAG to invoke dbt runs using a BashOperator",
    schedule_interval=None,
    catchup=False,
    default_args={
        "env": {
            "DBT_REDSHIFT_USER": os.getenv('DBT_REDSHIFT_USER'),
            "DBT_REDSHIFT_PASSWORD": os.getenv("DBT_REDSHIFT_PASSWORD"),
            "DBT_REDSHIFT_HOST": os.getenv("DBT_REDSHIFT_HOST"),
            "DBT_REDSHIFT_SCHEMA": os.getenv("DBT_REDSHIFT_SCHEMA"),
            "DBT_REDSHIFT_PORT": os.getenv("DBT_REDSHIFT_PORT"),
        }
    },
) as dag:
    # This task loads the CSV files from dbt/data into the local postgres database for the purpose of this demo.
    # In practice, we'd usually expect the data to have already been loaded to the database.
    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"/home/airflow/.local/bin/dbt seed --profiles-dir {DBT_DIR} --project-dir {DBT_DIR}",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"/home/airflow/.local/bin/dbt run --profiles-dir {DBT_DIR} --project-dir {DBT_DIR}",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"/home/airflow/.local/bin/dbt test --profiles-dir {DBT_DIR} --project-dir {DBT_DIR}",
    )

    dbt_seed >> dbt_run >> dbt_test