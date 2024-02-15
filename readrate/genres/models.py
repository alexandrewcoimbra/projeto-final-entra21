from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField(max_length=256)