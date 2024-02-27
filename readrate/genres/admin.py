from django.contrib import admin
from .models import Genero

# Register your models here.
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    ordering = ["-id"] # Padrão
    list_per_page = 100
    list_max_show_all = 1000