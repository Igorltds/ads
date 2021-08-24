from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass