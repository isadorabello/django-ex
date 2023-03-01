from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages
# from django.http import HttpResponse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')


    fotografias = Fotografia.objects.order_by(
        "-data_fotografia").filter(publicada=True)
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/imagem.html', {"foto": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})
