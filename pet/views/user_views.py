from django.shortcuts import redirect, render
from pet.forms import RegisterUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages


def register_user(request):
    form = RegisterUser()

    if request.method == 'POST':
        form = RegisterUser(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Cadastrado!')

            return redirect('pets:login')

    return render(
        request,
        'pet/user_register.html',
        {'form': form}
    )


def user_login(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        user = form.get_user()
        auth.login(request, user)
        messages.success(request, 'Usuario Logado')
        return redirect('pets:home')

    return render(
        request,
        'pet/user_login.html',
        {
            'form': form
        }
    )
