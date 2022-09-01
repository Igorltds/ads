import unittest
import requests

class TestStringMethods(unittest.TestCase):

     def test_01_soma(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"soma"})
         if "30" not in r1.text:
             self.fail("a soma de 10 com 20 deveria ter dado trinta")

     def test_02_divisao(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"div"})
         if "0.5" not in r1.text:
             self.fail("10/20 deveria ter dado 0.5")

     def test_03_mult(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"mult"})
         if "20" not in r1.text:
             self.fail("o produto de 10 com 20 deveria ter dado 200")

     def test_04_sub(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':30,"b":20, "ope":"sub"})
         if "10" not in r1.text:
             self.fail("subtrair 20 de 30 deveria ter dado 10")

     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()