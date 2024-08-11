import sys
import pandas as pd
from postgresql_checks import PostgreSQLQueries
from constants import TablesNames

def process_csv_in_chunks(csv_file, table_name, columns, chunk_size=1000):
    """ Read a CSV file in chunks and insert into the database. """
    database = PostgreSQLQueries()
    database.insert_data(csv_file, table_name, columns, chunk_size)
    print('successfully extracted and stored data in the DB')

if __name__ == '__main__':

    file_name = sys.argv[1]
    table_name = sys.argv[2]
    if table_name == TablesNames.to_tables.get(table_name, None):
        tablename = TablesNames.to_tables.get(table_name, None)
        columns = TablesNames.to_colums.get(tablename)

    if tablename:
        process_csv_in_chunks(file_name, table_name, columns)