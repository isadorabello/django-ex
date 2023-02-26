from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

# Create your views here.


def login(request):
    forms = LoginForms()
    return render(request, 'usuarios/login.html', {"form": forms})


def cadastro(request):
    forms = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {"form": forms})


def logout(request):
    pass
