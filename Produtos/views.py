from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Produtos
from .forms import ProdutosForm
from  django.contrib.auth import authenticate
from  django.contrib.auth import login as loginho
from django.contrib.auth.models import User
from django.contrib import messages




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
    return redirect('produtor_listar_admin') # procure um url com o nome 'produtos_listar'

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
    return render(request, "area_administrativa/areaAdmin.html",context)

def login(request):
     if request.method == 'GET':
         return render(request, 'area_administrativa/login.html')
     else:
         username = request.POST.get('username')
         senha = request.POST.get('senha')
        
         user = authenticate(username = username, password = senha)
        
         if user:
             loginho(request, user)
             return redirect('produtor_listar_admin')
         else:
              messages.error(request,'username ou senha inválida') 
         return redirect('login')
        

def produtos_listar_admin(request):
    produtos = Produtos.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "area_administrativa/areaAdmin.html",context)

        
def plataforma(request):
    if request.user.is_authenticated:
        
        return render(request,'area_administrativa/areaAdmin.html')
    
    return HttpResponse('voce precisa estar logado!')

# def login(request): 
#     if request.method == 'GET':
#         username = request.POST.get('username')
#         senha = request.POST.get('senha')
        
        
#         user = authenticate(username=username, password=senha)
        
#         if user: 
#             loginho(request, user) 
#             return redirect('produtor_listar_admin') 
#         else: 
#             messages.error(request,'username ou senha inválida') 
#         return redirect('login') 