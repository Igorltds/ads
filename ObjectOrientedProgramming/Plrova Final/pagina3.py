'''
Implemente as classes Conta e CadastroConta.
A classe Conta possui os atributos numero e titular.
A classe CadastroConta possui o atributo contas, que armazena uma
lista de objetos da classe Conta.
Os atributos das classes devem ser inicializados nos construtores.
A lista de contas deve ser inicializada como vazia.
A classe CadastroConta deve implementar os métodos:
    cadastrar: recebe como entrada um objeto da classe Conta e a insere
    na lista de contas.
    pesquisar: receba como entrada o número de uma conta e retorna a
    instância do objeto Conta correspondente.
'''


# --------------------- IMPLEMENTE SEU CÓDIGO AQUI --------------------------
# ...
# ...


class CadastroConta:
    def __init__(self):
        self.contas = []

    def cadastrar(self, novaconta):
        self.contas.append(novaconta)

    def pesquisar(self, numero_conta):
        for x in self.contas:
            if x == numero_conta:
                return x
        

class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------

conta1 = Conta(123, 'João')
conta2 = Conta(456, 'Maria')

cadastro = CadastroConta()
cadastro.cadastrar(conta1)
cadastro.cadastrar(conta2)

c = cadastro.pesquisar(456)
print("Número:", c.numero)              # Número: 456
print("Titular:", c.titular)            # Titular: Maria

c = cadastro.pesquisar(123)
print("Número:", c.numero)              # Número: 123
print("Titular:", c.titular)            # Titular: João