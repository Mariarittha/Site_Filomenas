from django.forms import ModelForm
from django import forms
from .models import Produtos

class ProdutosForm(ModelForm):

    class Meta:
        model = Produtos
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'marca' : forms.TextInput(attrs={'class': 'form-control' }),
            'preco' : forms.EmailInput(attrs={'class': 'form-control' }),
            'imagem': forms.Select(attrs={'class': 'form-control' }),
            'descricao': forms.FileInput(attrs={'class': 'form-control' })
        }