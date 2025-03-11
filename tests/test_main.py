import unittest
from src.main import solicitar_corrida

class TesteCorrida(unittest.TestCase):
    def test_solicitacao_corrida(self):
        usuario = "Carlos"
        local_partida = "Rua A"
        destino = "Aeroporto"
        resultado = solicitar_corrida(usuario, local_partida, destino)
        self.assertIn(resultado, [True, None])

if __name__ == "__main__":
    unittest.main()
