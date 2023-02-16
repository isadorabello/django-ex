from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/index.html')


def imagem(request):
    # função que responde a requisição HTTP da página WEB
    # HttpResponse('<h1>Web Test</h1>')
    return render(request, 'galeria/imagem.html')
