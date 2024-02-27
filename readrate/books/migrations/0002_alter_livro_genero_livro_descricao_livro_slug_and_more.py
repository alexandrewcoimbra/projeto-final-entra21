# Generated by Django 5.0.1 on 2024-02-13 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genres.genero'),
        ),
        migrations.AddField(
            model_name='livro',
            name='descricao',
            field=models.CharField(default=1010100, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='slug',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]