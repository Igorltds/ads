class AnimalTerrestre:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def andar(self):
        print("andando")
    def comer(self):
        print("comendo na superficie")

class AnimalAquatico:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def nadar(self):
        print("nadando")
    def comer(self):
        print("comendo ná agua")


class AnimalAnfibio(AnimalAquatico, AnimalTerrestre):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)


onintorrinco = AnimalAnfibio("pery", "40 cm")
onintorrinco.andar()
onintorrinco.nadar()
onintorrinco.comer()