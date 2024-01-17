# Generated by Django 5.0.1 on 2024-01-17 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_flashcarddesafio_desafio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desafio',
            name='quantidade_perguntas',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]