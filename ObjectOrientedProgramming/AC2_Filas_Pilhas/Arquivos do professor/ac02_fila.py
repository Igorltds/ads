# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 02

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO 1: nome
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


'''
Uma FILA é uma estrutura de dados onde os itens são sempre inseridos no
final da fila, e sempre removidos do início.
Não é permitido inserir ou remover itens que estejam em outras posições.

As operação básicas para manipular uma fila são:
-> Enfileirar: insere um item no final da fila
-> Desenfileirar: remove e retorna o item do início da fila
-> Primeiro: retorna mas não remove o item do início da fila
-> Vazia: retorna True se a fila estiver vazia e False caso contrário
-> Tamanho: retorna a quantidade de itens na fila

Considerando o conceito de fila, e sabendo que podemos implementar uma fila
a partir de uma lista, implemente as funções solicitadas neste arquivo.

Obs.: Considere que o elemento de índice zero, sempre será o início da fila.
'''

'''
Implemente a função "enfileirar" que recebe como entrada uma fila e um
elemento que deve ser inserido no final da fila
'''


def enfileirar(fila, elemento):
    pass        # retire esse pass e escreva aqui o seu código


'''
Implemente a função "desenfileirar" que recebe como entrada uma fila,
remove e retorna o elemento do inicio da fila
'''


def desenfileirar(fila):
    pass


'''
Implemente a função "primeiro" que recebe como entrada uma fila e retorna
o elemento do início, mas sem retirá-lo da fila.
'''


def primeiro(fila):
    pass


'''
Implemente a funcao "vazia" que recebe como entrada uma fila e retorna
True se a fila estiver vazia e False se a fila não estiver vazia.
'''


def vazia(fila):
    pass


'''
Implemente a função "tamanho" que recebe como entrada uma fila e retorna a
quantidade de elementos contidos nessa fila.
'''


def tamanho(fila):
    pass


'''
Implemente a função "vira_n" que recebe como entrada uma fila e um número n,
retira da fila os n primeiros elementos e os coloca de volta no fim da fila

Exemplo:
fila = [1, 2, 3, 4, 5]
Se fizermos vira_n(fila, 3), a fila passa a ser [4, 5, 1, 2, 3]

fila = [1, 2, 3, 4, 5]
Se fizermos vira_n(fila, 4), a fila passa a ser [5, 1, 2, 3, 4]

ATENÇÃO: Lembre-se que você só pode remover o primeiro elemento e só pode
inserir no final da fila.

DICA: Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def vira_n(fila, n):
    pass


'''
Implemente a função "vira_4_mata_1" que recebe como entrada uma fila,
retira da fila os 4 primeiros elementos e os coloca de volta no fim da fila.
E depois tira o primeiro elemento da fila e não coloca ele de volta.

Exemplo:
fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Tira o 1 e coloca no fim, depois o 2, depois o 3, depois o 4.
Tira o 5 e nao coloca na fila.
Ao final a fila será [6, 7, 8, 9, 1, 2, 3, 4]

ATENÇÃO: Lembre-se que você só pode remover o primeiro elemento e só pode
inserir no final da fila.
'''


def vira_4_mata_1(fila):
    pass


'''
Implemente a função "inverte", que recebe uma fila e inverte a posição dos
elementos contidos na fila.

Exemplo:
fila = [1, 3, 7, 5]
a função deve retornar[5, 7, 3, 1]

ATENÇÃO: Lembre-se que você só pode remover o primeiro elemento e só pode
inserir no final da fila.

DICA: Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
DICA: Utilize uma "pilha" como estrutura auxiliar:
      -> Desenfileire cada elemento da fila e vá empilhando na pilha.
      -> Depois desempilhe cada elemento da pilha e enfileire na fila.
'''


def inverte(fila):
    pass
