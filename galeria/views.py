from django.shortcuts import render
from galeria.models import Fotografia
# from django.http import HttpResponse

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.all()
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request):
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/imagem.html')
