FROM apache/airflow:2.5.1-python3.9

WORKDIR /opt/airflow



COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

USER root

COPY ./dags /opt/airflow/dags


RUN apt-get update && apt-get install -y \
    wget nano

COPY start.sh /start.sh
RUN chmod +x /start.sh

RUN chmod -R 777 /usr/local/bin

RUN chmod -R 777 /opt/airflow

USER airflow

RUN pip install dbt
RUN pip install dbt-athena-community

#RUN dbt run --project-dir /path/to/new --profiles-dir /path/to/new
#or configure env
#DBT_PROJECT_DIR
#DBT_PROFILES_DIR


ENTRYPOINT ["/bin/bash","/start.sh"]