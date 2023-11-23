import sqlite3

class DataConnect():
    def __init__(self):
        self.connect = sqlite3.connect('database')
        self.cursor = self.connect.cursor()
        
    def create_user(self, name: str, age: int):
        self.cursor.execute(f'INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (name, age))
        self.connect.commit()
        # self.connect.close()
        self.select_table('usuarios')

    def select_table(self, table: str):
        self.cursor.execute(f'SELECT * FROM {table}')
        print(self.cursor.fetchall())

data = DataConnect()
# data.create_user('Maria', 19)
# data.select_table('usuarios')


