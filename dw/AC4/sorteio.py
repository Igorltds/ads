from flask import Flask, request, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def exercicio():
    return '''O exercicio: crie um sistema que exibe uma lista
    de pessoas, marcando o ganhador como "ganhador", e relatando seu
    premio. Leia mais detalhes no arquivo .py
    '''
'''
Parte 1: Montar a lista

Sua missão é montar uma função que lê a lista
alunos e devolve uma lista ordenada com os nomes
(criando um html válido, usando templates)

Sua função deve atender na URL /sorteio
'''

alunos = ["Marcos", "Maria", "Eduarda", "José"]


@app.route("/sorteio")
def sorteio():
    '''
hoje = date.today()
    d = hoje.strftime('%d/%B/%Y') #Mês por extenso (no exercicio deu a entender que era por extenso, mas não era)
    d = d.split("/")
    '''
    return render_template("sorteio.html", lista_alunos = alunos, ganhador = ganhador, data = date.today())
    

'''
Parte 2: Você deve alterar sua função (e o template), de forma que o li do
usuário ganhador tenha a classe "destaque", fazendo com que 
esse li inteiro apareca em vermelho.

Adicione CSS no seu html para fazer com que a classe destaque
tenha esse efeito

Seu código deve funcionar sem erros, mesmo que não haja
nenhum jogador marcado como "ganhador".

Se o ganhador não constar na lista de alunos, nenhum aluno recebe destaque
'''

ganhador = "Maria"

'''
Parte 3: Você deve alterar sua função (e o template) para exibir
o dia de hoje, e a mensagem "No dia DIA do mês MES, o ganhador foi GANHADOR"

Por exemplo, se o ganhador foi a Maria, e hoje é primeiro de abril, 
deverá aparecer o texto "No dia 01 do mês abril, o ganhador foi Maria"

Para ver a data atual, consulte: https://docs.python.org/pt-br/3/library/datetime.html#date-objects

Se o ganhador não estiver especificado (valer None), 
ou não constar na lista de alunos
você deve não exibir nada dessa mensagem (nem mesmo a data)

Mantenha o destaque no ganhador

NOTE: No teste existe uma string data. Atualize ela para a data de hoje,
para que os testes possam rodar com sucesso. 

Isso é uma gambiarra para os testes não spoilarem o exercicio.

Seu código deve funcionar sem necessidade de gambiarra semelhante.
'''

#não altere mais nada nesse arquivo. As rotas abaixo 
#redefinem os alunos e o ganhador, para os testes
@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    aluno = request.form['nome']
    alunos.append(aluno)
    return "aluno adicionado com sucesso"

@app.route("/ganhador", methods=["POST"])
def adicionar_ganhador():
    global ganhador
    aluno = request.form['nome']
    ganhador = aluno
    return "ganhador alterado com sucesso"

@app.route("/reseta", methods=["POST"])
def resetar():
    global alunos
    global ganhador
    alunos = []
    ganhador = None
    return "reseta feito com sucesso"

app.run(debug=True)#toda vez que eu dou um save o servidor da reload
