import requests
from flask import Flask

#usa a biblioteca requests para abrir uma conexao com o viacep
def get_dicionario(cep):
     url = f"https://viacep.com.br/ws/{cep}/json/"
     response = requests.get(url)
     if response.status_code != 200:
         pass #TODO, lançar um erro
     dicionario_retornado = response.json()
     return dicionario_retornado

#rodando cep_to_bairro("01136000"), devemos receber "barra funda"

app = Flask(__name__) #gerar um objeto chamado app
#uma burocracia que a gente faz sempre

#o meu servidor tem uma URL bairro
# eu firefox -> meu servidor -> viacep
#            <-               <-
@app.route("/cep/<cep>")
def bairro(cep):
    Dicionario_retornado = get_dicionario(cep)
    return {"cep": Dicionario_retornado["cep"],
            "logradouro": Dicionario_retornado['logradouro'],
            "complemento": Dicionario_retornado['complemento'],
            "bairro": Dicionario_retornado['bairro'],
            "localidade": Dicionario_retornado['localidade'],
            "uf": Dicionario_retornado['uf'],
            "ibge": Dicionario_retornado['ibge'],
            "gia": Dicionario_retornado['gia'],
            "ddd": Dicionario_retornado['ddd'],
            "siafi": Dicionario_retornado['siafi']}
    #TODO tratar o erro, devolvendo um dicionario mais informativo para o usuario, e um status code 500

bairros_atende = ["Barra Funda", "Lapa", "Parque Residencial da Lapa", "Vila Invernada"]

#o meu servidor tem uma URL bairro
# eu firefox -> meu servidor -> viacep
#            <-               <-
@app.route("/atende/<cep>")
def atende(cep):
    bairro = get_dicionario["bairro"](cep)
    return {"atende": bairro in bairros_atende, "status": "ok"}

#adiciona um bairro, pra eu nao precisar ficar mexendo no codigo pra adicionar
#bairros. Mas isso eu vou mostrar mais pra frente (se quiser brincar com isso
# aprenda primeiro como funciona a biblioteca requests)
@app.route("/bairros/<nome>", methods=["PUT"])
def add_bairro(nome):
    if nome not in bairros_atende:
        bairros_atende.append(nome)
        return {"bairro_adicionado": nome, "status": "ok"}
    #TODO: adicionar tratamento de erro se o bairro já está na lista. Status code 400.

#TODO adicionar remoção de bairro

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)