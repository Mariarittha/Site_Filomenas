from django.shortcuts import render, get_object_or_404,redirect
from .models import Produtos
from .forms import ProdutosForm


def index(request):
    total_produtos = Produtos.objects.count()
    
    context = {
        'total_produtos' : total_produtos,
    }
    return render(request,"produtos/index.html",context)

#criar

def produtos_cadastrar(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST, request.FILES)
        if form.is_valid():
            print("salvando")
            form.save()
            form = ProdutosForm()
    else:
        
        print('entrou primeiro aqui')
        form = ProdutosForm()

    return render(request, "area_administrativa/form.html", {'form': form})

#atualizar

def produto_editar(request,id):
    produto = get_object_or_404(Produtos,id=id)
   
    if request.method == 'POST':
        form = ProdutosForm(request.POST,request.FILES,instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos_listar')
    else:
        form = ProdutosForm(instance=produto)

    return render(request,'area_administrativa/form.html',{'form':form})

#apagar

def produto_remover(request, id):
    produto = get_object_or_404(Produtos, id=id)
    produto.delete()
    return redirect('produtos_listar') # procure um url com o nome 'produtos_listar'

def produtos_listar(request):
    produtos = Produtos.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "produtos/produtos.html",context)

def detalhar_produto(request, id):
    produtos = get_object_or_404(Produtos, id=id)
    context={'produtos' : produtos}
    
    return render(request,'produtos/detalhar.html', context)


def total(request):
    total_produtos = Produtos.objects.count()

    context = {
        'total_produtos' : total_produtos
    }
    return render(request, "area_administrativa/administrador.html",context)



