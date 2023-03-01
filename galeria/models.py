from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Fotografia(models.Model):
    
    # AS OPÇÕES DEVEM SER EM FORMATO DE TUPLA, POIS É A MANEIRA QUE O METODO CHARFIELD ENTENDE
    OPCOES_CATEGORIAS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    # TODA VEZ QUE O BANCO DE DADOS É ALTERADO (QUE O ARQUIVO MODEL.PY É ALTERADO), É NECESSÁRIO FAZER UMA MIGRATION NOVAMENTE
    # python manage.py makemigrations -> python manage.py migrate
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS,default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name="user")


    def __str__(self) -> str:
        return self.nome
