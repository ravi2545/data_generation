# import psycopg2
# from psycopg2 import OperationalError, errorcodes, errors


# class PostgreSQLDataBase:
#     def __init__(self, host, database, user, password):
#         self.host = host
#         self.database = database
#         self.user = user
#         self.password = password
#         # self.port = port
#         self.connection = None
#         self.cursor = None

#     def data_connection(self):
#         try:
#             # Attempt to connect to the database
#             self.connection = psycopg2.connect(
#                 host = self.host,
#                 database = self.database,
#                 user = self.user,
#                 password = self.password
#             )
            
#             self.cursor = self.connection.cursor()
            
#             # Execute your query here
#             self.cursor.execute("SELECT version();")
            
#             db_version = self.cursor.fetchone()
#             print("Connected to:", db_version)

#             return self.connection 
            
#         except OperationalError as e:
#             # Handle errors related to connection problems
#             print(f"The error '{e}' occurred")
#             return None
#         finally:
#             # Ensure the cursor and connection are closed
#             if self.cursor:
#                 self.cursor.close()
#             if self.connection:
#                 self.connection.close()
#                 print("PostgreSQL connection is closed")
    
#     def execute_query(self, query):
#         try:
#             self.cursor.execute(query)
#             self.connection.commit()
#             print("Query executed successfully")
#         except Exception as e:
#             print(f"Error executing query: {e}")
#             self.connection.rollback()



# # # Example usage
# # db = PostgreSQLDataBase('localhost', 'your_database', 'your_user', 'your_password')
# # connection = db.data_connection()

# # if connection:
# #     db.execute_query('SELECT * FROM your_table;')




import psycopg2
from psycopg2 import OperationalError

class PostgreSQLDataBase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        """ Establish a new connection and create a cursor. """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Connection established.")
            return self.cursor
        except OperationalError as e:
            print(f"The error '{e}' occurred")
            self.connection = None
            self.cursor = None

    def close(self):
        """ Close the cursor and connection. """
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
        print("PostgreSQL connection is closed")

    def execute_query(self, query, fetch_results=False):
        """ Execute a query using the existing connection and cursor. """
        if not self.connection or not self.cursor:
            print("Connection or cursor is not initialized.")
            return 'Connection Not Established'
        
        try:
            self.cursor.execute(query)
            if fetch_results:
                results = self.cursor.fetchall()
                return results
            else:
                self.connection.commit()
                # import pdb;pdb.set_trace()
                print("Query executed successfully")
                results = None
                return results
        except Exception as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()

    def insert_data_table(self, table, columns, values):
        """ Insert data into a table. """
        if not self.connection or not self.cursor:
            print("Connection or cursor is not initialized.")
            return 'Connection Not Established'
        
        # Create the SQL query for insertion
        columns_str = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(values[0]))
        insert_query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

        try:
            # Execute the query for each row of data
            self.cursor.executemany(insert_query, values)
            self.connection.commit()
            print("Data inserted successfully")
        except Exception as e:
            print(f"Error inserting data: {e}")
            self.connection.rollback()