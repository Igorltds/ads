from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return "verifique a URL /calc e /resultado"

@app.route("/calc")
def exibe_calculadora():
    html = '''
    <form action="/resultado">
    a <input type="text" name="a" id="a">
    b <input type="text" name="b" id="b">
    multiplicação: <input type="radio" name="ope" value="mult">
    divisão: <input type="radio" name="ope" value="div">
    soma: <input type="radio" name="ope" value="soma">
    subtracao: <input type="radio" name="ope" value="sub">
    <button type="submit">calcular</button>
    </form>

    Implemente as operacoes! Teste com o arquivo runtests_calculadora.py
    '''
    return html

@app.route("/resultado")
def resultado():
    #chatisses: 
    # ?a=12,b=13 o flask interpreta a= string 12, b = string 13
    # quando eu for retornar, meu retorno tem que ser string, nao inteiro
    a   = int(request.args['a'])
    b   = int(request.args['b'])
    ope = request.args['ope']
    if ope == "soma":
        return str(a+b)
    if ope == "div":
        return str(a/b)
    if ope == "sub":
        return str(a-b)
    if ope == "mult":
        return str(a*b)

app.run(debug=True)