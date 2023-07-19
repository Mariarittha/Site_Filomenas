from django.contrib import admin
from django.urls import path
from Produtos.views import produstos_cadastrar, produtos_listar, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastrar/', produstos_cadastrar, name='produtos_cadatrar'),
    path('listar/', produtos_listar,name='produtos_listar', )
]
