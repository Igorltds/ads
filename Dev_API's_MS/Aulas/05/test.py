import requests

cep = "01133-000"
url = f"http://viacep.com.br/ws/{cep}/json"
retorno = requests.get(url)
dici = retorno.json()

logradouro = dici['logradouro']
cidade = dici['localidade']
print(f"{logradouro} - {cidade}")
retorno.status_code
