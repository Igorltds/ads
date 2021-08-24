from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone    


class Medico(Pessoa):
    def __init__(self, crm, cpf, nome, telefone, salario, especialidade):
        super().__init__(nome, cpf, telefone)
        self.__crm = crm
        self.__salario = salario
        self.__especialidade = especialidade
        self.__paciente = None
        self.__registro = None

    def visitar_pacientes(self, paciente):
        self.__paciente = paciente

    def registrar_observacoes(self, registro):
        self.__registro = registro


class Paciente(Pessoa):
    def __init__(self, cpf, rg, nome, endereco, telefone, data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.__rg = rg
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__quarto = None

    def set_quarto(self, quarto):
        self.__quarto = quarto


class Quarto():
    def __init__(self, numero, andar):
        self.__numero = numero
        self.__andar = andar


class Clinica():
    def __init__(self, medico, paciente):
        self.__medico = medico
        self.__paciente = paciente
        self.__historico_medico = None


class Historico():
    def __init__(self, medico):
        self.__data = None
        self.__horario = None
        self.__medico = medico

    def criar_historico(self, data, horario, observacao, medico):
        hist = {'medico': self.__medico.nome,
                'paciente': self.__medico.paciente.nome,
                'data': self.__data,
                'horario': self.__horario,
                'observacao': self.__medico.registro}
        print(hist)


med = Medico('11111', '22222', 'medico1', '11111111', '1800', ' Neuro')
paciente = Paciente('123456789', '3434343', 'Clarisberto',
                    'rua xxx', '11111', '111111111')
quarto1 = Quarto(1, 1)
clinica = Clinica(med, paciente)
med.visitar_pacientes(paciente)
med.registrar_observacoes('Óbito do paciente José')

paciente.set_quarto(quarto1)


historico = Historico(med)
historico.criar_historico('12-11-2010', '14:00', med.registro, med.nome)
