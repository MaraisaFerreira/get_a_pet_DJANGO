from django.shortcuts import render
from pet.forms import RegisterUser


def register_user(request):
    form = RegisterUser()

    return render(
        request,
        'pet/user_register.html',
        {'form': form}
    )
