from django.shortcuts import render
from pet.models import Pet, PetImages


def home(request):
    all_pets = Pet.objects.all()

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
