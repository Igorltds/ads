from ac02_fila import enfileirar, desenfileirar, primeiro, vazia, tamanho
from ac02_fila import vira_n, vira_4_mata_1, inverte


def test_01_enfileirar():
    try:
        fila = [1, 2]
        enfileirar(fila, 5)
        assert fila == [1, 2, 5]
        enfileirar(fila, 10)
        assert fila == [1, 2, 5, 10]
        fila = [1, 2]
        enfileirar(fila, 10)
        assert fila == [1, 2, 10]
        print("enfileirar: CORRETO")
    except AssertionError:
        print("enfileirar: ERRO")


def test_02_desenfileirar():
    try:
        fila = [10, 4, 5]
        item = desenfileirar(fila)
        assert item == 10
        assert fila == [4, 5]
        item = desenfileirar(fila)
        assert item == 4
        assert fila == [5]
        item = desenfileirar(fila)
        assert item == 5
        assert fila == []
        fila = [11, 12, 13]
        item = desenfileirar(fila)
        assert item == 11
        assert fila == [12, 13]
        print("desenfileirar: CORRETO")
    except AssertionError:
        print("desenfileirar: ERRO")


def test_03_primeiro():
    try:
        fila = [4, 3, 2]
        item = primeiro(fila)
        assert item == 4
        if fila != [4, 3, 2]:
            raise TypeError
        print("primeiro: CORRETO")
    except AssertionError:
        print("primeiro: ERRO")
    except TypeError:
        print("primeiro: ERRO - nao deve retirar da fila")


def test_04_vazia():
    try:
        fila = [4, 50, 2]
        assert vazia(fila) is False
        desenfileirar(fila)
        assert vazia(fila) is False
        desenfileirar(fila)
        assert vazia(fila) is False
        desenfileirar(fila)
        assert vazia(fila) is True
        enfileirar(fila, 12)
        assert vazia(fila) is False
        print("vazia: CORRETO")
    except AssertionError:
        print("vazia: ERRO")


def test_05_tamanho():
    try:
        fila = [10, 4, 5]
        assert tamanho(fila) == 3
        desenfileirar(fila)
        assert tamanho(fila) == 2
        desenfileirar(fila)
        assert tamanho(fila) == 1
        desenfileirar(fila)
        assert tamanho(fila) == 0
        print("tamanho: CORRETO")
    except AssertionError:
        print("tamanho: ERRO")


def test_06_vira_n():
    try:
        fila = [1, 2, 3, 4]
        vira_n(fila, 2)
        assert fila == [3, 4, 1, 2]
        vira_n(fila, 3)
        assert fila == [2, 3, 4, 1]
        fila = [3, 4, 5]
        vira_n(fila, 5)
        assert fila == [5, 3, 4]
        print("vira_n: CORRETO")
    except AssertionError:
        print("vira_n: ERRO")


def test_07_vira_4_mata_1():
    try:
        fila = [1, 2, 3, 4, 5, 6]
        vira_4_mata_1(fila)
        assert fila == [6, 1, 2, 3, 4]
        fila = [1, 2, 3, 4, 5]
        vira_4_mata_1(fila)
        assert fila == [1, 2, 3, 4]
        print("vira_4_mata_1: CORRETO")
    except AssertionError:
        print("vira_4_mata_1: ERRO")


def test_08_inverte():
    try:
        fila = [1, 2, 3, 4]
        inverte(fila)
        assert fila == [4, 3, 2, 1]
        fila = [7, 3, 1]
        inverte(fila)
        assert fila == [1, 3, 7]
        print("inverte: CORRETO")
    except AssertionError:
        print("inverte: ERRO")


test_01_enfileirar()
test_02_desenfileirar()
test_03_primeiro()
test_04_vazia()
test_05_tamanho()
test_06_vira_n()
test_07_vira_4_mata_1()
test_08_inverte()
