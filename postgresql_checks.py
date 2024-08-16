import os
from dotenv import load_dotenv

from database.database_connection import PostgreSQLDataBase


load_dotenv()
import pandas as pd


host = os.getenv('DATABASE_HOST')
database = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASS')
# port = os.getenv('DATABASE_PORT')

class PostgreSQLQueries:

    def get_data(self):
        try:
            db = PostgreSQLDataBase(host, database, database_user, password)
            db.connect()
            # Execute a query
            data = db.execute_query('SELECT * FROM data_extraction.store_random_data;', fetch_results=True)
            # Close the connection
            db.close()
            return data
        except Exception as error:
            return str(error)
    
    def insert_data(self, csv_file, table_name, columns, chunk_size):
        try:
            db = PostgreSQLDataBase(host, database, database_user, password)
            db.connect()

            # Execute a query
            for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
                values = chunk.values.tolist()
                data = db.insert_data_table(table_name, columns, values)
                print(f"Inserted chunk of size {len(values)}")

            # Close the connection
            db.close()
            return data
        except Exception as error:
            return str(error)