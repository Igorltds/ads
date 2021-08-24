'''
Esse arquivo pode ser utilizado para testar a implementação da AC01.
Não Faça nenhuma alteração nesse arquivo.
Ao executar esse arquivo, não deve ser exibida nenhuma mensagem de ERRO.
'''

from ac01 import pertence, substituir, posicoes_lista
from ac01 import aprovados, incluir_nota, maiores_notas

def teste_01():
    print(' teste_01', end=': ')
    tupla = (2, 3, 4)
    retorno = pertence(tupla, 3)        # chamada da função
    if retorno is True:
        print(" OK")
    else:
        print(" ERRO")


def teste_02():
    print(' teste_02', end=': ')
    tupla = (2, 3, 4)
    retorno = pertence(tupla, 1)        # chamada da função
    if retorno is False:
        print(" OK")
    else:
        print(" ERRO")


def teste_03():
    print(' teste_03', end=': ')
    lista = [1, 2, 3, 2, 4]
    retorno = substituir(lista, 2, 99)          # chamada da função
    if retorno == [1, 99, 3, 99, 4]:
        print(" OK")
    else:
        print(" ERRO")


def teste_04():
    print(' teste_04', end=': ')
    lista = [1, 2, 2, 4]
    retorno = substituir(lista, 2, 'abc')       # chamada da função
    if retorno == [1, 'abc', 'abc', 4]:
        print(" OK")
    else:
        print(" ERRO")


def teste_05():
    print(' teste_05', end=': ')
    lista = [1, 2, 2, 4]
    retorno = substituir(lista, 5, 10)       # chamada da função
    if retorno == [1, 2, 2, 4]:
        print(" OK")
    else:
        print(" ERRO")


def teste_06():
    print(' teste_06', end=': ')
    lista = ['a', 2, 'b', 'a', 'a']
    retorno = posicoes_lista(lista, 'a')        # chamada da função
    if retorno == [0, 3, 4]:
        print(" OK")
    else:
        print(" ERRO")


def teste_07():
    print(' teste_07', end=': ')
    lista = [2, 5, 5, 7, 8, 9, 10]
    retorno = posicoes_lista(lista, 5)          # chamada da função
    if retorno == [1, 2]:
        print(" OK")
    else:
        print(" ERRO")


def teste_08():
    print(' teste_08', end=': ')
    lista = [2, 5, 5, 7, 8, 9, 10]
    retorno = posicoes_lista(lista, 1)          # chamada da função
    if retorno == []:
        print(" OK")
    else:
        print(" ERRO")


def teste_09():
    print(' teste_09', end=': ')
    alunos = {'Augusto': [4.5, 7.0, 6.0],
              'Denise': [9.0, 8.5, 9.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = aprovados(alunos)                 # chamada da função
    if retorno == ['Denise', 'Marcelo']:
        print(" OK")
    else:
        print(" ERRO")


def teste_10():
    print(' teste_10', end=': ')
    alunos = {'Paulo': [5.5, 5.0, 4.0],
              'Fernando': [6.0, 6.0, 6.0],
              'Maria': [10.0, 8.5, 9]}
    retorno = aprovados(alunos)                 # chamada da função
    if retorno == ['Fernando', 'Maria']:
        print(" OK")
    else:
        print(" ERRO")


def teste_11():
    print(' teste_11', end=': ')
    alunos = {'Paulo': [5.5, 5.0, 4.0],
              'Fernando': [6.0, 7.0],
              'Maria': [10.0, 8.5, 5, 2.0, 1.0]}
    retorno = aprovados(alunos)                 # chamada da função
    if retorno == ['Fernando']:
        print(" OK")
    else:
        print(" ERRO")


def teste_12():
    print(' teste_12', end=': ')
    alunos = {'Paulo': [5.5, 5.0, 4.0],
              'Fernando': [6.0, 3.0],
              'Maria': [5.0, 5.0, 5.0, 2.0]}
    retorno = aprovados(alunos)                 # chamada da função
    if retorno == []:
        print(" OK")
    else:
        print(" ERRO")


def teste_13():
    print(' teste_13', end=': ')
    alunos = {'Augusto': [4.5, 7.0, 6.0],
              'Denise': [9.0, 8.5, 9.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = incluir_nota(alunos, 'Denise', 10.0)      # chamada da função
    if retorno == {'Augusto': [4.5, 7.0, 6.0],
                   'Denise': [9.0, 8.5, 9.5, 10.0],
                   'Ana Paula': [3.5, 1.0, 6.5],
                   'Marcelo': [9.0, 10.0, 7.0]}:
        print(" OK")
    else:
        print(" ERRO")


def teste_14():
    print(' teste_14', end=': ')
    alunos = {'Augusto': [4.5, 7.0, 6.0],
              'Denise': [9.0, 8.5, 9.5, 10.0],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = incluir_nota(alunos, 'Marcelo', 5.0)      # chamada da função
    if retorno == {'Augusto': [4.5, 7.0, 6.0],
                   'Denise': [9.0, 8.5, 9.5, 10.0],
                   'Ana Paula': [3.5, 1.0, 6.5],
                   'Marcelo': [9.0, 10.0, 7.0, 5.0]}:
        print(" OK")
    else:
        print(" ERRO")


def teste_15():
    print(' teste_15', end=': ')
    alunos = {'Augusto': [4.5, 7.0, 6.0],
              'Denise': [9.0, 8.5, 9.5, 10.0],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = incluir_nota(alunos, 'Paulo', 5.0)      # chamada da função
    if retorno == {'Augusto': [4.5, 7.0, 6.0],
                   'Denise': [9.0, 8.5, 9.5, 10.0],
                   'Ana Paula': [3.5, 1.0, 6.5],
                   'Marcelo': [9.0, 10.0, 7.0]}:
        print(" OK")
    else:
        print(" ERRO")


def teste_16():
    print(' teste_16', end=': ')
    alunos = {'Augusto': [4.5, 7.0, 6.0],
              'Denise': [9.0, 8.5, 9.5, 10.0],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = maiores_notas(alunos)                 # chamada da função
    if retorno == {'Augusto': 7.0,
                   'Denise': 10.0,
                   'Ana Paula': 6.5,
                   'Marcelo': 10.0}:
        print(" OK")
    else:
        print(" ERRO")


def teste_17():
    print(' teste_17', end=': ')
    alunos = {'Augusto': [6.0, 6.0, 6.0],
              'Denise': [9.0, 8.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = maiores_notas(alunos)                 # chamada da função
    if retorno == {'Augusto': 6.0,
                   'Denise': 9.0,
                   'Marcelo': 10.0}:
        print(" OK")
    else:
        print(" ERRO")


print("Função pertence:")
teste_01()
teste_02()

print("Função substituir:")
teste_03()
teste_04()
teste_05()

print("Função posicoes_lista:")
teste_06()
teste_07()
teste_08()

print("Função aprovados:")
teste_09()
teste_10()
teste_11()
teste_12()

print("Função incluir_nota:")
teste_13()
teste_14()
teste_15()

print("Função maiores_notas:")
teste_16()
teste_17()
