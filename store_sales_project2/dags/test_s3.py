from airflow import DAG
from airflow.operators import DummyOperator, PythonOperator
from datetime import datetime, timedelta
import airflow.hooks.S3_hook
from helper import t1, t2, t3, t4
#from helper import upload_file_to_S3_with_hook

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 9, 24),
    'retry_delay': timedelta(seconds=5)
}
# Using the context manager alllows you not to duplicate the dag parameter in each operator
with DAG('S3_dag_test', default_args=default_args, schedule_interval='@once') as dag:

    
    t1 = PythonOperator(
    task_id = "data_collection",
    python_callable = t1,
    dag=dag
        )

    t2 = PythonOperator(
    task_id = "downlaod_from_s3",
    python_callable = t2,
    dag=dag
        )

    t3 = PythonOperator(
    task_id = "transform",
    python_callable = t3,
    dag=dag
        )

    t4 = PythonOperator(
    task_id = "upload_to_salesforce1",
    python_callable = t4,
    dag=dag
        )

    t1 >> t2 >>t3 >> t4
    
    
    #t4
    '''
    start_task = DummyOperator(
            task_id='dummy_start'
    )

    hook = PythonOperator(
    task_id = "hook",
    python_callable = upload_file_to_S3_with_hook,
    dag=dag
        )

    
    download_to_S3_task = PythonOperator(
    task_id='download',
    python_callable=download,
    dag=dag)



    
    upload_to_S3_task = PythonOperator(
    task_id='upload_to_S3',
    python_callable=upload_file_to_S3_with_hook,
    op_kwargs={
        #'filename': 'path/to/my_file.csv',
        'key': 'integration/SharedDataRequest/DHCS-FAS-002/atlasmap-mapping.adm',
        'bucket_name': 'xaqua-udp',
    },
    dag=dag)

    # Use arrows to set dependencies between tasks'''
#start_task >> 
#upload_to_S3_task
#hook
#download_to_S3_task



