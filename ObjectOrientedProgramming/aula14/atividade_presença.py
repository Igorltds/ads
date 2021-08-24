import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE. Caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
# Criação da sessão
session = Session()

# tabelas

connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        CPF VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL)
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        CRM VARCHAR(255) NOT NULL,
                        ESPECIALIZACAO VARCHAR(255) NOT NULL)
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INT NOT NULL,
                        ID_PACIENTE INT NOT NULL,
                        DESCRICAO VARCHAR(255) NOT NULL,
                        RESULTADO VARCHAR(255) NOT NULL)
                    """)

# classes associadas as tabelas


class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    cpf = Column('CPF', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    crm = Column('CRM', String(255), nullable=False)
    especializacao = Column('ESPECIALIZACAO', String(255), nullable=False)

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer, nullable=False)
    id_paciente = Column('ID_PACIENTE', Integer, nullable=False)
    descricao = Column('DESCRICAO', String(255), nullable=False)
    resultado = Column('RESULTADO', String(255), nullable=False)

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


# criar medicos e pacientes
medico01 = Medico("Rodolfo da Silva", "12345", "cardiologista")
paciente01 = Paciente("João souza", "245646546", 30)
paciente02 = Paciente("Maria Silva", "567878787", 25)

# inserir dados
session.add(medico01)
session.add(paciente01)
session.add(paciente02)
session.commit()
# criar exame

exame01 = Exame(medico01.id, paciente01.id, "PCR COVID_19", "Negativo")
exame02 = Exame(medico01.id, paciente02.id, "Eletrocardiograma", "Normal")

# inserir dados

session.add(exame01)
session.add(exame02)
session.commit()

# Realiza consultas
lista_paciente = session.query(Paciente).order_by(Paciente.nome).all()
lista_medico = session.query(Medico).all()
lista_exames = session.query(Exame).all()


# exibe resultados
print("--" * 15)
for p in lista_paciente:
    print(p.id, p.nome, p.cpf, p.idade)

print("--" * 15)
for m in lista_medico:
    print(m.id, m.nome, m.crm, m.especializacao)

print('---' * 10)
for e in lista_exames:
    print("exame", e.id, "medico", e.id_medico, "paciente", e.id_paciente,
          "\ndescriação", e.descricao, "\nresultado", e.resultado, "\n")


# Fechar conexão com banco de dados
connection.close()
