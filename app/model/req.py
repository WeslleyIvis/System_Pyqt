import requests as r

url = 'http://127.0.0.1:5000/login'  

dados = {
    'nome': 'Usuário',
    'idade': 30,
    'email': 'usuario@example.com'
}

headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json'
}

response = r.post(url, json=dados, headers=headers)

print(response.status_code)
if response.status_code == 200:
    print('Dados enviados com sucesso!')
else:
    print('Falha ao enviar os dados.')
