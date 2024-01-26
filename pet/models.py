from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
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
    owner = models.ForeignKey(
        User,
        related_name='owned_pets',
        on_delete=models.CASCADE
    )
    adopter = models.ForeignKey(
        User,
        related_name='adopted_pets',
        default=None,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class PetImages(models.Model):
    picture = models.ImageField(
        upload_to='pet_imgs/%Y'
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Pet Images'

    def __str__(self):
        return f'Imagem pet - {self.pet}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='user_imgs/%Y', blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
