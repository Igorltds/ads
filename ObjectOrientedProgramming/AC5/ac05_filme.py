'''    Atividade Continua 05   '''
# Aluno 1: Igor Luan Teles de souza 
# RA: 1905365

import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()


class Filme(Base):
    __tablename__ = 'FILME'
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    titulo = Column("TITULO", String(255), nullable=False)
    ano = Column("ANO", Integer, nullable=False)
    genero = Column("GENERO", String(255), nullable=False)
    duracao = Column("DURACAO", Integer, nullable=False)
    pais = Column("PAIS", String(255), nullable=False)
    diretor = Column("DIRETOR", String(255), nullable=False)
    elenco = Column("ELENCO", String(255), nullable=False)
    avaliacao = Column("AVALIACAO", Float, nullable=False)
    votos = Column("VOTOS", Integer, nullable=False)

    def __init__(self, titulo, ano, genero, duracao,
                 pais, diretor, elenco, avaliacao, votos):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


class BancoDeDados:
    def criar_tabela(self):
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255) NOT NULL,
                              ANO INT NOT NULL,
                              GENERO VARCHAR(255) NOT NULL,
                              DURACAO INT NOT NULL,
                              PAIS VARCHAR(255) NOT NULL,
                              DIRETOR VARCHAR(255) NOT NULL,
                              ELENCO VARCHAR(255) NOT NULL,
                              AVALIACAO FLOAT NOT NULL,
                              VOTOS INT NOT NULL)""")

    def incluir(self, filme):
        session.add(filme)
        session.commit()
        return

    def incluir_lista(self, filmes):
        session.add_all(filmes)
        session.commit()
        return

    def alterar_avaliacao(self, id, avaliacao):
        if id is not None:
            session.execute
            (update(Filme)
             .where(Filme.id == id)
             .values(avaliacao=avaliacao))
            session.commit()
        return

    def excluir(self, id):
        session.execute
        (delete(Filme)
         .where(Filme.id == id))
        session.commit()
        return

    def buscar_por_id(self, id):
        bp_id = session.query(Filme).get(id)
        return BP_id

    def buscar_todos(self):
        bp_id = session.query(Filme).order_by(Filme.titulo).all()
        return bp_id

    def buscar_por_ano(self, ano):
        bp_ano = session.query(Filme).filter(
            Filme.ano == ano).order_by(Filme.id)
        return bp_ano

    def buscar_por_genero(self, genero):
        bp_genero = session.query(Filme).filter(
            Filme.genero.contains(genero)).order_by(Filme.titulo).all()
        return bp_genero

    def buscar_por_pais(self, pais):
        bp_pais = session.query(Filme).filter(
            Filme.pais.contains(pais)).order_by(Filme.ano).all()
        return bp_pais

    def buscar_melhores_do_ano(self, ano):
        bp_m_ano = session.query(Filme).filter(
            Filme.ano == ano, Filme.avaliacao > 74).order_by(desc(Filme.avaliacao)).all()
        return bp_m_ano

    def importar_filmes(self, nome_arquivo):
        lista_filmes = []
        arquivo = open('movies.txt', 'r', encoding='UTF-8')
        for line in arquivo:
            titulo, ano, genero, duracao, pais, diretor, elenco, avaliacao, votos = line.split(
                ';')
            filme = Filme(titulo, int(ano), genero, int(duracao),
                          pais, diretor, elenco, float(avaliacao), int(votos))
            lista_filmes.append(filme)
        arquivo.close()
        session.add_all(lista_filmes)
        session.commit()
        pre_import = session.query(Filme)
        return


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()

# Importa filmes do arquivo de texto e salva no banco de dados
banco.importar_filmes('movies.txt')

# Cria um novo Filme e insere no banco de dados
filme1 = Filme("Parasite", 2019, "Comedy, Drama, Thriller", 132, "Korea",
               "Bong Joon Ho", "Song Kang-ho, Jang Hye-jin, Choi Woo-shik",
               92, 40273)
banco.incluir(filme1)

# Cria uma lista com dois novos filmes e insere no banco de dados
filme2 = Filme("Joker", 2019, 'Crime, Drama, Thriller', 122, "USA",
               "Todd Phillips", "Joaquin Phoenix, Robert De Niro, Zazie Beetz",
               91, 78481)
filme3 = Filme("Avengers: Endgame", 2019, 'Drama, Thriller', 181, "USA",
               "Anthony Russo, Joe Russo",
               "Robert Downey Jr.,Chris Evans, Mark Ruffalo", 93, 715250)
lista_filmes = [filme2, filme3]
banco.incluir_lista(lista_filmes)

# Altera a avalação do filme de id 7 para 98
banco.alterar_avaliacao(7, 98)

# Exclui o filme de id 6
banco.excluir(6)

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
print('todos')
for f in lista:         # Exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao,
          f.pais, f.diretor, f.elenco, f.avaliacao, f.votos, '\n')

# Busca todos os filmes do ano de 2019
lista = banco.buscar_por_ano(2019)
print('-'*60)
print('2019')
for f in lista:         # Exibe lista de filmes
    print(f.id, f.titulo, f.ano)

# Busca todos os filmes do gênero 'Crime'
lista = banco.buscar_por_genero('Crime')
print('-'*60)
print('genero')
for f in lista:         # Exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)

# Busca todos os filmes do país 'Brazil'
lista = banco.buscar_por_pais('Brazil')
print('-'*60)
print('pais')
for f in lista:         # Exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.pais)

# Busca os melhores filmes do ano de 2019
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
print('melhores')
for f in lista:         # Exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.avaliacao)

connection.close()
