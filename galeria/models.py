from django.db import models

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
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"Fotografia [nome={self.nome}]"
