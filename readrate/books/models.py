from django.db import models
from django.contrib.auth.models import User
from genres.models import Genero

class Livro(models.Model):
    titulo = models.CharField(max_length=256)
    slug = models.CharField(max_length=255, blank=True)
    autor = models.CharField(max_length=256)
    numero_paginas = models.IntegerField()
    descricao = models.CharField(max_length=256)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)  # Adicionando campo de imagem


class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.IntegerField()

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)