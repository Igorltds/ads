# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO
# ALUNO 1: Felipe Waddington Pereira Jeronymo 1904837
# ALUNO 2: Gustavo de Moraes Silva 1905338
# ALUNO 3: Hires Serva de Maria Menezes 1904889
# ALUNO 4: Igor Luan Teles de Souza 1905365
# ALUNO 5: Jhonata Flaubert Alves 1904629
# ALUNO 6: Rodrigo Augusto Aniceto Alves 1904668


from abc import ABC


# classe Pessoa

class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    def get_nome(self):                     # get e set, nome
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_cpf(self):                      # get e set, cpf
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_telefone(self):                 # get e set, telefone
        return self.__telefone

    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone


# classe Medico

class Medico(Pessoa):
    def __init__(self, crm, cpf, nome, telefone, salario, especialidade):
        super().__init__(nome, cpf, telefone)
        self.__crm = crm
        self.__salario = salario
        self.__especialidade = especialidade

    def registrar_observacoes(self, registro):
        self.__registro.append(registro)

    def get_crm(self):                      # get e set, crm
        return self.__crm

    def set_crm(self, novo_crm):
        self.__crm = novo_crm

    def get_salario(self):                  # get e set, salario
        return self.__salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

    def get_especialidade(self):            # get e set, especialidade
        return self.__especialidade

    def set_especialidade(self, novo_especialidade):
        self.__especialidade = novo_especialidade

    def get_paciente(self):                 # get e set, paciente
        return self.__paciente

    def set_paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    def get_registro(self):                 # get e set, registro
        return self.__registro

    def set_registro(self, novo_registro):
        self.__registro = novo_registro


# classe Paciente

class Paciente(Pessoa):
    def __init__(self, cpf, rg, nome, endereco, telefone, data_nascimento, quarto):
        super().__init__(nome, cpf, telefone)
        self.__rg = rg
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__quarto = quarto

    def get_rg(self):                       # get e set, rg
        return self.__rg

    def set_rg(self, novo_rg):
        self.__rg = novo_rg

    def get_endereco(self):                 # get e set, endereço
        return self.__endereco

    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    def get_data_nascimento(self):          # get e set, data de nascimento
        return self.__data_nascimento

    def set_data_nascimento(self, novo_data_nascimento):
        self.__data_nascimento = novo_data_nascimento

    def get_quarto(self):                   # get e set, quarto
        return self.__quarto

    def set_quarto(self, novo_quarto):
        self.__quarto = novo_quarto


# classe Quarto

class Quarto():
    def __init__(self, numero, andar):
        self.__numero = numero
        self.__andar = andar

    def get_numero(self):                   # get e set, numero
        return self.__numero

    def set_numero(self, novo_numero):
        self.__numero = novo_numero

    def get_andar(self):                    # get e set, andar
        return self.__andar

    def set_andar(self, novo_andar):
        self.__andar = novo_andar


# classe Clinica

class Clinica():
    def __init__(self, medico, paciente):
        self.__medico = medico
        self.__paciente = paciente
        self.__historico_medico = []

    def get_medico(self):                   # get e set, medico
        return self.__medico

    def set_medico(self, novo_medico):
        self.__medico = novo_medico

    def get_paciente(self):                 # get e set, paciente
        return self.__paciente

    def set_paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    def get_historico_medico(self):         # get e set, historico medico
        return self.__historico_medico

    def set_historico_medico(self, novo_historico_medico):
        self.__historico_medico = novo_historico_medico


# classe Historico

class Historico():
    def __init__(self, medico_responsavel, paciente):
        self.__medico_responsavel = medico_responsavel
        self.__paciente = paciente
        self.__observacoes = []

    # novo registro:

    def append_observacoes(self,  medico, data, horario, observacao):
        observacao = {'data': data,
                      'horario': horario,
                      'observacao': observacao,
                      'medico': medico.get_nome()
                      }
        self.__observacoes.append(observacao)

    def get_paciente(self):                 # get e set, paciente
        return self.__paciente

    def set_paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    def get_observacoes(self):              # get, observacoes
        return self.__observacoes

    def get_medico_responsavel(self):       # get e set, medico responsavel
        return self.__medico_responsavel

    def set_medico_responsavel(self, novo_medico_responsavel):
        self.__medico_responsavel = novo_medico_responsavel


# Programa Principal

quarto01 = Quarto(1, 1)
med01 = Medico('46546crm', '454.545.458-92', 'medico1',
               '+55 11 97834982743', '19999R$', 'Neuro')
paciente01 = Paciente('xyz.545.458-92', 'RG 57.151.54.-4', 'Clarisberto',
                      'rua xxx', '+55 11 45465465465', '07/02/2007',  quarto01)

'''
print( med01.get_cpf(),
       med01.get_nome(),
       med01.get_telefone(),
       med01.get_crm())

print(paciente01.get_nome(),
      paciente01.get_cpf(),
      paciente01.get_rg())      

print(quarto01.get_andar(),
      quarto01.get_numero())
'''

clinica = Clinica(med01, paciente01)

'''print(clinica.get_medico().get_nome(),
      clinica.get_paciente().get_nome(),
      clinica.get_historico_medico())
'''

historico_paciente01 = Historico(med01, paciente01)
historico_paciente01.append_observacoes(
    med01, "07/07/2007", "12:40", "apresenta melhoras! :)")

quarto02 = Quarto(2, 1)

paciente01.set_quarto(quarto02)
# print(paciente01.get_quarto().get_numero())

print("Fim. ")