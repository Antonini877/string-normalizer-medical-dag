import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

sys.path.append('/opt/airflow/scripts')

from feature_extraction.preprocessing import preprocess
from writing.writing import write


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 3,
}

with DAG(
    'medical_nomenclature_normalizer',
    default_args=default_args,
    description='Create info columns by preprocessing the raw text',
    schedule_interval='0 9 * * *',  
    start_date=days_ago(1),
    catchup=False,
) as dag:

    preprocessor_task = PythonOperator(
        task_id='process_text',
        python_callable=preprocess,
    )

    writing_task = PythonOperator(
        task_id='write_to_database',
        python_callable=write,
    )

    preprocessor_task >> writing_task
