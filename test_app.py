import unittest
from app import app

class TestServico(unittest.TestCase):
    def test_status_ativo(self):
        cliente = app.test_client()
        resposta = cliente.get("/")
        dados = resposta.get_json()

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(dados["status"], "Serviço ativo")

if __name__ == "__main__":
    unittest.main()
