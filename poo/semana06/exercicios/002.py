class Triangulo:
    def _init_(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b 
        self.lado_c = lado_c
    
    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

a = float(int(input("medida do primeiro lado: ")))
b = float(int(input("medida do segundo lado: ")))
c = float(int(input("medida do terceiro lado: ")))

triangulo = Triangulo(a, b, c) 
print(triangulo.calcular_perimetro())
