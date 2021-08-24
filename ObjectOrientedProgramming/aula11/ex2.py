class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
class Cachorro(Animal):
    def emitir_som(self):
        print("o cachorro latiu")

class Gato(Animal):
    def emitir_som(self):
        print("o gato miou")

class Cavalo(Animal):
    def emitir_som(self):
        print("o cavalo relixu")
class Veterinario:
    def examinar(self, animal):
        animal.emitir_som()


# teste

dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato
