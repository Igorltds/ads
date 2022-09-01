#esse arquivo só poderá ser executado após a instalação do flask, que faremos via venv

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")            #especifiquei um caminho (parta da URL)
def ola():                        #defini uma funcao
    return "<h1>Olá Mundo!</h1>"  #que retorna uma string

#construir uma nova funcao, que atende em /ads2b, e devolve "olá, meus caros e caras"
@app.route("/ads2b")
def saudacao():
    return "Olá meus caros e caras!!"

#http://localhost:5000/hires
#--------------------- -----
# todas as urls         nome dado no app.route da funcao 
# desse arquivo
# começam assim
@app.route("/hires")
def saudacao2():
    return "ola hires"

##http://localhost:5000/cumprimentar/hires -> na funcao, a variavel nome = "hires"
##http://localhost:5000/cumprimentar/joao  -> na funcao, a variavel nome = "joao"
@app.route("/cumprimentar/<nome>") #a URL tem um buraco
def saudacao_pessoal(nome):        # e ele corresponde a um 
    return f"Olá {nome}"

#/pudim_magico
#retorna a string ola
import random #random quer dizer "aleatorio" em ingles
              # biblioteca de python pra fazer sorteios
@app.route("/pudim_magico")
def woody():
    respostas = ["com certeza!", "acho dificil",
                 "pode apostar", 
                 "improvavel",
                 "o futuro está obscuro",
                 "voce é fraco!"]
    resposta = random.choice(respostas)
    return resposta

#url /compras, retorna string "compras!"
@app.route("/compras")
def compras():
    # Exemplo de lista em html
    # <ul> abre uma lista nao ordenada
    # <li> Exemplo de item 1</li>
    # <li> Exemplo de item 2</li>
    # </ul> fecha
    # Gerar uma lista dessas, com base numa lista de python
    compras = ["frango", "agua", "sabão", "arroz", "leite", "chocolate"]
    string_html = ""
    string_html += "<ul>"
    for produto in compras:
        string_html += f"<li> {produto} </li>\n"
    string_html += "</ul>"
    return string_html

    '''<ul>
    <li> Exemplo de item 1</li>  <- quebra de linha que aparece no fonte do html, mas nao pro usuário
    <li> Exemplo de item 2</li> <br> <- usuário ve uma quebra de linha, no fonte do html, temos
                                  "<br>"
    </ul>'''
    


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
