import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


# Abre o arquivo de texto
arquivo = open("funcionarios.txt", "r", encoding='UTF-8')

lista_funcionario = []

# percorre o arquivo de texto
for linha in arquivo:
    lista = linha.split(';')

    # cria o objeto
    func = Funcionario(lista[0], int(lista[1]), float(lista[2]))
    # insere objeto na lista
    lista_funcionario.append(func)

# insere os objetos da lista no banco de dados
session.add_all(lista_funcionario)
session.commit()

# realiza a consulta na tabela
resultado = session.query(Funcionario).all()
for r in resultado:
    print(r.id, r.nome, r.idade, r.salario)

arquivo.close()
connection.close()