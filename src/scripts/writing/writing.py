from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
from airflow.hooks.base_hook import BaseHook

def write() -> None:
    
    data = pd.read_csv("./files/processed_data_med.csv")

    writer = ProdWriter(data, 'normalized_drug_namespaces')

    writer.write_data()


class ProdWriter:
    def __init__(self, df:pd.DataFrame, table_name:str):
        self.__df = data
        self.__table_name = table_name

    def write_data(self) -> None:
        
        database_url = self.__build_db_url()
        engine = create_engine(database_url)
        
        self.__df.to_sql(self.__table_name, engine, if_exists="append", index=False)

    
    def __build_db_url(self) -> str:
        
        connection = BaseHook.get_connection('string-normalizer-medical-dag-connection')
        
        password = connection.password
        host = connection.host
        port = connection.port
        database = connection.schema

        return f'postgresql://{username}:{password}@{host}:{port}/{database}'


