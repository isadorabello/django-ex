from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
# from django.http import HttpResponse

# Create your views here.

def index(request):
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
