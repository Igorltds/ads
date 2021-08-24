# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 02

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO 1: nome
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 5: nome


'''
Uma PILHA é uma estrutura de dados onde os itens são sempre inseridos no
final da pilha, e removidos também do final da pilha.

Não é permitido inserir ou remover itens que estejam em outras posições.

Normalmente o final da pilha de é chamado de 'topo'.

As operação básicas para manipular uma pilha são:
-> Enpilhar: insere um item no final da pilha
-> Desempilhar: remove e retorna o item do final da pilha
-> Topo: retorna mas não remove o item do final da pilha
-> Vazia: retorna True se a pilha estiver vazia e False caso contrário
-> Tamanho: retorna a quantidade de itens na pilha

Considerando o conceito de pilha, e sabendo que podemos implementar uma pilha
a partir de uma lista, implemente as funções solicitadas neste arquivo.

Obs.: Considere que o elemento de índice zero, será a base da pilha e o último
elemento será o topo.
'''

'''
Implemente a função "empilhar", que recebe uma pilha e um elemento e coloca
o elemento no topo da pilha.
'''


def empilhar(pilha, elemento):
    pass        # tire esse pass e escreva o codigo aqui


'''
Implemente a função "desempilhar" que recebe como entrada uma pilha,
remove e retorna o elemento do final da pilha
'''


def desempilhar(pilha):
    pass


'''
Implemente a função "topo" que recebe como entrada uma pilha e retorna
o elemento do topo, mas sem retirá-lo da pilha.
'''


def topo(pilha):
    pass


'''
Implemente a funcao "vazia" que recebe como entrada uma pilha e retorna
True se a pilha estiver vazia e False se a pilha não estiver vazia.
'''


def vazia(pilha):
    pass


'''
Implemente a função "tamanho" que recebe como entrada uma pilha e retorna a
quantidade de elementos contidos nessa pilha.
'''


def tamanho(pilha):
    pass


'''
Implemente a função "pilha_letras", que recebe uma string, percorre a string
do inicio até o final e vai colocando os caracter da string em uma pilha.
A função deve retornar a pilha.
'''


def pilha_letras(texto):
    pass


'''
Implemente a função "menos_o_d" que recebe uma string, percorre a string
do inicio até o final e vai colocando os caracter da string em uma pilha,
como a funcao acima.
Porém, quando encontrar o caracter "d", ao invés de colocar o "d", deve
desempilhar um item da pilha.

Observe que pode ocorrer a situação de tentar desempilhar um item de uma pilha
vazia. Nesse caso, simplesmente não tire nada da pilha, até que ela volte a ter
algum item.

Sua função deve retornar a ultima pilha.

Exemplos:
texto = "abcdxyd"
A pilha final deve ser: [a, b, x]

texto = "abcddxyz"
A pilha final deve ser: [a, x, y, z]

texto = "dabc"
A pilha final deve ser: [a, b, c]

texto = "abcddddxyzd"
A pilha final deve ser: [x, y]
'''


def menos_o_d(texto):
    pass


'''
Implemente a função "pilha_par_impar" que recebe uma pilha de números inteiros.
Você deve desempilhar os itens e distribuí-los em outras duas pilhas.

Uma pilha deve conter os números pares e outra os números ímpares,
mantendo a ordem original dos elementos.

ATENÇÃO: Lembre-se que você só pode remover o último elemento de uma pilha e
só pode inserir no final da pilha.

DICA: utilize uma pilha auxiliar:
        -> desempilhe cada elemento da pilha inicial e vá empilhando na pilha
           auxiliar
        -> depois desempilhe cada elemento da pilha auxiliar e vá empilhando
           nas pilhas de números pares e ímpares

A função deve retornar as duas pilhas.

Exemplos:
Se pilha = [1, 2, 3, 4, 5, 6, 8], então:
pilha_par = [2, 4, 6, 8]
pilha_impar = [1, 3, 5]

Se pilha = [1, 3, 5], então:
pilha_par = []
pilha_impar = [1, 3, 5]
'''


def pilha_par_impar(pilha):
    pilha_par = []
    pilha_impar = []

    pass                # implemente o restante aqui

    return pilha_par, pilha_impar
