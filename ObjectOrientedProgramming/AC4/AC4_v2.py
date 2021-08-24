from abc import ABC

'''classe Pessoa'''
class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone 


    def get_nome(self):              #set e get, nome
        return self.__nome


    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_cpf(self):              #set e get, cpf
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_telefone(self):               #set e get, telefone
        return self.__telefone

    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone

'''classe Medico'''
class Medico(Pessoa):
    def __init__(self, crm, cpf, nome, telefone, salario, especialidade):
        super().__init__(nome, cpf, telefone)
        self.__crm = crm
        self.__salario = salario
        self.__especialidade = especialidade

    #metodos comuns
    def registrar_observacoes(self, registro):
        self.__registro.append(registro)


    #set get
    def get_crm(self):              #set e get, crm
        return self.__crm
    def set_crm(self, novo_crm):
        self.__crm = novo_crm

    def get_salario(self):              #set e get, salario
        return self.__salario
    def set_salario(self, novo_salario):
        self.__salario = novo_salario

    def get_especialidade(self):              #set e get, especialidade
        return self.__especialidade
    def set_especialidade(self, novo_especialidade):
        self.__especialidade = novo_especialidade
    
    def get_paciente(self):              #set e get, paciente
        return self.__paciente
    def set_paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    def get_registro(self):              #set e get, registro
        return self.__registro
    def set_registro(self, novo_registro):
        self.__registro = novo_registro

'''class Paciente'''
class Paciente(Pessoa):
    def __init__(self, cpf, rg, nome, endereco, telefone, data_nascimento, quarto):
        super().__init__(nome, cpf, telefone)
        self.__rg = rg
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__quarto = quarto


    def get_rg(self):              #set e get, rg
        return self.__rg
    def set_rg(self, novo_rg):
        self.__rg = novo_rg

    def get_endereco(self):              #set e get, endereço
        return self.__endereco

    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    def get_data_nascimento(self):              #set e get, data de nascimento
        return self.__data_nascimento  

    def set_data_nascimento(self, novo_data_nascimento ):
        self.__data_nascimento  = novo_data_nascimento  

    def get_quarto(self):              #set e get, quarto
        return self.__quarto

    def set_quarto(self, novo_quarto):
        self.__quarto = novo_quarto

'''class Quarto'''
class Quarto():
    def __init__(self, numero, andar):
        self.__numero = numero
        self.__andar = andar

    def get_numero(self):              #set e get, numero
        return self.__numero

    def set_numero(self, novo_numero):
        self.__numero = novo_numero

    def get_andar(self):              #set e get, andar
        return self.__andar

    def set_andar(self, novo_andar):
        self.__andar = novo_andar

'''classe Clinica'''
class Clinica():
    def __init__(self, medico, paciente):
        self.__medico = medico
        self.__paciente = paciente
        self.__historico_medico = []

    def get_medico(self):              #set e get, medico
        return self.__medico

    def set_medico(self, novo_medico):
        self.__medico = novo_medico
    
    def get_paciente(self):              #set e get, paciente
        return self.__paciente

    def set_paciente(self, novo_paciente):
        self.__paciente = novo_paciente

    def get_historico_medico(self):              #set e get, historico_medico
        return self.__historico_medico
        
    def set_historico_medico(self, novo_historico_medico):
        self.__historico_medico = novo_historico_medico

'''classe Historico'''
class Historico():
    def __init__(self, medico, paciente):
        self.__medico = medico
        self.__paciente = paciente
        self.__registro_observacoes = []
    
    def append_observacoes(self,  medico, data, horario, observacao):        #novo registro
        observacao= {'data': data,
                     'horario': horario,
                     'observacao': observacao,
                     'medico': medico.get_nome()
                     }
        self.__registro_observacoes.append(observacao)    

    def get_data(self):              #set e get, data
        return self.__data
        
    def set_data(self, novo_data):
        self.__data = novo_data

    def get_horario(self):              #set e get, horario
        return self.__horario
        
    def set_horario(self, novo_horario):
        self.__horario = novo_horario

    def get_medico(self):              #set e get, medico
        return self.__medico
        
    def set_medico(self, novo_medico):
        self.__medico = novo_medico







quarto01 = Quarto(1, 1)
med01 = Medico('46546crm', '454.545.458-92', 'medico1', '+55 11 97834982743', '19999R$', 'Neuro')
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
historico_paciente01.append_observacoes(med01, "07/07/2007", "12:40", "apresenta melhoras! :)")

quarto02 = Quarto(2, 1)

#paciente01.set_quarto(quarto02)
#print(paciente01.get_quarto().get_numero())