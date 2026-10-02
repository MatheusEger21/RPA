import requests

url = "https://publica.cnpj.ws/cnpj/02697984000137"
response = requests.request("GET", url)
# response = requests.get(url)

print(response.text)