class Calcular():
    def __init__(self, medidas):
        self.medidadas = medidas

    def calcular_area(self):
        self.medidas = 3.14*(self.medidas.get_raio()**2)
        return(self.medidas)
    def calcular_volume(self):
        self.medidas= 3.14*(self.medidas.get_raio()**2)*self.medidas.get_altura()
        return self.medidas
    

