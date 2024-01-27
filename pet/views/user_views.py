from email.mime import image
from django.shortcuts import get_object_or_404, redirect, render
from pet.forms import RegisterUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from pet.models import UserProfile


def register_user(request):
    form = RegisterUser()

    if request.method == 'POST':
        form = RegisterUser(request.POST)

        if form.is_valid():
            picture = request.FILES.get('picture')
            phone = form.cleaned_data['phone']

            user = form.save()
            UserProfile(phone=phone, picture=picture,
                        user_id=user.id).save()
            messages.success(request, 'Usuário Cadastrado!')

            return redirect('pets:login')

    return render(
        request,
        'pet/user_register.html',
        {'form': form}
    )


def user_login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Usuário Logado.')
            return redirect('pets:home')
        messages.error(request, 'Login Invalido')

    return render(
        request,
        'pet/user_login.html',
        {'form': form}
    )


def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout")
    return redirect('pets:home')


def profile(request):
    user = request.user
    form = RegisterUser(instance=user)
    user_profile = UserProfile.objects.get(user_id=user.id)

    if request.method == 'POST':
        form = RegisterUser(
            request.POST,
            instance=request.user,
            request=request
        )

        if form.is_valid():
            picture = request.FILES.get('picture')
            phone = request.POST.get('phone')
            form.save()

            user_profile = get_object_or_404(UserProfile, user=user)
            user_profile.phone = phone
            if picture:
                user_profile.picture = picture
            user_profile.save()

            auth.login(request, user)
            return redirect('pets:my_pets')
        else:
            print(f'ERROS {form.errors}')

        return redirect('pets:profile')

    return render(
        request,
        'pet/user_register.html',
        {
            'form': form,
            'image': user_profile.picture
        }
    )
