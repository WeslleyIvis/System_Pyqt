import sqlite3

class DataConnect:
    def __init__(self):
        self.connect = sqlite3.connect('database')
        self.cursor = self.connect.cursor()

    def create_user(self, name: str, age: int):
        self.cursor.execute(f'INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (name, age))
        self.connect.commit()
