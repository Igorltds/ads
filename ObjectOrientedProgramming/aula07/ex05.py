class Paciente:
    def __init__(self, name, fone, age):
        self.name = name
        self.fone = fone
        self.age = age

class Medico:
    def __init__(self, name, crm, espec):
        self.name = name
        self.crm = crm
        self.espec = espec


class Exame:
    def __init__(self, medico, paciente, descrição, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descrição = descrição
        self.resultado = resultado

    def imprimir_exame(self):
        print("Medico: ", self.medico.name, self.medico.crm, self.medico.espec,
              "\nPaciente: ", self.paciente.name, self.paciente.fone, self.paciente.age,
              "\nDescriação: ", self.descrição,
              "\nResultado: ", self.resultado)

        

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')  
exame01.imprimir_exame()						
# Deve exibir relatório com os dados do exame (inclusive os do médico e do paciente)
