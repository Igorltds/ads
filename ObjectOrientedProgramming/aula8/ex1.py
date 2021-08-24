class Pacote:
    def __init__(self, nome_remetente, endereco_remetente, nome_destinatario, endereco_destinataio, peso, preco):
        self.nome_destinatario =  nome_destinatario
        self.endereco_destinataio = endereco_destinataio 
        self.nome_remetente = nome_remetente
        self.endereco_remetente = endereco_remetente
        self.__peso = peso
        self.__preco = preco

    def get_peso(self):
        return self.__peso
    def get_preco(self):
        return self.__preco
    def calcular_custo(self):
        return self.__peso * self.__preco



class PacoteDoisDias(Pacote):
    def __init__(self, nome_remetente, endereco_remetente, nome_destinatario, endereco_destinataio, peso, preco, adicional):
        super(). __init__(nome_remetente, endereco_remetente, nome_destinatario, endereco_destinataio, peso, preco)
        self.__adicional = adicional
    
    def  calcular_custo(self):
        return super().calcular_custo() + self.__adicional



class PacoteMesmoDia(Pacote):
    def __init__(self, nome_remetente, endereco_remetente, nome_destinatario, endereco_destinataio, peso, preco, adicional):
        super(). __init__(nome_remetente, endereco_remetente, nome_destinatario, endereco_destinataio, peso, preco)
        self.__adicional = adicional

    def  calcular_custo(self):
        return super().calcular_custo() + self.__adicional * self.get_peso()



pacote1 = Pacote("Paulo Vieira", "Avenida Brasil, 123, São Paulo",
                 "João Silva", "Rua Qualquer, 67", 1.5, 10.0)
pacote2 = PacoteDoisDias("Paulo Vieira", "Avenida Brasil, 123, São Paulo",
                         "João Silva", "Rua Qualquer, 67", 1.5, 10.0, 7.5)
pacote3 = PacoteMesmoDia("Paulo Vieira", "Avenida Brasil, 123, São Paulo",
                         "João Silva", "Rua Qualquer, 67", 1.5, 10.0, 7.5)
print("Custo do Pacote 1:", pacote1.calcular_custo())
print("Custo do Pacote 2:", pacote2.calcular_custo())
print("Custo do Pacote 3:", pacote3.calcular_custo())