import unittest
#from logica.calculosuma import SumaDosNumeros
from src.logica.calculosuma import SumaDosNumeros


class SumaNumeros(unittest.TestCase):
    def setUp(self):
        self.calcularsuma = SumaDosNumeros()
    
    def tearDown(self):
        self.calcularsuma = None
    
    def test_calcularsuma(self):
        a=3
        b=2
        resultado_esperado = 5
        resultado_actual = self.calcularsuma.sumandoNumeros(a,b)
        
        self.assertEqual(resultado_esperado, resultado_actual)

if __name__=='__main__':
    unittest.main()