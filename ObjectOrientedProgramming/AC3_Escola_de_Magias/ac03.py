# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 03

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO: Igor Luan Teles de Souza     
# RA: 1905365

#Fiz sozinho mesmo

class Escola:
    def __init__(self, nome,):
        self.nome = nome
        self.casas = []
    
    def incluir_casa(self, casa):
        self.casas.append(casa)



class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None #professor
        self.monitor = None #aluno


    def set_diretor(self, diretor):
        self.diretor = diretor 

    def set_monitor(self, aluno):
        self.monitor = aluno


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []
    
    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)        


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.casa = None  #classe Casa
        self.__triunfos = 0
        self.__mau_feitos = 0


    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos += quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos += quantidade

    def get_triunfos(self):
        return self.__triunfos
    
    def get_mau_feitos(self):
        return self.__mau_feitos


class Disciplina:
    def __init__(self,nome, ementa):
        self.ementa = ementa
        self.nome = nome
        self.alunos = [] #lsita de alunos

    
    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)

class Torneio:
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def marcar_ponto(self, casa, quantidade):
        if casa == self.casa1:
            self.__pontos_casa1 +=  quantidade
        else:
            self.__pontos_casa2 +=  quantidade
    
    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2
