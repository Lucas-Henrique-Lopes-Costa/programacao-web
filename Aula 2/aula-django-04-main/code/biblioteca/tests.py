from django.test import TestCase
from .models import Livro
from .models import TCC

class ModeloTestCase(TestCase):
    def setUp(self):
        Livro.objects.create(nome="Introdução ao Django", autor="João Silva", ano=2024)
        TCC.objects.create(titulo="Análise de Sistemas Web", autor="José Carvalho", orientador="Prof. Carlos Souza", ano=2023)

    def test_criacao_e_conteudo_livro(self):
        livro = Livro.objects.get(nome="Introdução ao Django")
        self.assertEqual(livro.autor, "João Silva")
        self.assertEqual(livro.ano, 2024)

    def test_criacao_e_conteudo_tcc(self):
        tcc = TCC.objects.get(titulo="Análise de Sistemas Web")
        self.assertEqual(tcc.autor, "José Carvalho")
        self.assertEqual(tcc.orientador, "Prof. Carlos Souza")
        self.assertEqual(tcc.ano, 2023)