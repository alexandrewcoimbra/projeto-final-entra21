from django.contrib import admin
from .models import Livro

# Register your models here.
@admin.register(Livro)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "autor", "numero_paginas", "descricao", "genero", "imagem" ]
    exclude = ["slug"]
    ordering = ["-id"] # Padrão
    list_per_page = 100
    list_max_show_all = 1000