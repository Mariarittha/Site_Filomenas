from django.contrib import admin
from django.urls import path
from Produtos.views import produtos_cadastrar, produtos_listar, index, detalhar_produto,total
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('acesso_restrito/', produtos_cadastrar, name='produtos_cadastrar'),
    path('listar/', produtos_listar,name='produtos_listar', ),
    path ('detalhar_produto/<int:id>', detalhar_produto, name='detalhar_produto'),
    path('teste/', total, name="total_produtos")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


