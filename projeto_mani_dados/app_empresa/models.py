from django.db import models

class Dado(models.Model):
    funcionarios = models.IntegerField(default=0)
    clientes = models.IntegerField(default=0)
    fornecedores = models.IntegerField(default=0)
    produtos = models.IntegerField(default=0)
    empresas_terceiras = models.IntegerField(default=0)
