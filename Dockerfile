FROM apache/airflow:2.9.0-python3.9

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

ENTRYPOINT ["/bin/bash","/start.sh"]