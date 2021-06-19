    #Classe, quem instancia o objeto, extraindo suas abstrações.

class Pessoa:
        #construtor
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

        #Métodos 
        #
        #



    #Programa

lista_pessoas = [] 

def nova_pessoa(lista_pessoas):     #função para adicionr pessoas
    nome = input("digite o nome: ")
    email = input('digite o email: ')
    numero = input('digite o numero: ')
    lista_pessoas.append([nome, email, numero])
    return lista_pessoas


lista_pessoas = nova_pessoa(lista_pessoas)
lista_pessoas = nova_pessoa(lista_pessoas)

for x in lista_pessoas:
    print(x)
