from django.contrib import admin
from django.urls import path
from Produtos.views import produtos_cadastrar, produtos_listar, index, detalhar_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('acesso_restrito/', produtos_cadastrar, name='produtos_cadastrar'),
    path('listar/', produtos_listar,name='produtos_listar', ),
    path ('detalhar_produto/<int:id>', detalhar_produto, name='detalhar_produto')
]
