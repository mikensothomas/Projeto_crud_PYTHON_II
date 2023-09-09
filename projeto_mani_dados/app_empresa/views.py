from django.shortcuts import render
from .models import Dado

def home(request):
    return render(request,'dados/home.html')

def dados(request):
    novo_dado = Dado()
    novo_dado.nome_setor = request.POST.get('nome_setor')
    novo_dado.funcionarios = request.POST.get('funcionarios')
    novo_dado.clientes = request.POST.get('clientes')
    novo_dado.fornecedores = request.POST.get('fornecedores')
    novo_dado.produtos = request.POST.get('produtos')
    novo_dado.empresas_terceiras = request.POST.get('empresas_terceiras')
    novo_dado.save()

    dados = {
        'dados': Dado.objects.all()
    }

    return render(request,'dados/dados.html',dados)