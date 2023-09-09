from django.db import models

class Dado(models.Model):
    nome_setor = models.CharField(max_length=30)
    funcionarios = models.IntegerField(default=0)
    clientes = models.IntegerField(default=0)
    fornecedores = models.IntegerField(default=0)
    produtos = models.IntegerField(default=0)
    empresas_terceiras = models.IntegerField(default=0)
