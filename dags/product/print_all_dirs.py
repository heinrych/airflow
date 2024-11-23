import logging
from airflow import DAG
from pendulum import datetime
from airflow.operators.bash import BashOperator

logger = logging.getLogger("airflow.task")

with DAG(
    "dbt_find_all_dirs_dag",
    start_date=datetime(2020, 12, 23),
    description="DAG para encontrar todos os diretórios e arquivos em busca do dbt",
    schedule_interval=None,
    catchup=False,
) as dag:

    # Encontrar todos os diretórios e arquivos a partir do diretório raiz '/'
    find_all_dirs = BashOperator(
        task_id="find_all_dirs",
        bash_command="echo 'Buscando todos os diretórios e arquivos a partir de /' && find / -type d -or -type f",
    )

    find_all_dirs
