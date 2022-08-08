import pendulum
import pandas as pd
from sqlalchemy import create_engine
from airflow import DAG
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
# from airflow.decorators import dag, task
from airflow.models.connection import Connection
from airflow.hooks.base import BaseHook

default_args = {
    'owner': 'Alexander Brezhnev',
    'mysql_conn_id': 'Maria_db',
    'start_date': pendulum.datetime(2022, 5, 17),
    'catchup': False
}

dag = DAG(
    dag_id='test_dag',
    schedule_interval='@daily',
    default_args=default_args
)


def engine():
    test = BaseHook.get_connection('Maria_db')
    print(test)


engine = PythonOperator(task_id='engine', python_callable=engine, dag=dag)

engine
