import sqlite3, os


class DataConnect():
    def __init__(self, data_name: str):
        self.connect = sqlite3.connect(data_name)
        self.cursor = self.connect.cursor()
        
    def _create_table(self, name_table: str, columns: list):
        create_query = f"CREATE TABLE IF NOT EXISTS {name_table} ({', '.join(columns)})"

        self.cursor.execute(create_query)

    def _create_user(self, name_columns: list, values: list, table: str):
        create_query = f"INSERT INTO {table} ({', '.join(name_columns),}), VALUES ({', '.join(['?']*len(values))})"

        self.cursor.execute(create_query, values)
    
        self.connect.commit()
        self.select_table(table)

    def select_table(self, table: str):
        self.cursor.execute(f'SELECT * FROM {table}')
        print(self.cursor.fetchall())

#data = DataConnect(os.environ.get["DATA_NAME"])


