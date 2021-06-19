#esse arquivo só poderá ser executado após a instalação do flask, que faremos via venv

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def ola():
    return "<h1>Olá Mundo!</h1>"

@app.route("/ads2b")
def saudacao():
    return "olá meus preços elevados!!"

@app.route("/comprimentar/<nome>")
def suadação2(nome):
    return f"ola {nome}!"

import random
@app.route("/maoe")
def hehe():
    respostas = ["sim", 'não', 'tavez']
    return random.choice(respostas)

@app.route("/compras")
def compras():
    compras= ["arroz", "feijão", "batata", "vento"]
    string_html = ""
    string_html += "<ul>\n"
    for produto in compras:
        string_html += f"<li> {produto} </li>\n"
    string_html += "</ul>"
    return string_html
#<ul> lista não ordenada
#<li>
@app.route("/")
def main_page():
    return "experimente acessar a url /home"

@app.route("/template")
def template():
    return render_template("index.html")

app.run(debug=True)
if __name__ == '__main__':     #IF esse arquivo foi rodado direto,
                               # não foi chamado como biblioteca
   app.run(host = 'localhost', port = 5002, debug = True)
                               #suba um servidor, na porta 5002,
                               #configuração de debug
                               #debug: salvar dá reload
