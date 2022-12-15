import os
from spark.session import Session
from utils.renamer_csv import rename_csv
from mongo.db_handler import init_db

if __name__ == "__main__":

    init_db()

    SPARK_RESULT_DIR = os.environ['SPARK_RESULT_DIR']
    if not os.path.exists(SPARK_RESULT_DIR):
        os.makedirs(SPARK_RESULT_DIR)
        session = Session()
        session.start()
    else:
        print('Encountered existing spark result directory, skip process step')

    SPARK_PRETTY_OUT_DIR = os.environ['SPARK_PRETTY_OUT_DIR']
    if not os.path.exists(SPARK_PRETTY_OUT_DIR):
        rename_csv()

    os.system('python3 -m streamlit run ./python/web_app/Введение.py')
