from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class Listando(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10

# Registrou o bando de dados no Admin
admin.site.register(Fotografia, Listando)
