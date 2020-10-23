import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
#from queue import Empty

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Default Path
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    #path = "/Users/apple/Desktop/airflow/store_sales_project2/logs/S3_dag_test/data_collection"

    # Initialize logging event 
    event_handler = LoggingEventHandler()

    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()