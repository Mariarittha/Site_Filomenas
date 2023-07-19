from django.contrib import admin
from .models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'preco', 'imagem', 'descricao',)