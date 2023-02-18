from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    dados = {
        1: {"nome": "Um nome aleatorio", "legenda": "fonte.vozes.da.minha.cabeça.org"},
        2: {"nome": "Um nome pouco comum", "legenda": "fonte.instituto.CDMR.org"}
    }
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/index.html', {"cards": dados})


def imagem(request):
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/imagem.html')
