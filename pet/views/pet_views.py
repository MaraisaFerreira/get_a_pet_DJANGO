from django.shortcuts import render
from pet.models import Pet


def home(request):
    pets_list = Pet.objects.all()
    print(pets_list)

    return render(
        request,
        'pet/home.html',
        {
            'pets': pets_list
        }
    )


def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)

    return render(
        request,
        'pet/pet.html',
        {'pet': pet}
    )
