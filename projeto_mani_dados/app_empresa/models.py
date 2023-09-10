from django.db import models

class Dado(models.Model):
    nome_setor = models.CharField(max_length=30)
    funcionarios = models.IntegerField(blank=True, null=True)
    clientes = models.IntegerField(blank=True, null=True)
    fornecedores = models.IntegerField(blank=True, null=True)
    produtos = models.IntegerField(blank=True, null=True)
    empresas_terceiras = models.IntegerField(blank=True, null=True)