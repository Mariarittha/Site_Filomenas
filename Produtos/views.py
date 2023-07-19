from django.shortcuts import render
from .models import Produtos
from .forms import ProdutosForm

def produstos_cadastrar(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            print("Está salvando!")
            form = ProdutosForm()
    else:
        form = ProdutosForm()

    return render(request, "area_administrativa/form.html", {'form': form})

def produtos_listar(request):
    produtos = Produtos.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "produtos/index.html",context)

def index(request):
    return (request, "produtos/index.html")
