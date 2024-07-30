import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

sys.path.append('/opt/airflow/scripts')

from feature_extraction.preprocessing import preprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'medical_nomenclature_normalizer',
    default_args=default_args,
    description='Create info columns by preprocessing the raw text',
    schedule_interval='* * * * *',  # Run every minute
    start_date=days_ago(1),
    catchup=False,
) as dag:

    preprocessor_task = PythonOperator(
        task_id='process_text',
        python_callable=preprocess,
    )

    preprocessor_task
