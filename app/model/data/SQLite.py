import sqlite3


# Create DB
connect = sqlite3.connect('database')

# Cria um cursos para utilizar comandos SQL
cursor = connect.cursor()

# Cria uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    idade INTEGER
                 )''')

data_users = [('Weslley', 24),
              ('Anna', 22),
              ('Carlin', 38)]

# Inserindo dados
cursor.executemany('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', data_users)

# Salva alterações
connect.commit()


# Seleciona todos os dados da tabela
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())


connect.close()