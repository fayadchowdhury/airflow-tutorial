from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'fayad',
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

@dag(
        default_args=default_args,
        dag_id='catchup_backfill_v1',
        description='A simple DAG to test catchup and backfill',
        schedule_interval=timedelta(minutes=10), # Just messing with the scheduler here
        # Also possible to do CRON expressions for scheduler
        # schedule_interval='0 0 * * *', # Run the DAG at midnight every day
        # Get CRON expression from crontab.guru
        start_date=datetime(2025, 3, 17),
        catchup=True, # This is the default behaviour; this catches up on runs from the start date to the current date
        # Another way to do this is to use backfill from the airflow instance like so
        # airflow dags backfill -s <start-date> <dag-id>
        # This will backfill all the runs from the start date to the current date and works with catchup=False too
)
def catchup_backfill():
    @task()
    def hello_world():
        print("HELLO WORLD!")

    hello_world()

dag = catchup_backfill()