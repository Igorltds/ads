import unittest
import requests

data = "dia 21 do mês 5"


class TestStringMethods(unittest.TestCase):

    def test_01_lista(self):
         requests.post("http://localhost:5000/reseta")
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Helena"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Gertrudes"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Zé"})
         r1 = requests.get("http://localhost:5000/sorteio")
         if "Maria1" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "Helena" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "Gertrudes" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "Zé" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "ol" not in r1.text:
             self.fail("Você não montou uma lista ordenada html")
         if "li" not in r1.text:
             self.fail("Você não montou uma lista ordenada html")

    def test_01a_lista(self):
         requests.post("http://localhost:5000/reseta")
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria2"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria3"})
         r1 = requests.get("http://localhost:5000/sorteio")
         if "Maria1" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "Maria2" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "Maria3" not in r1.text:
             self.fail("A lista não contém um aluno")
         if "Maria4" in r1.text:
             self.fail("A lista contém um aluno que não deveria aparecer")
         if "ol" not in r1.text:
             self.fail("Você não montou uma lista ordenada html")
         if "li" not in r1.text:
             self.fail("Você não montou uma lista ordenada html")


    def test_02a_destaque(self):
         requests.post("http://localhost:5000/reseta")

         r_inicial = requests.get("http://localhost:5000/sorteio")
         
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria2"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria3"})
         requests.post("http://localhost:5000/alunos", data={"nome": "JoaoV"})

         requests.post("http://localhost:5000/ganhador", data={"nome": "JoaoV"})

         r2 = requests.get("http://localhost:5000/sorteio")
         if r2.text.count("destaque") - r_inicial.text.count("destaque") != 1:
             self.fail("Ganhador não foi destacado")#so apareceu no CSS
         

    def test_02b_destaque(self):
         requests.post("http://localhost:5000/reseta")

         r_inicial = requests.get("http://localhost:5000/sorteio")
        

         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria2"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria3"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria4"})
         r3 = requests.get("http://localhost:5000/sorteio")
         if r3.text.count("destaque") - r_inicial.text.count("destaque") != 0:
             self.fail("Nao devia, mas alguem foi destacado")
    

    def test_02c_destaque(self):
         requests.post("http://localhost:5000/reseta")

         r_inicial = requests.get("http://localhost:5000/sorteio")

         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria2"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria3"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria4"})

         requests.post("http://localhost:5000/ganhador", data={"nome": "JoaoV"})

         r4 = requests.get("http://localhost:5000/sorteio")
         if r4.text.count("destaque") - r_inicial.text.count("destaque") != 0:
             self.fail("Nao devia, mas alguem foi destacado")



    def test_3a_data(self):
         requests.post("http://localhost:5000/reseta")
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria2"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria3"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria4"})

         requests.post("http://localhost:5000/ganhador", data={"nome": "Maria2"})


         r4 = requests.get("http://localhost:5000/sorteio")
         #aviso: vou mudar a data antes de testar, garanta 
         #que seu código realmente consulta a data atual
         if r4.text.count(data) == 0:
             self.fail("A data não apareceu, mas devia")


    def test_3b_data(self):
         requests.post("http://localhost:5000/reseta")
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria1"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria2"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria3"})
         requests.post("http://localhost:5000/alunos", data={"nome": "Maria4"})

         requests.post("http://localhost:5000/ganhador", data={"nome": "JoaoV"})


         r4 = requests.get("http://localhost:5000/sorteio")
         #aviso: vou mudar a data antes de testar, garanta 
         #que seu código realmente consulta a data atual
         if r4.text.count(data) == 1:
             self.fail("Ganhador inválido, mas a data apareceu")


     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
