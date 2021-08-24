class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.cep = cep

    def exibir_dados(self):
        print("Rua: ", self.rua)
        print("Numero: ", self.numero)
        print("CEP: ", self.cep)


class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Sexo: ", self.sexo)
        self.endereco.exibir_dados()

end1 = Endereco("Rua Paulista", 24, 8922)
end2 = Endereco("Av. Kenkiti shimomoto", 24, 45678)

pessoa001 = Pessoa("jubileu de bronze", 84, "Ele é mais que isso", end1)

pessoa002 = Pessoa("jubileu de ouro", 84, "Ele é bem mais que isso", end1)
pessoa003 = Pessoa("Jubileu de grafeno", 20, "Não preciso falar nada", end2)

pessoa001.exibir_dados()
pessoa002.exibir_dados()
pessoa003.exibir_dados()