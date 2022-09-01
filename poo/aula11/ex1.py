from abc import ABC, abstractmethod

class Operação(ABC):
    @abstractmethod 
    def calcular(self, x,y):
        pass


class Soma(Operação):
    def calcular(self, x, y):
        return x + y

class Subtração(Operação):
    def calcular(self, x, y):
        return x-y

class Multiplicação(Operação):
    def calcular(self, x, y):
        return x*y

class Divisão(Operação):
    def calcular(self, x, y):
        if y != 0:
            return x/y
        else:
            print ("Denominador é zero")
            return None


#teste
soma = Soma()
sub = Subtração()
div = Divisão()
mult = Multiplicação()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50
 