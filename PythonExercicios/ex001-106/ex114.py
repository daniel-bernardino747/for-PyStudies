import requests

try:
    resposta0 = requests.get('http://pudim.com.br/')
except requests.RequestException:
    print('\033[91mNão foi possível acessar o site.')
else:
    print(f'\033[93mSite acessado com sucesso, seu status de requisição é: {resposta0.status_code}')