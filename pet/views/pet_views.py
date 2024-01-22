from django.shortcuts import redirect, render
from pet import forms
from pet.models import Pet, PetImages
from pet.forms import PetRegister
from django.contrib import messages, auth
from django.contrib.auth.models import User


def home(request):
    all_pets = Pet.objects.all().order_by('-id')

    pet_list = []
    for pet in all_pets:
        imagem = PetImages.objects.filter(pet_id=pet.id).first()
        pet_list.append((pet, imagem))

    return render(
        request,
        'pet/home.html',
        {
            'pets': pet_list
        }
    )


def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    imagens = PetImages.objects.filter(pet_id=pet_id)

    return render(
        request,
        'pet/pet.html',
        {
            'pet': pet,
            'imagens': imagens
        }
    )


def add_pet(request):
    user = auth.get_user(request)
    form = PetRegister()

    if request.method == 'POST':
        form = PetRegister(request.POST)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner_id = user.id
            pet.save()
            files = request.FILES.getlist('images')

            for file in files:
                PetImages(picture=file, pet=pet).save()

        messages.success(request, 'Pet Cadastrado.')

        return redirect('pets:my_pets')

    return render(
        request,
        'pet/add_pet.html',
        {'form': form}
    )


def my_pets(request):
    user = auth.get_user(request)
    pets = Pet.objects.all().filter(owner_id=user.id)

    pets_list = []

    for pet in pets:
        print(f'pet id {pet.id}')
        image = PetImages.objects.filter(pet_id=pet.id).first()
        print(f'imagem {image}')

        adopter = None
        if pet.adopter_id:
            adopter = User.objects.get(id=pet.adopter_id)
            print(f'Adopter {adopter.first_name}')
        pets_list.append((pet, image, adopter))

    return render(
        request,
        'pet/my_pets.html',
        {'pets': pets_list}
    )


def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    form = PetRegister(instance=pet)

    if request.method == 'POST':
        form = PetRegister(request.POST, instance=pet)

        if form.is_valid():
            pet = form.save()
            files = request.FILES.getlist('images')

            for file in files:
                PetImages(picture=file, pet=pet).save()

            messages.success(request, 'Pet Atualizado.')

            return redirect('pets:my_pets')

    return render(
        request,
        'pet/add_pet.html',
        {'form': form}
    )
