from django.contrib import admin
from django.urls import path
from Produtos.views import produtos_cadastrar, produtos_listar, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastrar/', produtos_cadastrar, name='produtos_cadastrar'),
    path('listar/', produtos_listar,name='produtos_listar', )
]
