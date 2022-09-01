class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo 
        self.area = area
        self.salario = salario
        self.bonus = bonus


class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        valor = len(self.dependentes) * self.emprego.bonus
        valor_final = (self.emprego.salario + self.emprego.salario * valor)/10
        return valor_final

emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

# dois dependentes (o dependente também é um objeto Pessoa)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

# adiciona dependentes na lista de dependentes da pessoa1
pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario())                # imprime 1100.0
