from django.contrib import admin
from .models import Produtos, Admin_login

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'preco', 'imagem', 'descricao',)
    
@admin.register(Admin_login)
class Admin_loginAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha',)
    
