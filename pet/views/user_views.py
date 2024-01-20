from django.shortcuts import redirect, render
from pet.forms import RegisterUser
from django.contrib import messages


def register_user(request):
    form = RegisterUser()

    if request.method == 'POST':
        form = RegisterUser(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Cadastrado!')

            return redirect('pets:home')

    return render(
        request,
        'pet/user_register.html',
        {'form': form}
    )
