from django.shortcuts import redirect, render
from pet.models import Pet, PetImages
from pet.forms import PetRegister
from django.contrib import messages


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
    imagens = PetImages.objects.all().filter(pet_id=pet_id)

    return render(
        request,
        'pet/pet.html',
        {
            'pet': pet,
            'imagens': imagens
        }
    )


def add_pet(request):
    form = PetRegister()

    if request.method == 'POST':
        form = PetRegister(request.POST)

        if form.is_valid():
            pet = form.save()
            files = request.FILES.getlist('images')

            for file in files:
                PetImages(picture=file, pet=pet).save()

        messages.success(request, 'Pet Cadastrado.')

        return redirect('pets:home')

    return render(
        request,
        'pet/add_pet.html',
        {'form': form}
    )


def my_pets(request):
    return render(
        request,
        'pet/my_pets.html'
    )
