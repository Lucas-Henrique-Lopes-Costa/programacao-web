from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.autor}" 
    
class TCC(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    orientador = models.CharField(max_length=255)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class QuantitativoMateriais(models.Model):
    livros = models.IntegerField()
    tccs = models.IntegerField()
    dissertacoes = models.IntegerField()
    teses = models.IntegerField()
    apostilas = models.IntegerField()
    jornais = models.IntegerField()

    def __str__(self):
        return f"{self.livros} - {self.tccs} - {self.dissertacoes} - {self.teses} - {self.apostilas} - {self.jornais}"