from abc import ABC, abstractmethod


class Pessoa(ABC):
    def _init_(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
    
    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_telefone(self):
        return self.__telefone
    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone


class Medico(Pessoa):
    def _init_(self, crm, cpf, nome, telefone, salario, especialidade):
        super()._init_(nome, cpf, telefone)
        self.__crm = crm
        self.__salario = salario
        self.__especialidade = especialidade
        self.__paciente = None
        self.__registro_de_observação = None


    def visitar_pacientes(self, paciente):
        self.__paciente = paciente


    def registrar_observacoes(self, registro_de_observação):
        self.__registro_de_observação = registro_de_observação


class Paciente(Pessoa):
    def _init_(self, cpf, rg, nome, endereco, telefone, data_nascimento, medico_responsavel):
        super()._init_(nome, cpf, telefone)
        self.__rg = rg
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento  
        self.__medico_responsavel = medico_responsavel

    def internar(self, interna_paciente):
        self.iterna_paciente = interna_paciente


class Clinica():
    def _init_(self, medico, paciente, quarto):
        self.medico = medico
        self. paciente = paciente
        self.quarto = quarto
        self.historico_medico = None


class Historico():
    def _init_(self, datas, horarios, observacoes, medico_responsavel):
        self.data = datas
        self.horario = horarios
        self.observacao = observacoes
        self.medico = medico_responsavel

class quarto():
    def __init__(self, numero, andar):
        self.__numero_quarto = numero
        self.__andar_quarto = andar 


paciente01 = Paciente(cpf, rg, nome)

med = Medico("11111111", "454.545.458.9-2", "nome", "+55 11 99889954", "4.999 R$", "Neuro")
med.visitar_pacientes("joaquim")
med.registrar_observações("obito de joaquim")
print(med.registro_observar)