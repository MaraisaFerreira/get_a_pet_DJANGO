from django.db import models
from django.core.validators import MinValueValidator
from datetime import date


class Pet(models.Model):

    name = models.CharField(max_length=80)

    COLOR_CHOICES = [
        ('white', 'Branco'),
        ('black', 'Preto'),
        ('yellow', 'Amarelo'),
        ('tricolor', 'Tricolor'),
        ('white_yellow', 'Branco e Amarelo'),
        ('black_white', 'Preto e Branco'),
    ]
    color = models.CharField(
        max_length=16,
        choices=COLOR_CHOICES,
        default=COLOR_CHOICES[0][0]
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    AGE_CHOICES = [
        ('days', 'Dias'),
        ('months', 'Meses'),
        ('years', 'Anos'),
    ]
    age_type = models.CharField(
        max_length=6,
        choices=AGE_CHOICES,
        default=AGE_CHOICES[0][0]
    )

    TYPE_CHOICES = [
        ('cat', 'Gato'),
        ('dog', 'Cachorro'),
        ('hamster', 'Hamster'),
        ('rabbit', 'Coelho'),
        ('bird', 'Pássaro'),
    ]
    animal_type = models.CharField(
        max_length=8,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0][0]
    )

    available = models.BooleanField(default=True)

    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name
