from data_connect import DataConnect
import os, sys
sys.path.append('../../SISTEMA')



data = DataConnect(os.environ.get('DATA_NAME'))

table_user = {
    'name': 'users',
    'columns': ['id INTEGER PRIMARY KEY', 
                'name TEXT',
                'age INTEGER'
                ]
}

user = [('admin', 'admin')]

data._create_table(table_user['name'], table_user['columns'])
data._create_user(['name', 'age'], user, table_user)


