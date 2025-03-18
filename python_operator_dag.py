from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'fayad',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2021, 1, 1),
}

def get_name():
    return "Fayad"

def get_full_name(ti):
    # It is also possible to push multiple values to XCom via keys
    ti.xcom_push(key='first_name', value='Ahmad Al Fayad')
    ti.xcom_push(key='last_name', value='Chowdhury')

def get_age():
    return 26

def greet(ti):
    name = ti.xcom_pull(task_ids='get_name')
    age = ti.xcom_pull(task_ids='get_age')
    print(f"HELLO WORLD IN PYTHON! THIS IS FROM A {age} YEAR OLD {name}")

def greet_full_name(ti):
    first_name = ti.xcom_pull(task_ids='get_full_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_full_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age')
    print(f"HELLO WORLD IN PYTHON! THIS IS FROM A {age} YEAR OLD {first_name} {last_name}")

with DAG(
    dag_id = "python_operator_dag",
    default_args=default_args,
    description="A simple DAG with PythonOperator",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        # op_kwargs = {'name': 'Fayad', 'age': 26}, # This is how to pass parameters; not necessary if pulling from xcoms
    )

    task1_2 = PythonOperator(
        task_id="greet_full_name",
        python_callable=greet_full_name,
    )

    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name,
    )

    task2_2 = PythonOperator(
        task_id="get_full_name",
        python_callable=get_full_name,
    )

    task3 = PythonOperator(
        task_id="get_age",
        python_callable=get_age,
    )

    [task2_2, task3] >> task1_2

    # Even though task1 and task2 are not called in the DAG they are
    # still compiled and run and show up on the DAG with no runs