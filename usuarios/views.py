from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def login(request):
    forms = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

            
            
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                return redirect('login')
        
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
