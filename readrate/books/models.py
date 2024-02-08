from django.db import models
from django.contrib.auth.models import User

class Genero(models.Model):
    nome = models.CharField(max_length=256)

class Livro(models.Model):
    titulo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    numero_paginas = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.IntegerField()

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)