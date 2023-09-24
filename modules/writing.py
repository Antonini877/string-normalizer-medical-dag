from sqlalchemy import create_engine
from dotenv import load_dotenv
from pandas import DataFrame
import os


class ProdWriter:
    def __init__(self):
        load_dotenv()
    
    def write_data(self, df:DataFrame, table_name:str) -> None:
        
        database_url = self.__build_db_url()
        engine = create_engine(database_url)
        
        df.to_sql(table_name, engine, if_exists="append", index=False)

    
    def __build_db_url(self) -> str:
        
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        database = os.getenv('DB_DATABASE')

        return f'postgresql://{username}:{password}@{host}:{port}/{database}'


