from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.utils.text import slugify

class Genero(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        super().save(*args, **kwargs)
    
class Autor(models.Model):
    nome = models.CharField(max_length=256, unique=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        super().save(*args, **kwargs)
class Livro(models.Model):
    titulo = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, blank=True)
    numero_paginas = models.IntegerField()
    autores = models.ManyToManyField(Autor)
    generos = models.ManyToManyField(Genero)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.IntegerField()

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)