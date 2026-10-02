import requests

req = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL').json()

print(req['EURBRL']['bid'])

