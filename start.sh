#!/bin/bash
airflow standalone

if [ -f .env ]; then
    export $(cat .env | xargs)
fi
exec "$@"
