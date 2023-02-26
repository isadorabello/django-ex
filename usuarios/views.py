from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    forms = LoginForms()
    return render(request, 'usuarios/login.html', {"form": forms})


def cadastro(request):
    forms = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha"].value() != form["senha_confirmar"].value():
                return redirect('cadastro')
            
            nome = form["nome_cadastro"].value()
            email = form["email_cadastro"].value()
            senha = form["senha"].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": forms})


def logout(request):
    pass
