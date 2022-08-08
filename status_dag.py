import pendulum
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {
    'owner': 'Alexander Brezhnev',
    'mysql_conn_id': 'Maria_db',
    'start_date': pendulum.datetime(2022, 5, 17),
    'catchup': False
}

dag = DAG(
    dag_id='status_dag',
    schedule_interval='@daily',
    default_args=default_args
)

all_users_sql = MySqlOperator(task_id='all_users_sql', sql='/SQL/All_users.sql', dag=dag)
super_sql = MySqlOperator(task_id='super_sql', sql='/SQL/Super.sql', dag=dag)
total_calls_sql = MySqlOperator(task_id='total_calls_sql', sql='/SQL/Total_calls.sql', dag=dag)
total_calls_31d_sql = MySqlOperator(task_id='total_calls_31d_sql', sql='/SQL/Total_calls_31d.sql', dag=dag)
test_to_csv = MySqlOperator(task_id='test_mysql_to_csv', sql='/SQL/Test_mysql_to_csv.sql', dag=dag)

all_users_sql
super_sql
total_calls_sql
total_calls_31d_sql
test_to_csv
