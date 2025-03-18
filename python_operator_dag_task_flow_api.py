from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'fayad',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2021, 1, 1),
}

# This is a simpelr, more modern way to create a DAG with TaskFlow API
@dag(
    dag_id = "python_operator_dag_task_flow_api",
    default_args=default_args,
    description="A simple DAG with PythonOperator and TaskFlow API",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
)
def hello_world_dag():

    # All tasks have to be decorated with @task decorator
    @task(multiple_outputs=True) # Possible to produce multiple outputs with multiple_outputs=True to return a dictionary
    def get_name():
        return {
            "first_name" :"Ahmad Al Fayad",
            "last_name": "Chowdhury"
        }
    
    @task()
    def get_age():
        return 26
    
    @task()
    def greet(first_name, last_name, age):
        print(f"HELLO WORLD IN PYTHON! THIS IS FROM A {age} YEAR OLD {first_name} {last_name}")

    name_dict = get_name()
    age = get_age()
    first_name = name_dict["first_name"]
    last_name = name_dict["last_name"]
    greet(first_name, last_name, age)

dag = hello_world_dag()