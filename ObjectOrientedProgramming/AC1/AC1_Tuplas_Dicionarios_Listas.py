# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Igor Luan Teles de Souza
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


''''
Escreva uma função com o nome pertence, que recebe como argumentos de entrada
uma tupla e um item e retorna True, se o item estiver armazenado na tupla, e
False, caso contrário.
'''


def pertence(tupla, item):
    for c in tupla:
        if c == item:
            return True
    else:
        return False
#concluida ok


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    contagem = 0
    for x in lista:
        if x == velho:
            lista[contagem]=novo
        contagem += 1
    return lista
#concluido ok


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada
uma lista e um item, e retorna uma lista contendo todos os índices em que o
item aparece na lista.
'''


def posicoes_lista(lista, item):
    indices = []
    count = 0
    for x in lista:
        if x == item:
            indices.append(count)
        count+=1
    return indices

#concluido ok

'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada aprovados que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos aprovados
(um aluno é aprovado quando a média das suas notas é maior ou igual a 6).
'''
#tentativa bem sucedida
''' 
def aprovados(alunos):
    nomes=[]
    notas=[]
    lista=[]
    for x in alunos.keys():
        nomes.append(x)

    for x in alunos.values():
        media=0
        #print("x: ", x)
        for y in x:
            #print("y: ", y)
            media+=y
        media = media/len(x)
        notas.append(media)

    
    for a,b in zip(nomes, notas):
        if b >= 6:
            lista.append(a)

    return lista
'''
#resumo bem succedido
def aprovados(alunos):
    nomes=[]
    lista=[]

    for x, y in zip(alunos.keys(), alunos.values()):
        nomes.append(x)
        notinha=0
        notinha =sum(y)
        dividendo=len(y)

        if notinha/dividendo >= 6:
            lista.append(x)

    return lista
#concluida ok

'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        alunos[nome].append(nota)
    return alunos




'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maiores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com o nome e a
maior nota de cada aluno.
'''


def maiores_notas(alunos):
    dicionario={}
    for nomes, notas in zip(alunos.keys(), alunos.values()):
        dicionario[nomes] = max(notas)
    return  dicionario

