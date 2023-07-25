from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=120)
    marca = models.CharField(max_length=120, null='')
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='imagem')
    descricao = models.CharField(max_length=200)
    
    
class Admin_login(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    senha = models.IntegerField()
    