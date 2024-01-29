from email.mime import image
from django.shortcuts import get_object_or_404, redirect, render
from pet.forms import RegisterUser, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from pet.models import UserProfile


def register_user(request):
    form = RegisterUser()
    profile = UserProfileForm()

    if request.method == 'POST':
        form = RegisterUser(request.POST)
        profile = UserProfileForm(request.POST, files=request.FILES)

        if form.is_valid() and profile.is_valid():
            user = form.save()
            user_profile = profile.save(commit=False)
            user_profile.user_id = user.id
            user_profile.save()
            messages.success(request, 'Usuário Cadastrado!')

            return redirect('pets:login')

    return render(
        request,
        'pet/user_register.html',
        {
            'form': form,
            'profile': profile
        }
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
    user_form = RegisterUser(instance=user)
    user_profile = UserProfile.objects.get(user_id=user.id)
    profile_form = UserProfileForm(instance=user_profile)
    image = UserProfile.objects.get(user_id=user.id).picture

    if request.method == 'POST':
        user_form = RegisterUser(
            request.POST,
            instance=request.user,
            request=request
        )
        profile_form = UserProfileForm(
            data=request.POST, files=request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Usuário atualizado.')

            auth.login(request, user)
            return redirect('pets:my_pets')
        else:
            print(f'ERROS {user_form.errors}')

        return redirect('pets:profile')

    return render(
        request,
        'pet/user_register.html',
        {
            'form': user_form,
            'profile': profile_form,
            'image': image,
            'is_edit': True
        }
    )
