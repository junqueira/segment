from django.db import models


class Bairro(models.Model):
    codigo = models.BigIntegerField(primary_key=True)  # AutoField?
    nome = models.TextField()
    municipio = models.TextField()
    uf = models.TextField()
    area = models.TextField()


class Concorrente(models.Model):
    codigo = models.BigIntegerField(primary_key=True)  # AutoField?
    nome = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    faixa_preco = models.TextField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    uf = models.TextField(blank=True, null=True)
    codigo_bairro = models.TextField(blank=True, null=True)