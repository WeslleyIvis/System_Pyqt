from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
var_1 = os.getenv('VARIAVEL_1')
var_2 = os.getenv('VARIAVEL_2')

# Exibe os valores das variáveis
print(var_1)  # Saída: Valor1
print(var_2)  # Saída: Valor2

table_user = {
    'name': 'users',
    'columns': ['id INTEGER PRIMARY KEY', 
                'name TEXT',
                'age INTEGER'
                ]
}

print(os.getenv('DATA_NAME'))

print(table_user['name'])
print(table_user['columns'])
print(', '.join(table_user['columns']))
print(', '.join(['?']*len(table_user['columns'])))



for column in table_user['columns']:
    print(column)