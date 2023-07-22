from django.shortcuts import render, get_object_or_404,redirect
from .models import Produtos
from .forms import ProdutosForm


def index(request):
    total_produtos = Produtos.objects.count()
    
    context = {
        'total_produtos' : total_produtos,
    }
    return render(request,"produtos/index.html",context)

def produtos_cadastrar(request):
    if request.method == 'POST':
        print('entrou')
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
    return render(request, "produtos/produtos.html",context)
