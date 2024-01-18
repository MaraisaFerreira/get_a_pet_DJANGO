from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from pet import models

from pet.models import Pet, PetImages


class RegisterUser(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3
    )

    last_name = forms.CharField(
        required=True,
        min_length=3
    )

    email = forms.EmailField(
        required=True,
        min_length=3
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Esse email já existe, escolha outro.', code='invalid')
            )

        return email


class PetRegister(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'name',
            'color',
            'age',
            'age_type',
            'animal_type',
            'available'
        )
