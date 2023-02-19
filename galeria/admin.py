from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class Listando(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

# Registrou o bando de dados no Admin
admin.site.register(Fotografia, Listando)
