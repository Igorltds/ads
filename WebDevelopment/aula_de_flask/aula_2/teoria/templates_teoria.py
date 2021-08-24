from flask import Flask, request, render_template

app = Flask(__name__)

#Já vimos na aula passada como criar rotas do flask

@app.route("/")
def hello():
    return '''essa é a rota principal. Procure as demais rotas no arquivo py'''

#uma rota é uma associação entre uma URL e uma função
#a função retorna a string que o navegador vai baixar, 
# quando alguém navegar até ela

@app.route("/california")
def estrada():
    return '''<h1>Hotel California</h1>
    <p>On a dark desert highway<br>
    Cool wind in my hair<br>
    Warm smell of colitas<br>
    Rising up through the air</p>
    <p>
    There she stood in the doorway<br>
    I heard the Mission bell<br>
    And I was thinking to myself<br>
    This could be heaven or this could be hell</p>
    '''

#A propósito, ficou feio esse html no navegador, não?

# Voltando, podemos sempre montar o html a partir do código python

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

#Mas isso pode ficar confuso...
#Seria MUITO melhor separar o código html do código python
#Para isso, usaremos templates: uma "html com variáveis"
# que vai ser preenchido através do python


@app.route("/compras_template")
def compras_template():
    compras = ["frango", "agua", "sabão", "arroz", "leite", "chocolate"]
    return render_template("compras.html",lista_compras = compras)

#onde eu acho o arquivo compras.html?? 
# o flask automaticamente buscou o arquivo na pasta templates


#templates são uma idéia fundamental: nos ajuda a separar o código HTML
#do código python, deixando os dois mais fáceis de ler e de manter

#além do for, exemplificado acima, tb podemos colocar um IF

@app.route("/compras_template_if")
def compras_template_if():
    compras = ["frango", "agua", "sabão", "arroz", "leite", "chocolate"]
    return render_template("compras_com_if.html",lista_compras = compras)

#Para termos um código ainda mais limpo e elegante, as vezes queremos
#uma template "basica" e templates especificas.
# Veja, por exemplo, as URLs:
# * https://github.com/pallets
# * https://github.com/pallets/flask/
# * https://github.com/pallets/flask/issues
# Todas elas tem a mesma barrinha de acesso em cima
# Seria chato copiar e colar em todos os templates (e imagina ter que mudar!)

@app.route("/template_extra")
def lista():
    return render_template('compras_v3.html')

#python (chamou) template compras_v3 (extendeu) base.html
#renderizamos um html que é o base.html, preenchido com coisas do 
#compras_v3

#Como foi feita essa "ligação" ?

#O arquivo do conteudo principal avisou que ia extender
#o arquivo base, e separou um "block" pra preencher o base

#compras_v3: {% extends "base.html" %} -- eu quero completar o base.html
#compras_v3 {% block content %} coisas {% endblock %}


# criei um bloco no compras_v3, e indiquei, no base.html, o que fazer com esse bloco
# base.html: <div id="content">{% block content %}{% endblock %}</div>
# no caso, colocar dentro de um div

#Um detalhe: Seria possível definir multiplos blocks no arquivo compras_v3,
# E usar alguns ou todos eles no arquivo base.html


# Algumas atividades para a gente tentar fazer
# * construir lista de compras (dada uma lista de itens, monta uma <ol>)
# construir views: chat
# AC: sorteio
# voltemos no pip freeze, que fiquei devendo da aula passada
# adicionar form: chat


mensagens = [{"nome":"igor", "texto":"top"},
            {"nome":"laun", "texto":"maneiro"},
            {"nome":"teles", "texto":"pokemmon"}
]

@app.route("/chat")
def chat():
    return render_template("chat.html", 
    lista_mensagens = mensagens)

app.run(debug=True, port=5001)#toda vez que eu dou um save o servidor da reload
