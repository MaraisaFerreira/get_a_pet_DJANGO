import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from pet.models import Pet, UserProfile


class RegisterUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegisterUser, self).__init__(*args, **kwargs)

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
        stored_email = User.objects.filter(email=email)

        logged_user = self.request.user if self.request else None

        if stored_email and logged_user.email != email:
            self.add_error(
                'email',
                ValidationError('esse email já existe escolha outro.')
            )

        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        stored_username = User.objects.filter(username=username)
        logged_user = self.request.user if self.request else None

        if stored_username and logged_user.username != username:
            self.add_error(
                'username',
                ValidationError('Esse nome usuario já existe')
            )

        return username


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(
        required=True,
        min_length=10,
        max_length=15
    )

    picture = forms.ImageField(label='Imagem', required=False)

    class Meta:
        model = UserProfile
        fields = ('phone', 'picture')

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not re.match('^[0-9]+$', phone):
            self.add_error(
                'phone',
                ValidationError(
                    'Apenas Números, mínimo de 10 dígitos'
                )
            )

        return phone


class PetRegister(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'name',
            'color',
            'age',
            'age_type',
            'animal_type',
            'available',
        )
        labels = {
            'name': 'Nome',
            'color': 'Cor',
            'age': 'Idade',
            'age_type': 'Dias?',
            'animal_type': 'Tipo de Animal',
            'available': 'Disponível',
        }
