FROM apache/airflow:2.9.3

COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt

USER root

RUN apt-get update && apt-get install -y \
    wget nano

USER airflow