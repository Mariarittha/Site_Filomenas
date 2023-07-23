from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=120)
    marca = models.CharField(max_length=120, null='')
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='imagem')
    descricao = models.CharField(max_length=200)