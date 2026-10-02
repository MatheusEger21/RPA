import requests
import pandas as pd

ceps = open('ceps.txt','r').read().splitlines()
dados = []

for cep in ceps:

    req = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    dados.append(req)

df = pd.DataFrame(dados)
df.to_csv('ceps.csv')
print(df)
# print(request.text)

