class Pessoa:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.__cpf = cpf
    
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, mod):
        self.__cpf = mod

pessoa1 = Pessoa("igor", "igorltdz", "79791313467")
print(pessoa1.get_cpf())
