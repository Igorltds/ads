from ac02_pilha import empilhar, desempilhar, vazia, topo, tamanho, menos_o_d
from ac02_pilha import pilha_letras, pilha_par_impar


def test_01_empilhar():
    try:
        pilha = [2, 3]
        empilhar(pilha, 4)
        assert pilha == [2, 3, 4]
        empilhar(pilha, 5)
        assert pilha == [2, 3, 4, 5]
        pilha = []
        empilhar(pilha, 5)
        assert pilha == [5]
        print("empilhar: CORRETO")
    except AssertionError:
        print("empilhar: ERRO")


def test_02_desempilhar():
    try:
        pilha = [1, 2, 3, 4, 5, 6, 7]
        item = desempilhar(pilha)
        assert item == 7
        assert pilha == [1, 2, 3, 4, 5, 6]
        item = desempilhar(pilha)
        assert item == 6
        assert pilha == [1, 2, 3, 4, 5]
        item = desempilhar(pilha)
        assert item == 5
        assert pilha == [1, 2, 3, 4]
        print("desempilhar: CORRETO")
    except AssertionError:
        print("desempilhar: ERRO")


def test_03_topo():
    try:
        pilha = [1, 2, 3, 4, 5, 6, 7]
        item = topo(pilha)
        assert item == 7
        assert pilha == [1, 2, 3, 4, 5, 6, 7]
        pilha = [1, 2, 3]
        item = topo(pilha)
        assert item == 3
        assert pilha == [1, 2, 3]
        pilha = [1]
        item = topo(pilha)
        assert item == 1
        assert pilha == [1]
        print("topo: CORRETO")
    except AssertionError:
        print("topo: ERRO")


def test_04_vazia():
    try:
        pilha = [1, 2, 3]
        assert vazia(pilha) is False
        pilha = []
        assert vazia(pilha) is True
        print("vazia: CORRETO")
    except AssertionError:
        print("vazia: ERRO")


def test_05_tamanho():
    try:
        pilha = [1, 2, 3]
        assert tamanho(pilha) == 3
        pilha = []
        assert tamanho(pilha) == 0
        pilha = [5, 6, 7, 8, 9, 10]
        assert tamanho(pilha) == 6
        print("tamanho: CORRETO")
    except AssertionError:
        print("tamanho: ERRO")


def test_06_pilha_letras():
    try:
        pilha = pilha_letras('banana')
        assert pilha == ['b', 'a', 'n', 'a', 'n', 'a']
        pilha = pilha_letras('teste')
        assert pilha == ['t', 'e', 's', 't', 'e']
        print("pilha_letras: CORRETO")
    except AssertionError:
        print("pilha_letras: ERRO")


def test_07_menos_o_d():
    try:
        pilha = menos_o_d('banana')
        assert pilha == ['b', 'a', 'n', 'a', 'n', 'a']
        pilha = menos_o_d('bandana')
        assert pilha == ['b', 'a', 'a', 'n', 'a']
        pilha = menos_o_d('addd')
        assert pilha == []
        pilha = menos_o_d('dbandana')
        assert pilha == ['b', 'a', 'a', 'n', 'a']
        print("menos_o_d: CORRETO")
    except AssertionError:
        print("menos_o_d: ERRO")


def test_08_pilha_par_impar():
    try:
        pilha = [1, 2, 3, 4, 5, 6, 7]
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == [2, 4, 6]
        assert resultado[1] == [1, 3, 5, 7]
        pilha = [7, 5, 3, 8, 4, 2, 5, 1, 9]
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == [8, 4, 2]
        assert resultado[1] == [7, 5, 3, 5, 1, 9]
        pilha = [4, 6, 8, 10]
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == [4, 6, 8, 10]
        assert resultado[1] == []
        pilha = []
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == []
        assert resultado[1] == []
        print("pilha_par_impar: CORRETO")
    except AssertionError:
        print("pilha_par_impar: ERRO")


test_01_empilhar()
test_02_desempilhar()
test_03_topo()
test_04_vazia()
test_05_tamanho()
test_06_pilha_letras()
test_07_menos_o_d()
test_08_pilha_par_impar()
