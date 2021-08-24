class Cachorro:
    # construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade  = idade
        self.peso = None

    #metodos
    def andar(self, distancia):
        print(f"o cachorro andou {distancia} metros")
    def comer(self):
        print(f'o cachorro de nome {self.nome} comeu')
    def latir(self):
        print(f'o cachorro latiu')

    