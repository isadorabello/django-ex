from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms

# Create your views here.


def login(request):
    forms = LoginForms()
    return render(request, 'usuarios/login.html', {"form": forms})


def cadastro(request):
    forms = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form["senha"].value() != form["senhaConfirmar"].value():
            return redirect('cadastro')


    return render(request, 'usuarios/cadastro.html', {"form": forms})


def logout(request):
    pass
