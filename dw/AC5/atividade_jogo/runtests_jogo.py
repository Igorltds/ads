import unittest
from jogo import Jogo

class TestStringMethods(unittest.TestCase):

    def test_00_jogo_guarda_chutes(self):
        j = Jogo()
        j.chutar(12)
        j.chutar(50)
        self.assertEqual(j.chutes,[12,50])

    def test_01_jogo_guarda_maior_e_menor(self):
        j = Jogo()
        j.alvo = 50
        j.chutar(75)
        self.assertEqual(j.maior,74)
        self.assertEqual(j.menor,0)
        j.chutar(30)
        self.assertEqual(j.maior,74)
        self.assertEqual(j.menor,31)
        j.chutar(42)
        self.assertEqual(j.maior,74)
        self.assertEqual(j.menor,43)
        j.chutar(50)
        self.assertEqual(j.maior,50)
        self.assertEqual(j.menor,50)

    def test_02_jogo_gera_alvo(self):
        j = Jogo()
        self.assertTrue(0 <= j.alvo <= 100)

    def test_03_resumo_do_jogo(self):
        j = Jogo()
        j.alvo = 60
        j.chutar(75)
        self.assertEqual(j.resumo(),"Seu ultimo chute foi alto! Estamos entre 0 e 74")
        j.chutar(30)
        self.assertEqual(j.resumo(),"Seu ultimo chute foi baixo! Estamos entre 31 e 74")
        j.chutar(42)
        self.assertEqual(j.resumo(),"Seu ultimo chute foi baixo! Estamos entre 43 e 74")
        j.chutar(50)
        self.assertEqual(j.resumo(),"Seu ultimo chute foi baixo! Estamos entre 51 e 74")
        j.chutar(60)
        self.assertEqual(j.resumo(),"Você fez um chute correto! Você acertou! Parabéns!")

        



def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
