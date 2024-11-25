from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from cosmos import DbtTaskGroup, ProfileConfig, ProjectConfig
from pathlib import Path

default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 1, 1),
    "retries": 1,
}

DBT_PATH = "/opt/airflow/dbt"
DBT_PROFILE = "dbt_athena_iceberg" ## nome do profile definido no profile.yml
DBT_TARGETS = "dev"
TAGS = "daily"

# Profile enviroment
profile_config = ProfileConfig(
    profile_name=DBT_PROFILE,
    target_name=DBT_TARGETS,
    profiles_yml_filepath=Path(f"{DBT_PATH}/profiles.yml"),
)

# Models dbt
project_config = ProjectConfig(
    dbt_project_path=DBT_PATH,
    models_relative_path="models"
)

dag = DAG(
    "dag_dbt_athena_iceberg",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

start_dag = EmptyOperator(task_id="start_dag", dag=dag)

dbt_running_models = DbtTaskGroup(
    group_id="dbt_running_models",
    project_config=project_config,
    profile_config=profile_config,
    dbt_args={"--select": TAGS},
    default_args={"retries": 2},
    dag=dag,
)

end_dag = EmptyOperator(task_id="end_dag", dag=dag)

start_dag >> dbt_running_models >> end_dag