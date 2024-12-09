FROM apache/airflow:2.9.0-python3.10

COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt

USER root

RUN chmod +x ./start.sh && \
   apt-get update && apt-get install -y \
   wget nano

USER airflow