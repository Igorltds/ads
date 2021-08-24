import random
from flask import Flask, request, render_template

class Jogo():
    def __init__(self):
        self.restart()

    def restart(self):
        self.alvo = random.randint(0, 100)
        self.maior = 100
        self.menor = 0
        self.chutes = []

    def chutar(self, chute):
        assert(type(chute) == int)
        # TODO: salvar o chute na lista de chutes
        self.chutes.append(chute)

        if chute > self.alvo:
            self.maior = chute-1
        if chute < self.alvo:
            self.menor = chute+1

        if chute == self.alvo:
            self.menor = chute
            self.maior = chute

    def resumo(self):
        if self.chutes == []:
            return f"Estamos entre {self.menor} e {self.maior}. Chute um número"

        ultimo_chute = self.chutes[-1]
        if ultimo_chute == self.alvo:
            return "Você fez um chute correto! Você acertou! Parabéns!"

        resumo = ""

        if ultimo_chute < self.alvo:
            resumo += "Seu ultimo chute foi baixo!"
        if ultimo_chute > self.alvo:
            resumo += "Seu ultimo chute foi alto!"
        resumo += f" Estamos entre {self.menor} e {self.maior}"

        return resumo






app = Flask(__name__)
@app.route("/")
def inicio():
    return  render_template("main.html")

primeira = True
@app.route('/jogo', methods=['GET', 'POST'])
def jogo():
    global primeira
    if primeira:
        joguinho = Jogo()
    forms = request.form.get(("chute"))
    joguinho.chutar
    print(joguinho.resumo)
    primeira = False

    return  render_template("jogo.html")

@app.route('/restart')
def restart():
    global primeira
    primeira = True
    joguinho.restart
    pass



app.run(debug=True)
