#Exercício 01

#Altere a classe Funcionario do programa abaixo:
#    Transforme todos os seus atributos em atributos privados.
#    Crie os métodos get e set para todos os atributos.
#    Faça as demais alterações necessárias para que o programa principal funcione corretamente


#programa
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
#nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_nome(self):
        return self.__nome

#cpf
    def set_cpf(self, novo_cpf):
            self.__cpf = novo_cpf

    def get_cpf(self):
            return self.__cpf
#salario
    def set_salario(self, novo_salario):
            self.__salario = novo_salario
    
    def get_salario(self):
            return self.__salario



func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.set_salario(2000.0)              # Altera o salário
print("Nome:", func1.get_nome())
print("CPF:", func1.get_cpf())
print("Salário:", func1.get_salario())
