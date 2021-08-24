# ARQUIVO DE TESTE
# Esse arquivo não deve ser alterado

from ac03 import Escola, Casa, Professor, Disciplina, Torneio, Aluno
import sys
import traceback

erros = 0


def imprime_erro():
    # função utilizada para exibir mensagens de erro
    _, _, tb = sys.exc_info()
    tb_info = traceback.extract_tb(tb)
    _, line, _, text = tb_info[-1]
    print(f'ERRO no teste da linha {line}: {text}')
    global erros
    erros = erros + 1


try:
    # Criação do objeto Escola
    hogwarts = Escola("Escola de Magia e Bruxaria de Hogwarts")
except Exception:
    imprime_erro()

try:
    # Criação dos objetos Casa
    grifinoria = Casa("Grifinória", "Leão")
    sonserina = Casa("Sonserina", "Serpente")
    corvinal = Casa("Corvinal", "Corvo")
    lufalufa = Casa("Lufa-Lufa", "Texugo")
except Exception:
    imprime_erro()

try:
    # Criação dos objetos Disciplina
    herbologia = Disciplina("Herbologia", "Ervas, Fungos e Árvores Mágicas")
    transfiguracao = Disciplina("Transfiguracao", "Transfiguração Humana")
    pocoes = Disciplina("Poções", "Poções Simples, Poções Avançadas")
    defesa = Disciplina("Defesa", "Maldições, Dementadores, Feitiços verbais")
except Exception:
    imprime_erro()

try:
    # Criação dos objetos Professor
    minerva = Professor("Minerva McGonagall", "19351004")
    filio = Professor("Fílio Flitwick", "19301017")
    pomona = Professor("Pomona Sprout", "19410515")
    severo = Professor("Severo Snape", "19600109")
except Exception:
    imprime_erro()

try:
    # Criação dos objetos Aluno
    draco = Aluno("Draco Malfoy", "19800605", "puro-sangue")
    ernesto = Aluno("Ernesto Macmillan", "19800901", "puro-sangue")
    hermione = Aluno("Hermione Granger", "19790919", "trouxa")
    harry = Aluno("Harry Potter", "19800731", "mestiço")
    luna = Aluno("Luna Lovegood", "19810213", "puro-sangue")
except Exception:
    imprime_erro()

try:
    # Criação do objeto Torneio
    torneio = Torneio(sonserina, grifinoria)
except Exception:
    imprime_erro()

try:
    # Inclui as casas na escola
    hogwarts.incluir_casa(grifinoria)
    hogwarts.incluir_casa(sonserina)
    hogwarts.incluir_casa(corvinal)
    hogwarts.incluir_casa(lufalufa)

except Exception:
    imprime_erro()

try:
    # Definição dos diretores das casas
    grifinoria.set_diretor(minerva)
    sonserina.set_diretor(severo)
    corvinal.set_diretor(filio)
    lufalufa.set_diretor(pomona)
except Exception:
    imprime_erro()

try:
    # Definicao dos monitores das casas
    grifinoria.set_monitor(hermione)
    sonserina.set_monitor(draco)
    corvinal.set_monitor(ernesto)
    lufalufa.set_monitor(luna)
except Exception:
    imprime_erro()

try:
    # Definição das casas dos alunos
    draco.set_casa(sonserina)
    ernesto.set_casa(corvinal)
    hermione.set_casa(grifinoria)
    harry.set_casa(grifinoria)
    luna.set_casa(lufalufa)
except Exception:
    imprime_erro()

try:
    # Definicao dos professores das disciplinas
    severo.incluir_disciplina(defesa)
    severo.incluir_disciplina(transfiguracao)
    minerva.incluir_disciplina(herbologia)
    filio.incluir_disciplina(transfiguracao)
    pomona.incluir_disciplina(pocoes)
except Exception:
    imprime_erro()

try:
    # Definição dos alunos que cursam as disciplinas
    herbologia.incluir_aluno(harry)
    herbologia.incluir_aluno(hermione)
    transfiguracao.incluir_aluno(draco)
    transfiguracao.incluir_aluno(hermione)
    pocoes.incluir_aluno(ernesto)
    defesa.incluir_aluno(harry)
    defesa.incluir_aluno(draco)
    defesa.incluir_aluno(ernesto)
    defesa.incluir_aluno(hermione)
    defesa.incluir_aluno(luna)
except Exception:
    imprime_erro()

try:
    # Inclusão de triunfos e mau_feitos dos alunos
    harry.incluir_triunfo(3)
    harry.incluir_mau_feito(1)
    draco.incluir_mau_feito(2)
    draco.incluir_triunfo(1)
    hermione.incluir_triunfo(4)
    harry.incluir_triunfo(2)
except Exception:
    imprime_erro()

try:
    # Marcação de pontos no torneio de quadribol
    torneio.marcar_ponto(sonserina, 2)
    torneio.marcar_ponto(grifinoria, 1)
    torneio.marcar_ponto(grifinoria, 3)
    torneio.marcar_ponto(sonserina, 1)
except Exception:
    imprime_erro()


try:
    # Verifica valores de alguns atributos
    assert hogwarts.nome == 'Escola de Magia e Bruxaria de Hogwarts'
    assert len(hogwarts.casas) == 4
    assert sonserina.nome == 'Sonserina'
    assert sonserina.animal == "Serpente"
    assert grifinoria.diretor.nome == "Minerva McGonagall"
    assert grifinoria.monitor.nome == "Hermione Granger"
    assert minerva.nome == "Minerva McGonagall"
    assert severo.nascimento == "19600109"
    assert severo.disciplinas[1].nome == "Transfiguracao"
    assert defesa.nome == "Defesa"
    assert herbologia.ementa == "Ervas, Fungos e Árvores Mágicas"
    assert len(defesa.alunos) == 5
    assert defesa.alunos[0].nome == "Harry Potter"
    assert luna.nome == "Luna Lovegood"
    assert luna.nascimento == "19810213"
    assert draco.tipo == "puro-sangue"
    assert draco.casa.nome == "Sonserina"
    assert hermione.get_triunfos() == 4
    assert draco.get_mau_feitos() == 2
    assert torneio.casa1.nome == "Sonserina"
    assert torneio.casa2.nome == "Grifinória"
    assert torneio.get_pontos_casa1() == 3
    assert torneio.get_pontos_casa2() == 4
except Exception:
    imprime_erro()


if erros == 0:
    print("NENHUM ERRO ENCONTRADO NOS TESTES")
