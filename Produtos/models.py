from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=120)
    marca = models.CharField(max_length=120)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='imagens')
    descricao = models.CharField(max_length=200)