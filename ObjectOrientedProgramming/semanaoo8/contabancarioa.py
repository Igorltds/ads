class Contabancaria:
    def __init__(self, numero, titular,senha, pix):
        self.numero = numero
        self.titular = titular
        self.pix = pix
        self.__senha = senha 
        self.__saldo = 0


    def depositar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor
            print("dinehiro somado ao saldo")
        else:
            print("Senha Inválida")
    
    def sacar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo -= valor
            print("dinheiro subtraido do saldo")
        else: 
            print("senha inválida")
    
    def get_saldo(self, senha):
        return self.__saldo



contadoigor = Contabancaria(654654, "Igor Luan Teles de Souza", 12345678, "pixpix@pixpix.pix.pix")
contadoigor.depositar(10,123456789)
contadoigor.depositar(700, 12345678)
contadoigor.sacar(7, 12345678)
contadoigor.sacar(3, 123456789)
print(contadoigor.get_saldo(12345678))